@echo off
@REM Batchfile simples apenas para iniciar o django e react automaticamente.
title Staring Django and React
cls

:django
cd backend
.venv\Scripts\activate && start py manege.py runserver
cd..

:react
cd frontend
start npm run dev

exit /b