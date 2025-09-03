@echo off
echo 🔍 Password Strength Analyzer - Building Executable...
echo.

REM Install PyInstaller if needed
pip install pyinstaller

REM Build the executable
pyinstaller --onefile --windowed --name="Password-Analyzer" --clean --distpath=dist password_analyzer.py

REM Clean up
rmdir /s /q build 2>nul
del Password-Analyzer.spec 2>nul

echo.
echo ✅ Build complete!
echo 📁 Executable location: dist\Password-Analyzer.exe
echo.
pause
