@echo off
cd /d %~dp0
call env\Scripts\activate
streamlit run weihnachtsfeier_game.py
pause
