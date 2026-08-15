#!/usr/bin/env bash
# Quick status monitor for autonomous translation loop
cd "$(dirname "$0")"

echo "=================================================="
echo "📊 STATUS DA TRADUÇÃO AUTÔNOMA (PT-BR)"
echo "=================================================="

if [ -f RELATORIO_TRADUCAO.md ]; then
    cat RELATORIO_TRADUCAO.md
    echo ""
fi

echo "--------------------------------------------------"
echo "📋 DECISÕES HUMANAS PENDENTES:"
if [ -f DECISOES_HUMANAS.md ]; then
    cat DECISOES_HUMANAS.md
    echo ""
fi

echo "--------------------------------------------------"
echo "📜 ÚLTIMAS LINHAS DE LOG (translation_runner.log):"
if [ -f translation_runner.log ]; then
    tail -n 15 translation_runner.log
else
    echo "Nenhum arquivo de log encontrado ainda."
fi
echo "=================================================="
