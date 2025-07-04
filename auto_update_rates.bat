@echo off
cd /d "D:\New Project-28-6-2025\pakistan-ka-rates-auto"

echo 🟡 Running update_rates.py...
python scripts\update_rates.py

echo 🟢 Adding all changes to Git...
git add .

echo 🟢 Committing changes...
git commit -m "✅ Auto-updated latest_rates.html and latest_rates.json"

echo 🟢 Pushing to GitHub...
git push

echo ✅ Update complete and pushed successfully!
pause
