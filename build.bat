@echo off
echo 🔑 SecurePass Generator - Building Executable...
echo.

REM Install PyInstaller if needed
pip install pyinstaller

REM Build the executable
pyinstaller --onefile --windowed --name="SecurePass-Generator" --clean --distpath=dist password_generator_gui.py

REM Clean up
rmdir /s /q build 2>nul
del SecurePass-Generator.spec 2>nul

echo.
echo ✅ Build complete! 
echo 📁 Executable location: dist\SecurePass-Generator.exe
echo.
pause
