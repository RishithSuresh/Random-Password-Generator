import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import re
from datetime import datetime

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔑 SecurePass Generator")
        self.root.geometry("500x650")
        self.root.resizable(False, False)

        # Modern color scheme
        self.colors = {
            'bg_primary': '#1a1a2e',
            'bg_secondary': '#16213e',
            'bg_card': '#0f3460',
            'accent': '#e94560',
            'accent_hover': '#c73650',
            'text_primary': '#ffffff',
            'text_secondary': '#b8c5d6',
            'success': '#00d4aa',
            'warning': '#ffb347',
            'danger': '#ff6b6b'
        }

        self.root.configure(bg=self.colors['bg_primary'])

        # Configure modern styles
        self.setup_modern_styles()

        # Create main container
        self.create_main_interface()

        # Center window on screen
        self.center_window()

    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.root.winfo_screenheight() // 2) - (650 // 2)
        self.root.geometry(f"500x650+{x}+{y}")

    def setup_modern_styles(self):
        style = ttk.Style()

        # Configure modern button style
        style.configure('Modern.TButton',
                       background=self.colors['accent'],
                       foreground=self.colors['text_primary'],
                       borderwidth=0,
                       focuscolor='none',
                       font=('Segoe UI', 10, 'bold'),
                       padding=(20, 12))

        style.map('Modern.TButton',
                 background=[('active', self.colors['accent_hover']),
                           ('pressed', self.colors['accent_hover'])])

        # Configure modern frame style
        style.configure('Card.TFrame',
                       background=self.colors['bg_card'],
                       relief='flat',
                       borderwidth=1)

        # Configure modern label styles
        style.configure('Title.TLabel',
                       background=self.colors['bg_primary'],
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 20, 'bold'))

        style.configure('Heading.TLabel',
                       background=self.colors['bg_card'],
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 11, 'bold'))

        style.configure('Body.TLabel',
                       background=self.colors['bg_card'],
                       foreground=self.colors['text_secondary'],
                       font=('Segoe UI', 9))

        # Configure modern checkbutton style
        style.configure('Modern.TCheckbutton',
                       background=self.colors['bg_card'],
                       foreground=self.colors['text_secondary'],
                       font=('Segoe UI', 9),
                       focuscolor='none')

        style.map('Modern.TCheckbutton',
                 background=[('active', self.colors['bg_card'])])

    def create_main_interface(self):
        # Main container
        main_container = tk.Frame(self.root, bg=self.colors['bg_primary'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Title section
        title_frame = tk.Frame(main_container, bg=self.colors['bg_primary'])
        title_frame.pack(fill=tk.X, pady=(0, 30))

        title_label = ttk.Label(title_frame, text="🔑 SecurePass", style='Title.TLabel')
        title_label.pack()

        subtitle_label = ttk.Label(title_frame, text="Generate & Analyze Secure Passwords",
                                  style='Body.TLabel')
        subtitle_label.pack(pady=(5, 0))

        # Create tabbed interface
        self.create_tabbed_interface(main_container)

    def create_tabbed_interface(self, parent):
        # Custom tab container
        tab_container = tk.Frame(parent, bg=self.colors['bg_primary'])
        tab_container.pack(fill=tk.BOTH, expand=True)

        # Tab buttons
        tab_frame = tk.Frame(tab_container, bg=self.colors['bg_primary'])
        tab_frame.pack(fill=tk.X, pady=(0, 20))

        self.current_tab = tk.StringVar(value="generate")

        # Generate tab button
        self.gen_btn = tk.Button(tab_frame, text="Generate Password",
                                command=lambda: self.switch_tab("generate"),
                                bg=self.colors['accent'], fg=self.colors['text_primary'],
                                font=('Segoe UI', 10, 'bold'), relief='flat',
                                padx=20, pady=10, cursor='hand2')
        self.gen_btn.pack(side=tk.LEFT, padx=(0, 10))

        # Analyze tab button
        self.analyze_btn = tk.Button(tab_frame, text="Analyze Password",
                                    command=lambda: self.switch_tab("analyze"),
                                    bg=self.colors['bg_secondary'], fg=self.colors['text_secondary'],
                                    font=('Segoe UI', 10), relief='flat',
                                    padx=20, pady=10, cursor='hand2')
        self.analyze_btn.pack(side=tk.LEFT)

        # Content area
        self.content_frame = tk.Frame(tab_container, bg=self.colors['bg_primary'])
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # Create tab contents
        self.create_generator_content()
        self.create_analyzer_content()

        # Show initial tab
        self.switch_tab("generate")

    def switch_tab(self, tab_name):
        self.current_tab.set(tab_name)

        # Update button styles
        if tab_name == "generate":
            self.gen_btn.configure(bg=self.colors['accent'], fg=self.colors['text_primary'],
                                  font=('Segoe UI', 10, 'bold'))
            self.analyze_btn.configure(bg=self.colors['bg_secondary'], fg=self.colors['text_secondary'],
                                      font=('Segoe UI', 10))
            self.generator_frame.pack(fill=tk.BOTH, expand=True)
            self.analyzer_frame.pack_forget()
        else:
            self.analyze_btn.configure(bg=self.colors['accent'], fg=self.colors['text_primary'],
                                      font=('Segoe UI', 10, 'bold'))
            self.gen_btn.configure(bg=self.colors['bg_secondary'], fg=self.colors['text_secondary'],
                                  font=('Segoe UI', 10))
            self.analyzer_frame.pack(fill=tk.BOTH, expand=True)
            self.generator_frame.pack_forget()

    def create_generator_content(self):
        # Generator frame
        self.generator_frame = tk.Frame(self.content_frame, bg=self.colors['bg_primary'])

        # Length section
        length_card = tk.Frame(self.generator_frame, bg=self.colors['bg_card'], padx=20, pady=15)
        length_card.pack(fill=tk.X, pady=(0, 15))

        ttk.Label(length_card, text="Password Length", style='Heading.TLabel').pack(anchor=tk.W)

        length_control_frame = tk.Frame(length_card, bg=self.colors['bg_card'])
        length_control_frame.pack(fill=tk.X, pady=(10, 0))

        self.length_var = tk.IntVar(value=16)
        self.length_scale = tk.Scale(length_control_frame, from_=8, to=32,
                                    variable=self.length_var, orient=tk.HORIZONTAL,
                                    bg=self.colors['bg_card'], fg=self.colors['text_primary'],
                                    highlightthickness=0, troughcolor=self.colors['bg_secondary'],
                                    activebackground=self.colors['accent'],
                                    font=('Segoe UI', 9), command=self.update_length_label)
        self.length_scale.pack(fill=tk.X)

        self.length_display = tk.Label(length_control_frame, text="16 characters",
                                      bg=self.colors['bg_card'], fg=self.colors['accent'],
                                      font=('Segoe UI', 10, 'bold'))
        self.length_display.pack(pady=(5, 0))

        # Options section
        options_card = tk.Frame(self.generator_frame, bg=self.colors['bg_card'], padx=20, pady=15)
        options_card.pack(fill=tk.X, pady=(0, 15))

        ttk.Label(options_card, text="Character Types", style='Heading.TLabel').pack(anchor=tk.W)

        options_grid = tk.Frame(options_card, bg=self.colors['bg_card'])
        options_grid.pack(fill=tk.X, pady=(10, 0))

        self.use_upper = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        self.exclude_ambiguous = tk.BooleanVar(value=True)

        # Create modern checkboxes
        self.create_modern_checkbox(options_grid, "Uppercase (A-Z)", self.use_upper, 0)
        self.create_modern_checkbox(options_grid, "Numbers (0-9)", self.use_digits, 1)
        self.create_modern_checkbox(options_grid, "Symbols (!@#$)", self.use_symbols, 2)
        self.create_modern_checkbox(options_grid, "Exclude Similar (0,O,l,1)", self.exclude_ambiguous, 3)

        # Generate button
        generate_btn = tk.Button(self.generator_frame, text="🎲 Generate Secure Password",
                                command=self.generate_password,
                                bg=self.colors['accent'], fg=self.colors['text_primary'],
                                font=('Segoe UI', 12, 'bold'), relief='flat',
                                padx=30, pady=15, cursor='hand2')
        generate_btn.pack(pady=15)

        # Result section
        result_card = tk.Frame(self.generator_frame, bg=self.colors['bg_card'], padx=20, pady=15)
        result_card.pack(fill=tk.X, pady=(0, 15))

        ttk.Label(result_card, text="Generated Password", style='Heading.TLabel').pack(anchor=tk.W)

        # Password display
        password_frame = tk.Frame(result_card, bg=self.colors['bg_secondary'], padx=15, pady=10)
        password_frame.pack(fill=tk.X, pady=(10, 15))

        self.password_var = tk.StringVar(value="Click generate to create a password")
        self.password_label = tk.Label(password_frame, textvariable=self.password_var,
                                      bg=self.colors['bg_secondary'], fg=self.colors['text_primary'],
                                      font=('Consolas', 11), wraplength=400, justify=tk.LEFT)
        self.password_label.pack()

        # Action buttons
        btn_frame = tk.Frame(result_card, bg=self.colors['bg_card'])
        btn_frame.pack(fill=tk.X)

        copy_btn = tk.Button(btn_frame, text="📋 Copy", command=self.copy_password,
                            bg=self.colors['success'], fg=self.colors['text_primary'],
                            font=('Segoe UI', 9, 'bold'), relief='flat',
                            padx=15, pady=8, cursor='hand2')
        copy_btn.pack(side=tk.LEFT, padx=(0, 10))

        save_btn = tk.Button(btn_frame, text="💾 Save", command=self.save_password,
                            bg=self.colors['bg_secondary'], fg=self.colors['text_primary'],
                            font=('Segoe UI', 9, 'bold'), relief='flat',
                            padx=15, pady=8, cursor='hand2')
        save_btn.pack(side=tk.LEFT)

        # Strength indicator
        self.strength_card = tk.Frame(self.generator_frame, bg=self.colors['bg_card'], padx=20, pady=15)
        self.strength_card.pack(fill=tk.X)

        ttk.Label(self.strength_card, text="Password Strength", style='Heading.TLabel').pack(anchor=tk.W)

        self.strength_bar_frame = tk.Frame(self.strength_card, bg=self.colors['bg_card'])
        self.strength_bar_frame.pack(fill=tk.X, pady=(10, 5))

        self.strength_bar = tk.Frame(self.strength_bar_frame, bg=self.colors['bg_secondary'], height=8)
        self.strength_bar.pack(fill=tk.X)

        self.strength_fill = tk.Frame(self.strength_bar, bg=self.colors['text_secondary'], height=8)

        self.strength_text = tk.Label(self.strength_card, text="Generate a password to see strength analysis",
                                     bg=self.colors['bg_card'], fg=self.colors['text_secondary'],
                                     font=('Segoe UI', 9))
        self.strength_text.pack(pady=(5, 0))

    def create_modern_checkbox(self, parent, text, variable, row):
        cb_frame = tk.Frame(parent, bg=self.colors['bg_card'])
        cb_frame.pack(fill=tk.X, pady=2)

        checkbox = tk.Checkbutton(cb_frame, text=text, variable=variable,
                                 bg=self.colors['bg_card'], fg=self.colors['text_secondary'],
                                 selectcolor=self.colors['accent'], activebackground=self.colors['bg_card'],
                                 font=('Segoe UI', 9), relief='flat', borderwidth=0)
        checkbox.pack(anchor=tk.W)

    def update_length_label(self, value=None):
        length = int(self.length_var.get())
        self.length_display.config(text=f"{length} characters")

    def create_analyzer_content(self):
        # Analyzer frame
        self.analyzer_frame = tk.Frame(self.content_frame, bg=self.colors['bg_primary'])

        # Input section
        input_card = tk.Frame(self.analyzer_frame, bg=self.colors['bg_card'], padx=20, pady=15)
        input_card.pack(fill=tk.X, pady=(0, 15))

        ttk.Label(input_card, text="Enter Password to Analyze", style='Heading.TLabel').pack(anchor=tk.W)

        input_frame = tk.Frame(input_card, bg=self.colors['bg_secondary'], padx=15, pady=10)
        input_frame.pack(fill=tk.X, pady=(10, 15))

        self.analyze_entry = tk.Entry(input_frame, font=('Consolas', 11),
                                     bg=self.colors['bg_secondary'], fg=self.colors['text_primary'],
                                     relief='flat', borderwidth=0, insertbackground=self.colors['text_primary'])
        self.analyze_entry.pack(fill=tk.X)
        self.analyze_entry.bind('<KeyRelease>', self.on_analyze_text_change)

        analyze_btn = tk.Button(input_card, text="🔍 Analyze Password Strength",
                               command=self.analyze_password,
                               bg=self.colors['accent'], fg=self.colors['text_primary'],
                               font=('Segoe UI', 11, 'bold'), relief='flat',
                               padx=25, pady=12, cursor='hand2')
        analyze_btn.pack()

        # Results section
        self.analysis_card = tk.Frame(self.analyzer_frame, bg=self.colors['bg_card'], padx=20, pady=15)
        self.analysis_card.pack(fill=tk.BOTH, expand=True)

        ttk.Label(self.analysis_card, text="Analysis Results", style='Heading.TLabel').pack(anchor=tk.W)

        # Strength visualization
        self.analysis_strength_frame = tk.Frame(self.analysis_card, bg=self.colors['bg_card'])
        self.analysis_strength_frame.pack(fill=tk.X, pady=(15, 10))

        self.analysis_strength_bar = tk.Frame(self.analysis_strength_frame, bg=self.colors['bg_secondary'], height=12)
        self.analysis_strength_bar.pack(fill=tk.X)

        self.analysis_strength_fill = tk.Frame(self.analysis_strength_bar, bg=self.colors['text_secondary'], height=12)

        self.analysis_strength_label = tk.Label(self.analysis_card, text="Enter a password to see analysis",
                                               bg=self.colors['bg_card'], fg=self.colors['text_secondary'],
                                               font=('Segoe UI', 10, 'bold'))
        self.analysis_strength_label.pack(pady=(5, 15))

        # Detailed analysis
        analysis_scroll_frame = tk.Frame(self.analysis_card, bg=self.colors['bg_secondary'])
        analysis_scroll_frame.pack(fill=tk.BOTH, expand=True)

        self.analysis_text = tk.Text(analysis_scroll_frame, wrap=tk.WORD,
                                    bg=self.colors['bg_secondary'], fg=self.colors['text_secondary'],
                                    font=('Segoe UI', 9), relief='flat', borderwidth=0,
                                    padx=15, pady=10)

        scrollbar = tk.Scrollbar(analysis_scroll_frame, orient=tk.VERTICAL, command=self.analysis_text.yview)
        self.analysis_text.configure(yscrollcommand=scrollbar.set)

        self.analysis_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def on_analyze_text_change(self, event=None):
        # Real-time analysis as user types
        password = self.analyze_entry.get()
        if password:
            self.update_analysis_display(password)
        else:
            self.clear_analysis_display()

    def clear_analysis_display(self):
        self.analysis_strength_fill.place_forget()
        self.analysis_strength_label.config(text="Enter a password to see analysis")
        self.analysis_text.delete(1.0, tk.END)

    def generate_password(self):
        try:
            length = self.length_var.get()

            # Build character set
            characters = string.ascii_lowercase

            if self.use_upper.get():
                characters += string.ascii_uppercase
            if self.use_digits.get():
                characters += string.digits
            if self.use_symbols.get():
                characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"

            # Remove ambiguous characters if requested
            if self.exclude_ambiguous.get():
                ambiguous = "0O1lI"
                characters = ''.join(c for c in characters if c not in ambiguous)

            if not characters:
                messagebox.showerror("Error", "Please select at least one character type!")
                return

            # Generate password ensuring at least one character from each selected type
            password_chars = []

            # Ensure at least one character from each selected type
            if self.use_upper.get():
                upper_chars = string.ascii_uppercase
                if self.exclude_ambiguous.get():
                    upper_chars = ''.join(c for c in upper_chars if c not in "O")
                if upper_chars:
                    password_chars.append(random.choice(upper_chars))

            if self.use_digits.get():
                digit_chars = string.digits
                if self.exclude_ambiguous.get():
                    digit_chars = ''.join(c for c in digit_chars if c not in "01")
                if digit_chars:
                    password_chars.append(random.choice(digit_chars))

            if self.use_symbols.get():
                symbol_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
                password_chars.append(random.choice(symbol_chars))

            # Fill remaining length with random characters
            remaining_length = length - len(password_chars)
            for _ in range(remaining_length):
                password_chars.append(random.choice(characters))

            # Shuffle the password characters
            random.shuffle(password_chars)
            password = ''.join(password_chars)

            # Display password
            self.password_var.set(password)

            # Show strength
            self.show_strength(password)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate password: {str(e)}")
        
    def show_strength(self, password):
        strength, score, _ = self.evaluate_password_strength(password)

        # Update strength bar
        strength_colors = {
            "Very Weak": self.colors['danger'],
            "Weak": "#ff9500",
            "Fair": self.colors['warning'],
            "Good": "#00b894",
            "Strong": self.colors['success']
        }

        color = strength_colors.get(strength, self.colors['text_secondary'])
        width_percent = score / 100

        # Animate strength bar
        self.strength_fill.place_forget()
        self.strength_fill.configure(bg=color)
        self.strength_fill.place(relwidth=width_percent, relheight=1)

        # Update text
        self.strength_text.config(text=f"{strength} • {score}/100 points", fg=color)

    def copy_password(self):
        password = self.password_var.get()
        if password and password != "Click generate to create a password":
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            # Show temporary success message
            original_text = self.password_var.get()
            self.password_var.set("✓ Copied to clipboard!")
            self.root.after(1500, lambda: self.password_var.set(original_text))
        else:
            messagebox.showwarning("No Password", "Generate a password first!")

    def save_password(self):
        password = self.password_var.get()
        if not password or password == "Click generate to create a password":
            messagebox.showwarning("No Password", "Generate a password first!")
            return

        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("passwords.txt", "a", encoding='utf-8') as f:
                f.write(f"{timestamp} - {password}\n")
            messagebox.showinfo("Saved", "Password saved to passwords.txt!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {str(e)}")

    def analyze_password(self):
        password = self.analyze_entry.get().strip()
        if not password:
            messagebox.showwarning("No Password", "Please enter a password to analyze!")
            return
        self.update_analysis_display(password)

    def update_analysis_display(self, password):
        strength, score, feedback = self.evaluate_password_strength(password)

        # Update strength bar
        strength_colors = {
            "Very Weak": self.colors['danger'],
            "Weak": "#ff9500",
            "Fair": self.colors['warning'],
            "Good": "#00b894",
            "Strong": self.colors['success']
        }

        color = strength_colors.get(strength, self.colors['text_secondary'])
        width_percent = score / 100

        # Update strength visualization
        self.analysis_strength_fill.place_forget()
        self.analysis_strength_fill.configure(bg=color)
        self.analysis_strength_fill.place(relwidth=width_percent, relheight=1)

        self.analysis_strength_label.config(text=f"{strength} • {score}/100 points", fg=color)

        # Create detailed analysis
        analysis = f"📊 Password Analysis for: {password}\n"
        analysis += f"{'='*50}\n\n"

        analysis += f"📏 Length: {len(password)} characters\n"
        analysis += f"🎯 Strength: {strength}\n"
        analysis += f"📈 Score: {score}/100 points\n\n"

        # Character breakdown
        analysis += "🔤 Character Composition:\n"
        analysis += f"   • Lowercase: {sum(1 for c in password if c.islower())}\n"
        analysis += f"   • Uppercase: {sum(1 for c in password if c.isupper())}\n"
        analysis += f"   • Numbers: {sum(1 for c in password if c.isdigit())}\n"
        analysis += f"   • Symbols: {sum(1 for c in password if c in string.punctuation)}\n\n"

        # Detailed feedback
        analysis += "🔍 Security Analysis:\n"
        for item in feedback:
            analysis += f"   {item}\n"

        analysis += "\n💡 Recommendations:\n"
        if score < 50:
            analysis += "   • Use at least 12 characters\n"
            analysis += "   • Mix uppercase, lowercase, numbers & symbols\n"
            analysis += "   • Avoid common words and patterns\n"
        elif score < 80:
            analysis += "   • Good foundation! Consider adding length\n"
            analysis += "   • Ensure uniqueness across accounts\n"
        else:
            analysis += "   • Excellent security! Keep it safe\n"
            analysis += "   • Never reuse for other accounts\n"

        # Display analysis
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
    PasswordGeneratorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
