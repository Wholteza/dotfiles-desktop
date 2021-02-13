#!/bin/bash
echo "--- Git Sync ---"
echo "Dotfiles"
yadm add -u && yadm commit -m "Automatic commit" && yadm pull && yadm push
echo ""

echo "Password store:"
cd ~/.password-store && git add -A && git commit -m "Automatic commit" && git pull && git push
echo ""

echo "Notable:"
cd ~/.notable && git add -A && git commit -m "Automatic commit" && git pull && git push
echo ""
