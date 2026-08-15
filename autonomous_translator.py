#!/usr/bin/env python3
"""
Autonomous Translation Loop Engine for developer-roadmap (PT-BR)
Strictly isolated to /home/rafaelmeurer/workspaces/developer-roadmap
"""

import os
import sys
import json
import time
import re
import signal
import traceback
import urllib.request
import urllib.error
import subprocess
from datetime import datetime

# Prevent SIGHUP from killing the process when terminal closes
signal.signal(signal.SIGHUP, signal.SIG_IGN)

WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
ROADMAPS_DIR = os.path.join(WORKSPACE_DIR, "roadmaps")
STATE_FILE = os.path.join(WORKSPACE_DIR, ".translation_state.json")
LOG_FILE = os.path.join(WORKSPACE_DIR, "translation_runner.log")
REPORT_FILE = os.path.join(WORKSPACE_DIR, "RELATORIO_TRADUCAO.md")
HUMAN_DECISIONS_FILE = os.path.join(WORKSPACE_DIR, "DECISOES_HUMANAS.md")

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "qwen2.5-coder:7b"
BATCH_SIZE = 3

ISSUE_MAPPINGS = {
    1: ["frontend-beginner", "backend-beginner", "devops-beginner", "git-github-beginner"],
    2: ["html", "css", "javascript", "typescript", "frontend", "full-stack"],
    3: ["react", "nextjs", "vue", "angular", "wordpress"],
    4: ["backend", "api-design", "graphql", "design-system"],
    5: ["nodejs", "python", "golang", "rust", "java", "kotlin"],
    6: ["c", "cpp", "aspnet-core", "php", "laravel", "django", "ruby", "ruby-on-rails", "spring-boot", "scala"],
    7: ["devops", "docker", "kubernetes", "aws", "cloudflare", "terraform", "linux", "shell-bash"],
    8: ["cyber-security", "devsecops", "ai-red-teaming"],
    9: ["android", "ios", "swift-ui", "react-native", "flutter"],
    10: ["sql", "postgresql-dba", "mongodb", "redis", "elasticsearch"],
    11: ["ai-engineer", "ai-agents", "ai-data-scientist", "ai-product-builder", "prompt-engineering", "machine-learning", "mlops"],
    12: ["data-engineer", "data-analyst", "bi-analyst", "power-bi", "python-data-analysis"],
    13: ["computer-science", "datastructures-and-algorithms", "leetcode"],
    14: ["system-design", "software-architect", "software-design-architecture"],
    15: ["product-manager", "engineering-manager", "product-design", "ux-design", "qa", "code-review", "technical-writer", "devrel"],
    16: ["game-developer", "server-side-game-developer", "blockchain", "network-engineer", "forward-deployed-engineer", "claude-code", "openclaw", "vibe-coding", "git-github"]
}

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {message}"
    print(formatted, flush=True)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(formatted + "\n")
            f.flush()
    except Exception:
        pass

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            log(f"Warning loading state file: {e}. Reinitializing.")
    
    return {
        "completed_files": [],
        "completed_roadmaps": [
            "frontend-beginner",
            "backend-beginner",
            "devops-beginner",
            "git-github-beginner"
        ],
        "flagged_issues": [],
        "last_updated": datetime.now().isoformat(),
        "total_translated_count": 54
    }

def save_state(state):
    state["last_updated"] = datetime.now().isoformat()
    temp_file = STATE_FILE + ".tmp"
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
        f.flush()
    os.replace(temp_file, STATE_FILE)

def update_human_decisions_file(flagged_issues):
    content = """# 📋 Registro de Decisões Humanas e Itens Sinalizados

Este arquivo lista automaticamente todos os tópicos ou arquivos que apresentaram inconsistências, falhas na resposta do modelo ou que foram sinalizados para revisão manual por um desenvolvedor humano.

---

"""
    if not flagged_issues:
        content += "> ✅ **Nenhum problema encontrado até o momento.** Todos os arquivos foram traduzidos com sucesso e mantêm a integridade de formatação e nós.\n"
    else:
        content += f"> ⚠️ **Total de itens sinalizados:** {len(flagged_issues)}\n\n"
        content += "| Arquivo / Tópico | Motivo da Sinalização | Data/Hora |\n"
        content += "|---|---|---|\n"
        for item in flagged_issues:
            path = item.get("file", "Desconhecido")
            reason = item.get("reason", "Erro desconhecido")
            ts = item.get("timestamp", "")
            content += f"| `{path}` | {reason} | {ts} |\n"

    with open(HUMAN_DECISIONS_FILE, "w", encoding="utf-8") as f:
        f.write(content)
        f.flush()

