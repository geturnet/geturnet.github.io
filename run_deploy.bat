@echo off
title Geturnet Auto Deploy Engine
echo =======================================================
echo  [1/3] Menjalankan Generator Artikel Python...
echo =======================================================
python generate_blog.py

echo.
echo =======================================================
echo  [2/3] Menyalin file Web ke Root Direktori...
echo =======================================================
xcopy /E /Y geturnet_blog\* .

echo.
echo =======================================================
echo  [3/3] Melakukan Push ke Repositori GitHub...
echo =======================================================
git add .
git commit -m "Build: Auto-generate 300 artikel SEO via Nabi Group Engine"
git push origin main

echo.
echo =======================================================
echo  [SUKSES] Proses Selesai! Blog Anda sedang diperbarui.
echo =======================================================
pause
