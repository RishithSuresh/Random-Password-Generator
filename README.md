# 🔑 Advanced Password Generator & Analyzer

A comprehensive Python application for generating secure passwords and analyzing password strength with both command-line and graphical interfaces.

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
- **GUI Version**: Modern, aesthetic graphical interface with tabs
- **CLI Version**: Simple command-line interface
- **Launcher**: Choose between GUI or CLI at startup

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
- No external dependencies (uses only built-in modules)
- tkinter (included with most Python installations)

## 🖼️ GUI Features

The graphical interface includes:

### Generate Password Tab
- Interactive length slider (4-50 characters)
- Checkboxes for character type selection
- Real-time password strength display
- One-click copy and save functionality

### Analyze Password Tab
- Text input for password analysis
- Detailed strength evaluation
- Character composition breakdown
- Security recommendations
- Color-coded strength indicators

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
Random Password Generator/
├── main.py                    # Main launcher script
├── password_generator_gui.py  # GUI application
├── password_generator.py      # Original CLI version
├── requirements.txt           # Dependencies (none required)
├── passwords.txt             # Saved passwords (auto-created)
└── README.md                 # This file
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