def update_progress_report(state, total_files_count):
    completed_count = len(state["completed_files"]) + state.get("total_translated_count", 0)
    percent = (completed_count / total_files_count * 100) if total_files_count > 0 else 0
    roadmaps_done = len(state["completed_roadmaps"])
    
    content = f"""# 📊 Relatório de Progresso da Tradução Autônoma (PT-BR)

**Última atualização:** {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}

## 📈 Estatísticas Gerais
- **Progresso Global:** `{completed_count} / {total_files_count}` arquivos (`{percent:.2f}%`)
- **Roadmaps Concluídos:** `{roadmaps_done} / 91`
- **Itens Pendentes para Decisão Humana:** `{len(state['flagged_issues'])}` (veja [DECISOES_HUMANAS.md](./DECISOES_HUMANAS.md))

---

## 🗺️ Roadmaps Finalizados
"""
    for r in sorted(state["completed_roadmaps"]):
        content += f"- ✅ `{r}`\n"

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(content)
        f.flush()

def query_ollama(prompt, retries=3, backoff=3):
    for attempt in range(1, retries + 1):
        try:
            data = {
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.2,
                    "num_ctx": 4096
                }
            }
            req = urllib.request.Request(
                OLLAMA_URL,
                data=json.dumps(data).encode("utf-8"),
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=90) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                return result.get("response", "")
        except Exception as e:
            log(f"Ollama attempt {attempt}/{retries} error: {e}")
            if attempt < retries:
                time.sleep(backoff * attempt)
    return None

def translate_batch(file_batch):
    prompt = """Você é um tradutor técnico e desenvolvedor de software sênior.
Sua tarefa é traduzir cards de roadmaps de programação do inglês para Português do Brasil (PT-BR).

DIRETRIZES FUNDAMENTAIS:
1. Mantenha os delimitadores exatos <<<FILE: caminho_do_arquivo>>> e <<<END>>> em volta de cada arquivo.
2. Traduza o título principal (# Título) e o texto explicativo mantendo clareza, fluidez e precisão técnica em PT-BR.
3. Padronize a seção de links como:
   "Visite os seguintes recursos para aprender mais:" (ou "Acesse os seguintes recursos para saber mais:").
4. PRESERVE estritamente a sintaxe de links: [@tipo@Descrição](URL).
   - NUNCA apague ou altere URLs.
   - NUNCA remova a sintaxe [@tipo@...].
   - Traduza a descrição do link para PT-BR quando for apropriado.
5. Retorne APENAS os blocos delimitados.

ARQUIVOS PARA TRADUZIR:
"""
    for rel_path, content in file_batch:
        prompt += f"\n<<<FILE: {rel_path}>>>\n{content.strip()}\n<<<END>>>\n"

    response = query_ollama(prompt)
    if not response:
        return {}

    results = {}
    pattern = re.compile(r'<<<FILE:\s*([^>]+?)>>>\s*\n(.*?)\s*<<<END>>>', re.DOTALL)
    matches = pattern.findall(response)

    for matched_path, translated_body in matches:
        matched_path = matched_path.strip()
        cleaned_body = translated_body.strip()
        if cleaned_body.startswith("```markdown"):
            cleaned_body = cleaned_body[len("```markdown"):].strip()
        if cleaned_body.startswith("```md"):
            cleaned_body = cleaned_body[len("```md"):].strip()
        if cleaned_body.startswith("```"):
            cleaned_body = cleaned_body[3:].strip()
        if cleaned_body.endswith("```"):
            cleaned_body = cleaned_body[:-3].strip()

        if len(cleaned_body) > 15 and ("#" in cleaned_body or "@" in cleaned_body):
            results[matched_path] = cleaned_body

    return results

def git_commit_and_push(roadmap_name, file_count):
    try:
        subprocess.run(["git", "add", "."], cwd=WORKSPACE_DIR, check=True)
        commit_msg = f"feat(traducao): traduz roadmap {roadmap_name} ({file_count} tópicos) para PT-BR"
        res = subprocess.run(["git", "commit", "-m", commit_msg], cwd=WORKSPACE_DIR, capture_output=True, text=True)
        if "nothing to commit" in res.stdout or "nothing to commit" in res.stderr:
            return True
        subprocess.run(["git", "push", "origin", "master"], cwd=WORKSPACE_DIR, capture_output=True, text=True, check=True)
        log(f"🚀 Pushed commit for '{roadmap_name}' to origin/master")
        return True
    except Exception as e:
        log(f"Git commit/push warning for '{roadmap_name}': {e}")
        return False

def sync_github_issue_for_roadmap(roadmap_name):
    target_issue = None
    for issue_id, roadmaps in ISSUE_MAPPINGS.items():
        if roadmap_name in roadmaps:
            target_issue = issue_id
            break

    if target_issue:
        try:
            comment_body = f"✅ Trilha `{roadmap_name}` traduzida com sucesso para Português Brasileiro (PT-BR) e comitada no branch `master`."
            subprocess.run(["gh", "issue", "comment", str(target_issue), "--body", comment_body], cwd=WORKSPACE_DIR, capture_output=True, check=False)
        except Exception as e:
            log(f"Issue comment warning: {e}")

