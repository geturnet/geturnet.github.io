#!/bin/bash
set -e

echo "======================================================="
echo " [1/3] Menjalankan Generator Artikel Python..."
echo "======================================================="
python3 generate_blog.py

echo -e "\n======================================================="
echo " [2/3] Menyalin file Web ke Root Direktori..."
echo "======================================================="
cp -r geturnet_blog/* .

echo -e "\n======================================================="
echo " [3/3] Melakukan Push ke Repositori GitHub..."
echo "======================================================="
git add .
git commit -m "Build: Auto-generate 300 artikel SEO via Nabi Group Engine"
git push origin main

echo -e "\n======================================================="
echo " [SUKSES] Proses Selesai! Blog Anda sedang diperbarui."
echo "======================================================="
