# 🔍 Password Strength Analyzer

A comprehensive password security analysis tool with strict evaluation criteria and detailed feedback. Analyze password strength in real-time with professional-grade security assessment.

## ✨ Features

### Comprehensive Password Analysis
- **Strict Security Criteria**: Professional-grade evaluation with rigorous standards
- **Real-time Analysis**: Instant feedback as you type
- **Detailed Scoring**: 100-point scoring system with strict thresholds
- **Multiple Security Checks**:
  - Length analysis (8-16+ characters)
  - Character variety (uppercase, lowercase, digits, symbols)
  - Pattern detection (repeated sequences, common patterns)
  - Dictionary word detection
  - Sequential character analysis
  - Entropy calculation

### Advanced Security Features
- **Crack Time Estimation**: Realistic time-to-crack calculations
- **Visual Strength Indicators**: Color-coded strength levels
- **Comprehensive Reports**: Detailed security analysis with recommendations
- **Professional Feedback**: Specific improvement suggestions
- **Security Best Practices**: Built-in security education

### User Interface
- **Modern GUI**: Sleek dark theme with professional design
- **Real-time Updates**: Instant analysis as you type
- **Password Visibility Toggle**: Show/hide password option
- **Detailed Reports**: Comprehensive analysis in scrollable text area
- **Executable Version**: Standalone .exe file for easy distribution

## 🚀 Quick Start

### Option 1: Use the Launcher (Recommended)
```bash
python main.py
```
Choose between GUI Analyzer (1) or CLI Generator (2).

### Option 2: Direct Launch
```bash
# Launch Password Analyzer directly
python password_analyzer.py

# Launch CLI Generator directly
python password_generator.py
```

### Option 3: Use the Executable
```bash
# Run the standalone executable (no Python required)
dist\Password-Analyzer.exe
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