# ✨ Diretrizes de Contribuição e Tradução (PT-BR) ✨

Agradecemos imensamente seu interesse em contribuir para o projeto de localização e tradução do **developer-roadmap** para Português do Brasil!

## 📋 Sumário
- [Como Contribuir com as Traduções](#como-contribuir-com-as-traduções)
- [Estrutura dos Arquivos](#estrutura-dos-arquivos)
- [Diretrizes de Estilo e Terminologia](#diretrizes-de-estilo-e-terminologia)
- [Tipos de Links Permitidos](#tipos-de-links-permitidos)
- [Passo a Passo de Desenvolvimento Local](#passo-a-passo-de-desenvolvimento-local)

---

## 🎯 Como Contribuir com as Traduções

1. Acesse as [Issues do Repositório](https://github.com/rafameureer/developer-roadmap/issues) para verificar as trilhas abertas ou em andamento.
2. Comente na issue da trilha correspondente informando qual parte você gostaria de traduzir.
3. Crie uma branch específica a partir de `master` (ex: `traducao/frontend-html`).
4. Realize a tradução mantendo o padrão de formato e abra um **Pull Request**.

---

## 📁 Estrutura dos Arquivos

Os conteúdos dos tópicos ficam localizados no diretório `roadmaps/<slug-do-roadmap>/content/`.

Cada arquivo segue a nomenclatura:
```
<slug-do-topico>@<id-do-no>.md
```

> ⚠️ **IMPORTANTE**: Nunca renomeie os arquivos! O sufixo `@id-do-no.md` é a chave única que conecta o texto ao respectivo nó visual no roadmap interativo.

### Formato Padrão do Conteúdo:

```md
# Título do Tópico em Português

Parágrafo conciso e claro explicando o conceito (1 a 2 parágrafos no máximo), utilizando terminologia técnica adequada em português.

Visite os seguintes recursos para aprender mais:

- [@tipo@Título ou Descrição do Link](URL)
```

---

## 🏷️ Tipos de Links Permitidos

O prefixo `@tipo@` categoriza visualmente o recurso no roadmap:

- `@official@` — Documentação ou site oficial
- `@opensource@` — Projetos ou repositórios open-source
- `@article@` — Artigos, tutoriais ou posts em blogs
- `@course@` — Cursos estruturados (gratuitos ou pagos)
- `@podcast@` — Episódios de podcast
- `@video@` — Vídeos no YouTube ou plataformas de vídeo
- `@book@` — Livros técnicos recomendados
- `@roadmap@` — Link para outro roadmap do roadmap.sh

---

## 📖 Diretrizes de Estilo e Terminologia

- **Qualidade Técnica:** Busque naturalidade na escrita em português brasileiro (PT-BR), evitando traduções literais mecânicas.
- **Terminologia Consagrada:** Termos amplamente utilizados pela comunidade em inglês devem ser mantidos ou contextualizados (ex: *commit, pull request, branch, deploy, framework, runtime, cache, middleware*).
- **Recursos em Português:** Sempre que houver documentação oficial ou artigo de referência de alta qualidade em português (como MDN Web Docs em PT-BR ou artigos consolidados), você pode incluí-los ou substituir links quebrados.

---

## 💻 Passo a Passo de Desenvolvimento Local

```bash
# 1. Clone o repositório
git clone https://github.com/rafameureer/developer-roadmap.git
cd developer-roadmap

# 2. Crie uma nova branch
git checkout -b traducao/minha-trilha

# 3. Faça suas edições nos arquivos markdown

# 4. Verifique e comite suas alterações
git add .
git commit -m "traducao: adiciona versao pt-br para trilha X"
git push origin traducao/minha-trilha
```
