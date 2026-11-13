#!/usr/bin/env bash
# Revue NON INTERACTIVE en CI (proposé, non exécuté par le formateur).
# Options vérifiées dans l'aide de Claude Code 2.1.323 : -p/--print, --output-format, --json-schema, --allowedTools.
set -euo pipefail

SCHEMA='{"type":"object","properties":{"problemes":{"type":"array","items":{"type":"object","properties":{"fichier":{"type":"string"},"gravite":{"type":"string","enum":["bloquant","majeur","mineur"]},"description":{"type":"string"}},"required":["fichier","gravite","description"]}}},"required":["problemes"]}'

claude -p "Fais une revue de src/ selon les règles du projet. Liste uniquement les problèmes réels." \
  --output-format json \
  --json-schema "$SCHEMA" \
  --allowedTools "Read,Grep,Glob" \
  > revue.json

echo "Résultat écrit dans revue.json"
