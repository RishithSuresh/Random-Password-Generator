import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import string
import re
from datetime import datetime

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔑 Advanced Password Generator")
        self.root.geometry("600x700")
        self.root.configure(bg='#2c3e50')
        
        # Configure style
        self.setup_styles()
        
        # Create main frame
        main_frame = ttk.Frame(root, style='Main.TFrame', padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="🔑 Password Generator & Analyzer", 
                               style='Title.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(main_frame, style='Custom.TNotebook')
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_generator_tab()
        self.create_analyzer_tab()
        
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure styles
        style.configure('Main.TFrame', background='#2c3e50')
        style.configure('Title.TLabel', background='#2c3e50', foreground='#ecf0f1', 
                       font=('Arial', 18, 'bold'))
        style.configure('Heading.TLabel', background='#34495e', foreground='#ecf0f1', 
                       font=('Arial', 12, 'bold'))
        style.configure('Custom.TNotebook', background='#2c3e50')
        style.configure('Custom.TNotebook.Tab', background='#34495e', foreground='#ecf0f1',
                       padding=[20, 10])
        style.map('Custom.TNotebook.Tab', background=[('selected', '#3498db')])
        
    def create_generator_tab(self):
        # Generator tab
        gen_frame = ttk.Frame(self.notebook, style='Main.TFrame', padding="20")
        self.notebook.add(gen_frame, text="Generate Password")
        
        # Password length
        length_frame = ttk.Frame(gen_frame, style='Main.TFrame')
        length_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(length_frame, text="Password Length:", style='Heading.TLabel').pack(anchor=tk.W)
        self.length_var = tk.IntVar(value=12)
        length_scale = ttk.Scale(length_frame, from_=4, to=50, variable=self.length_var, 
                                orient=tk.HORIZONTAL)
        length_scale.pack(fill=tk.X, pady=(5, 0))
        
        self.length_label = ttk.Label(length_frame, text="12", style='Heading.TLabel')
        self.length_label.pack(anchor=tk.W)
        length_scale.configure(command=self.update_length_label)
        
        # Options frame
        options_frame = ttk.LabelFrame(gen_frame, text="Character Options", padding="15")
        options_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.use_upper = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        self.use_ambiguous = tk.BooleanVar(value=False)
        
        ttk.Checkbutton(options_frame, text="Include Uppercase Letters (A-Z)", 
                       variable=self.use_upper).pack(anchor=tk.W, pady=2)
        ttk.Checkbutton(options_frame, text="Include Digits (0-9)", 
                       variable=self.use_digits).pack(anchor=tk.W, pady=2)
        ttk.Checkbutton(options_frame, text="Include Symbols (!@#$%^&*)", 
                       variable=self.use_symbols).pack(anchor=tk.W, pady=2)
        ttk.Checkbutton(options_frame, text="Exclude Ambiguous Characters (0,O,l,1)", 
                       variable=self.use_ambiguous).pack(anchor=tk.W, pady=2)
        
        # Generate button
        generate_btn = ttk.Button(gen_frame, text="🎲 Generate Password", 
                                 command=self.generate_password, style='Accent.TButton')
        generate_btn.pack(pady=15)
        
        # Result frame
        result_frame = ttk.LabelFrame(gen_frame, text="Generated Password", padding="15")
        result_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.password_text = tk.Text(result_frame, height=3, wrap=tk.WORD, font=('Courier', 12))
        self.password_text.pack(fill=tk.X, pady=(0, 10))
        
        # Buttons frame
        btn_frame = ttk.Frame(result_frame, style='Main.TFrame')
        btn_frame.pack(fill=tk.X)
        
        ttk.Button(btn_frame, text="📋 Copy", command=self.copy_password).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(btn_frame, text="💾 Save to File", command=self.save_password).pack(side=tk.LEFT)
        
        # Strength indicator
        self.strength_frame = ttk.LabelFrame(gen_frame, text="Password Strength", padding="15")
        self.strength_frame.pack(fill=tk.X)
        
        self.strength_label = ttk.Label(self.strength_frame, text="Generate a password to see strength", 
                                       style='Heading.TLabel')
        self.strength_label.pack()
        
    def create_analyzer_tab(self):
        # Analyzer tab
        analyzer_frame = ttk.Frame(self.notebook, style='Main.TFrame', padding="20")
        self.notebook.add(analyzer_frame, text="Analyze Password")
        
        # Input frame
        input_frame = ttk.LabelFrame(analyzer_frame, text="Enter Password to Analyze", padding="15")
        input_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.analyze_text = tk.Text(input_frame, height=3, wrap=tk.WORD, font=('Courier', 12))
        self.analyze_text.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(input_frame, text="🔍 Analyze Password", 
                  command=self.analyze_password, style='Accent.TButton').pack()
        
        # Results frame
        self.analysis_frame = ttk.LabelFrame(analyzer_frame, text="Analysis Results", padding="15")
        self.analysis_frame.pack(fill=tk.BOTH, expand=True)
        
        self.analysis_text = tk.Text(self.analysis_frame, wrap=tk.WORD, font=('Arial', 10))
        scrollbar = ttk.Scrollbar(self.analysis_frame, orient=tk.VERTICAL, command=self.analysis_text.yview)
        self.analysis_text.configure(yscrollcommand=scrollbar.set)
        
        self.analysis_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def update_length_label(self, value):
        self.length_label.config(text=str(int(float(value))))
        
    def generate_password(self):
        length = self.length_var.get()
        
        # Build character set
        characters = string.ascii_lowercase
        
        if self.use_upper.get():
            characters += string.ascii_uppercase
        if self.use_digits.get():
            characters += string.digits
        if self.use_symbols.get():
            characters += string.punctuation
            
        # Remove ambiguous characters if requested
        if self.use_ambiguous.get():
            ambiguous = "0O1lI"
            characters = ''.join(c for c in characters if c not in ambiguous)
        
        if not characters:
            messagebox.showerror("Error", "Please select at least one character type!")
            return
            
        # Generate password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display password
        self.password_text.delete(1.0, tk.END)
        self.password_text.insert(1.0, password)
        
        # Show strength
        self.show_strength(password)
        
    def show_strength(self, password):
        strength, score, feedback = self.evaluate_password_strength(password)
        
        # Color coding
        colors = {
            "Very Weak": "#e74c3c",
            "Weak": "#f39c12", 
            "Fair": "#f1c40f",
            "Good": "#2ecc71",
            "Strong": "#27ae60"
        }
        
        self.strength_label.config(text=f"Strength: {strength} ({score}/100)",
                                  foreground=colors.get(strength, "#ecf0f1"))

    def copy_password(self):
        password = self.password_text.get(1.0, tk.END).strip()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy!")

    def save_password(self):
        password = self.password_text.get(1.0, tk.END).strip()
        if not password:
            messagebox.showwarning("Warning", "No password to save!")
            return

        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("passwords.txt", "a") as f:
                f.write(f"{timestamp} - {password}\n")
            messagebox.showinfo("Success", "Password saved to passwords.txt!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save password: {str(e)}")

    def analyze_password(self):
        password = self.analyze_text.get(1.0, tk.END).strip()
        if not password:
            messagebox.showwarning("Warning", "Please enter a password to analyze!")
            return

        strength, score, feedback = self.evaluate_password_strength(password)

        # Display detailed analysis
        analysis = f"Password: {password}\n"
        analysis += f"Length: {len(password)} characters\n"
        analysis += f"Strength: {strength}\n"
        analysis += f"Score: {score}/100\n\n"
        analysis += "Detailed Analysis:\n"
        analysis += "=" * 50 + "\n"

        for item in feedback:
            analysis += f"• {item}\n"

        # Character composition
        analysis += f"\nCharacter Composition:\n"
        analysis += "=" * 50 + "\n"
        analysis += f"• Lowercase letters: {sum(1 for c in password if c.islower())}\n"
        analysis += f"• Uppercase letters: {sum(1 for c in password if c.isupper())}\n"
        analysis += f"• Digits: {sum(1 for c in password if c.isdigit())}\n"
        analysis += f"• Symbols: {sum(1 for c in password if c in string.punctuation)}\n"

        # Security recommendations
        analysis += f"\nSecurity Recommendations:\n"
        analysis += "=" * 50 + "\n"
        if score < 60:
            analysis += "• Consider using a longer password (12+ characters)\n"
            analysis += "• Include a mix of uppercase, lowercase, numbers, and symbols\n"
            analysis += "• Avoid common words and patterns\n"
        elif score < 80:
            analysis += "• Good password! Consider making it even longer for better security\n"
            analysis += "• Ensure it's unique and not used elsewhere\n"
        else:
            analysis += "• Excellent password strength!\n"
            analysis += "• Make sure to store it securely\n"
            analysis += "• Don't reuse this password for other accounts\n"

        self.analysis_text.delete(1.0, tk.END)
        self.analysis_text.insert(1.0, analysis)

    def evaluate_password_strength(self, password):
        """Evaluate password strength and return strength level, score, and feedback"""
        score = 0
        feedback = []

        length = len(password)

        # Length scoring
        if length >= 12:
            score += 25
            feedback.append("✓ Good length (12+ characters)")
        elif length >= 8:
            score += 15
            feedback.append("⚠ Adequate length (8+ characters)")
        else:
            feedback.append("✗ Too short (less than 8 characters)")

        # Character variety
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in string.punctuation for c in password)

        char_types = sum([has_lower, has_upper, has_digit, has_symbol])

        if char_types == 4:
            score += 25
            feedback.append("✓ Excellent character variety (all types)")
        elif char_types == 3:
            score += 20
            feedback.append("✓ Good character variety (3 types)")
        elif char_types == 2:
            score += 10
            feedback.append("⚠ Limited character variety (2 types)")
        else:
            feedback.append("✗ Poor character variety (1 type only)")

        # Pattern detection
        if not re.search(r'(.)\1{2,}', password):
            score += 15
            feedback.append("✓ No repeated character sequences")
        else:
            feedback.append("⚠ Contains repeated character sequences")

        # Common patterns
        if not re.search(r'(123|abc|qwe|password|admin)', password.lower()):
            score += 15
            feedback.append("✓ No common patterns detected")
        else:
            feedback.append("✗ Contains common patterns")

        # Sequential characters
        sequential = False
        for i in range(len(password) - 2):
            if (ord(password[i+1]) == ord(password[i]) + 1 and
                ord(password[i+2]) == ord(password[i]) + 2):
                sequential = True
                break

        if not sequential:
            score += 10
            feedback.append("✓ No sequential characters")
        else:
            feedback.append("⚠ Contains sequential characters")

        # Entropy bonus for longer passwords
        if length > 16:
            score += 10
            feedback.append("✓ Bonus for extra length")

        # Determine strength level
        if score >= 85:
            strength = "Strong"
        elif score >= 70:
            strength = "Good"
        elif score >= 50:
            strength = "Fair"
        elif score >= 30:
            strength = "Weak"
        else:
            strength = "Very Weak"

        return strength, min(score, 100), feedback


def main():
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
