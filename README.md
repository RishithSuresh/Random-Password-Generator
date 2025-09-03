# 🔑 SecurePass Generator

A modern, sleek password generator and analyzer with an intuitive GUI and powerful security features. Generate ultra-secure passwords and analyze password strength with real-time feedback.

## ✨ Features

### Password Generation
- Generate passwords of any length (4-50 characters)
- Customizable character sets:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Symbols (!@#$%^&*)
- Option to exclude ambiguous characters (0, O, l, 1, I)
- Real-time password strength evaluation
- Copy to clipboard functionality
- Save passwords with timestamps

### Password Analysis
- Comprehensive password strength evaluation
- Detailed security scoring (0-100)
- Character composition analysis
- Pattern detection (repeated sequences, common patterns)
- Security recommendations
- Visual strength indicators

### User Interfaces
- **Modern GUI**: Sleek dark theme with smooth animations and intuitive controls
- **Classic CLI**: Simple command-line interface for quick generation
- **Smart Launcher**: Choose your preferred interface at startup
- **Executable Version**: Standalone .exe file for easy distribution

## 🚀 Quick Start

### Option 1: Use the Launcher (Recommended)
```bash
python main.py
```
Choose between GUI (1) or CLI (2) interface.

### Option 2: Direct Launch
```bash
# Launch GUI directly
python password_generator_gui.py

# Launch CLI directly
python password_generator.py
```

## 📋 Requirements

- Python 3.x
- No external dependencies for running (uses only built-in modules)
- tkinter (included with most Python installations)
- PyInstaller (only needed for building executable)

## 📦 Building Executable

To create a standalone executable that others can use without Python:

### Option 1: Use the Build Script (Recommended)
```bash
python build_exe.py
```

### Option 2: Use the Batch File (Windows)
```bash
build.bat
```

### Option 3: Manual Build
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name="SecurePass-Generator" password_generator_gui.py
```

The executable will be created in the `dist/` folder as `SecurePass-Generator.exe`

## 🖼️ Modern GUI Features

The sleek graphical interface includes:

### Generate Password Section
- Smooth length slider (8-32 characters)
- Modern toggle switches for character types
- Real-time strength visualization with animated bars
- One-click copy with visual feedback
- Smart password generation ensuring character variety

### Analyze Password Section
- Real-time analysis as you type
- Animated strength indicators
- Comprehensive security scoring
- Detailed feedback and recommendations
- Beautiful dark theme with accent colors

## 💻 CLI Features

The command-line version provides:
- Step-by-step password generation
- Customizable options
- File saving capability
- Simple and fast operation

## 📊 Password Strength Evaluation

The strength analyzer evaluates passwords based on:

- **Length**: Longer passwords score higher
- **Character Variety**: Mix of uppercase, lowercase, digits, symbols
- **Pattern Detection**: Avoids repeated sequences and common patterns
- **Sequential Characters**: Detects and penalizes sequential patterns
- **Common Words**: Identifies common weak patterns

### Strength Levels
- 🔴 **Very Weak** (0-29): Highly vulnerable
- 🟠 **Weak** (30-49): Easily crackable
- 🟡 **Fair** (50-69): Moderate security
- 🟢 **Good** (70-84): Strong security
- 🔵 **Strong** (85-100): Excellent security

## 📁 File Structure

```
SecurePass Generator/
├── main.py                    # Smart launcher script
├── password_generator_gui.py  # Modern GUI application
├── password_generator.py      # Classic CLI version
├── build_exe.py              # Executable builder script
├── build.bat                 # Windows build batch file
├── requirements.txt          # Build dependencies
├── passwords.txt             # Saved passwords (auto-created)
├── dist/                     # Executable output folder
└── README.md                 # Documentation
```

## 🔒 Security Best Practices

- Use passwords with 12+ characters
- Include all character types (upper, lower, digits, symbols)
- Avoid common words and patterns
- Don't reuse passwords across accounts
- Store passwords securely
- Consider using a password manager

## 🎯 Example Usage

### GUI Example
1. Launch with `python main.py` and select GUI
2. Adjust length slider to desired length
3. Select character types
4. Click "Generate Password"
5. View strength analysis
6. Copy or save as needed

### CLI Example
```
🔑 Password Generator 🔑
Enter password length: 16
Include uppercase letters? (y/n): y
Include digits? (y/n): y
Include symbols? (y/n): y

✅ Your generated password is: K8#mP2$vN9@qR5!x

Do you want to save this password to a file? (y/n): y
📁 Password saved in 'passwords.txt'
```