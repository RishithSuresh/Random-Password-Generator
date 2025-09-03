#!/usr/bin/env python3
"""
Build script to create executable for SecurePass Generator
"""

import os
import subprocess
import sys
from pathlib import Path

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("✓ PyInstaller is already installed")
    except ImportError:
        print("📦 Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✓ PyInstaller installed successfully")

def create_executable():
    """Create the executable using PyInstaller"""
    print("🔨 Building Password Strength Analyzer executable...")

    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",                    # Create single executable file
        "--windowed",                   # Hide console window (GUI app)
        "--name=Password-Analyzer",     # Name of the executable
        "--icon=NONE",                  # No icon for now
        "--clean",                      # Clean PyInstaller cache
        "--distpath=dist",              # Output directory
        "password_analyzer.py"          # Main script
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("✅ Executable created successfully!")
        print("📁 Location: dist/Password-Analyzer.exe")
        print("\n🎉 You can now distribute the executable to other users!")
        print("   They don't need Python installed to run it.")

    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating executable: {e}")
        return False

    return True

def cleanup():
    """Clean up build files"""
    import shutil

    build_dir = Path("build")
    spec_file = Path("Password-Analyzer.spec")

    if build_dir.exists():
        shutil.rmtree(build_dir)
        print("🧹 Cleaned up build directory")

    if spec_file.exists():
        spec_file.unlink()
        print("🧹 Cleaned up spec file")

def main():
    print("🔍 Password Strength Analyzer - Executable Builder")
    print("=" * 50)

    # Check if main script exists
    if not Path("password_analyzer.py").exists():
        print("❌ Error: password_analyzer.py not found!")
        return
    
    # Install PyInstaller
    install_pyinstaller()
    
    # Create executable
    if create_executable():
        # Clean up
        cleanup()
        
        print("\n📋 Distribution Instructions:")
        print("1. Share the 'dist/Password-Analyzer.exe' file")
        print("2. Users can run it directly without Python")
        print("3. The executable is portable and self-contained")
    else:
        print("❌ Build failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