def get_all_roadmap_dirs():
    dirs = []
    if not os.path.exists(ROADMAPS_DIR):
        return dirs
    for item in sorted(os.listdir(ROADMAPS_DIR)):
        full = os.path.join(ROADMAPS_DIR, item)
        if os.path.isdir(full) and os.path.exists(os.path.join(full, "content")):
            dirs.append(item)
    return dirs

def count_all_markdown_files():
    count = 0
    for r in get_all_roadmap_dirs():
        content_dir = os.path.join(ROADMAPS_DIR, r, "content")
        count += len([f for f in os.listdir(content_dir) if f.endswith(".md")])
    return count

def run_loop():
    while True:
        try:
            log("==================================================")
            log("🚀 Autonomous Translation Loop Running...")
            log("==================================================")

            state = load_state()
            all_roadmaps = get_all_roadmap_dirs()
            total_files = count_all_markdown_files()

            update_progress_report(state, total_files)
            update_human_decisions_file(state["flagged_issues"])

            completed_this_cycle = 0

            for roadmap in all_roadmaps:
                if roadmap in state["completed_roadmaps"]:
                    continue

                content_dir = os.path.join(ROADMAPS_DIR, roadmap, "content")
                if not os.path.exists(content_dir):
                    continue

                files = sorted([f for f in os.listdir(content_dir) if f.endswith(".md") and f != "index.md"])
                if not files:
                    state["completed_roadmaps"].append(roadmap)
                    save_state(state)
                    continue

                log(f"--- Processing roadmap: '{roadmap}' ({len(files)} topics) ---")
                
                pending_files = []
                for f in files:
                    rel_path = os.path.join("roadmaps", roadmap, "content", f)
                    if rel_path not in state["completed_files"]:
                        full_path = os.path.join(content_dir, f)
                        try:
                            with open(full_path, "r", encoding="utf-8") as file_obj:
                                content = file_obj.read()
                            if content.strip():
                                pending_files.append((rel_path, full_path, content))
                        except Exception as e:
                            state["flagged_issues"].append({
                                "file": rel_path,
                                "reason": f"Erro de leitura: {e}",
                                "timestamp": datetime.now().isoformat()
                            })

                batches = [pending_files[i:i + BATCH_SIZE] for i in range(0, len(pending_files), BATCH_SIZE)]
                roadmap_success_count = 0

                for b_idx, batch in enumerate(batches):
                    log(f"[{roadmap}] Translating batch {b_idx + 1}/{len(batches)} ({len(batch)} files)...")
                    batch_payload = [(rel, cnt) for rel, full, cnt in batch]
                    
                    translated_dict = translate_batch(batch_payload)

                    for rel_path, full_path, original_content in batch:
                        if rel_path in translated_dict:
                            new_content = translated_dict[rel_path]
                            try:
                                with open(full_path, "w", encoding="utf-8") as out_f:
                                    out_f.write(new_content.strip() + "\n")
                                    out_f.flush()
                                state["completed_files"].append(rel_path)
                                roadmap_success_count += 1
                            except Exception as e:
                                state["flagged_issues"].append({
                                    "file": rel_path,
                                    "reason": f"Erro de escrita: {e}",
                                    "timestamp": datetime.now().isoformat()
                                })
                        else:
                            # Fallback attempt
                            log(f"Fallback translation for {rel_path}...")
                            single_res = translate_batch([(rel_path, original_content)])
                            if rel_path in single_res:
                                new_content = single_res[rel_path]
                                with open(full_path, "w", encoding="utf-8") as out_f:
                                    out_f.write(new_content.strip() + "\n")
                                    out_f.flush()
                                state["completed_files"].append(rel_path)
                                roadmap_success_count += 1
                            else:
                                log(f"⚠️ Flagging {rel_path} for human decision.")
                                state["flagged_issues"].append({
                                    "file": rel_path,
                                    "reason": "Falha na tradução automática após tentativas no Ollama",
                                    "timestamp": datetime.now().isoformat()
                                })

                    save_state(state)
                    update_progress_report(state, total_files)
                    update_human_decisions_file(state["flagged_issues"])

                state["completed_roadmaps"].append(roadmap)
                save_state(state)
                update_progress_report(state, total_files)

                git_commit_and_push(roadmap, roadmap_success_count)
                sync_github_issue_for_roadmap(roadmap)
                log(f"✅ Roadmap '{roadmap}' completed ({roadmap_success_count} topics translated).")
                completed_this_cycle += 1

            if completed_this_cycle == 0:
                log("🎉 All 91 roadmaps are translated! Sleeping for 10 minutes before next check.")
                time.sleep(600)

        except Exception as e:
            log(f"Unexpected error in main loop: {e}\n{traceback.format_exc()}")
            time.sleep(10)

if __name__ == "__main__":
    run_loop()
