@echo off
chcp 65001 > nul

echo Starting backend server...
cd backend
start "" cmd /k "python app.py"
cd ..

echo Starting frontend server...
cd frontend
start "" cmd /k "python -m http.server 8000"
cd ..

echo Both servers started.
echo Close this window to stop the application.

exit