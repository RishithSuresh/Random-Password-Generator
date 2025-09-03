import tkinter as tk
from tkinter import messagebox
import re
import string
import math

class PasswordAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔍 Password Strength Analyzer")
        self.root.geometry("700x800")
        self.root.resizable(True, True)
        
        # Modern color scheme
        self.colors = {
            'bg_primary': '#1a1a2e',
            'bg_secondary': '#16213e', 
            'bg_card': '#0f3460',
            'accent': '#e94560',
            'text_primary': '#ffffff',
            'text_secondary': '#b8c5d6',
            'very_weak': '#ff4757',
            'weak': '#ff6348',
            'fair': '#ffa502',
            'good': '#2ed573',
            'strong': '#1e90ff',
            'very_strong': '#5f27cd'
        }
        
        self.root.configure(bg=self.colors['bg_primary'])
        
        # Create main interface
        self.create_analyzer_interface()
        
        # Center window on screen
        self.center_window()
        
    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (700 // 2)
        y = (self.root.winfo_screenheight() // 2) - (800 // 2)
        self.root.geometry(f"700x800+{x}+{y}")
        
    def create_analyzer_interface(self):
        # Main container
        main_container = tk.Frame(self.root, bg=self.colors['bg_primary'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title section
        title_frame = tk.Frame(main_container, bg=self.colors['bg_primary'])
        title_frame.pack(fill=tk.X, pady=(0, 30))
        
        title_label = tk.Label(title_frame, text="🔍 Password Strength Analyzer", 
                              bg=self.colors['bg_primary'], fg=self.colors['text_primary'],
                              font=('Segoe UI', 20, 'bold'))
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Analyze password strength with strict security criteria", 
                                 bg=self.colors['bg_primary'], fg=self.colors['text_secondary'],
                                 font=('Segoe UI', 10))
        subtitle_label.pack(pady=(5, 0))
        
        # Password input section
        self.create_input_section(main_container)
        
        # Analysis results section
        self.create_results_section(main_container)
        
        # Detailed analysis section
        self.create_detailed_analysis_section(main_container)
        
    def create_input_section(self, parent):
        # Input card
        input_card = tk.Frame(parent, bg=self.colors['bg_card'], padx=25, pady=20)
        input_card.pack(fill=tk.X, pady=(0, 20))
        
        # Title
        input_title = tk.Label(input_card, text="Enter Password to Analyze", 
                              bg=self.colors['bg_card'], fg=self.colors['text_primary'],
                              font=('Segoe UI', 14, 'bold'))
        input_title.pack(anchor=tk.W, pady=(0, 15))
        
        # Password input
        input_frame = tk.Frame(input_card, bg='#ffffff', padx=15, pady=12, 
                              relief='solid', borderwidth=2)
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.password_entry = tk.Entry(input_frame, font=('Consolas', 14), 
                                      bg='#ffffff', fg='#000000',
                                      relief='flat', borderwidth=0, 
                                      insertbackground='#000000', show='')
        self.password_entry.pack(fill=tk.X)
        self.password_entry.bind('<KeyRelease>', self.on_password_change)
        
        # Show/Hide password toggle
        toggle_frame = tk.Frame(input_card, bg=self.colors['bg_card'])
        toggle_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.show_password = tk.BooleanVar()
        show_check = tk.Checkbutton(toggle_frame, text="Show password", 
                                   variable=self.show_password,
                                   command=self.toggle_password_visibility,
                                   bg=self.colors['bg_card'], fg=self.colors['text_secondary'],
                                   selectcolor=self.colors['accent'], 
                                   activebackground=self.colors['bg_card'],
                                   font=('Segoe UI', 9))
        show_check.pack(anchor=tk.W)
        
        # Analyze button
        analyze_btn = tk.Button(input_card, text="🔍 Analyze Password Strength",
                               command=self.analyze_password,
                               bg=self.colors['accent'], fg=self.colors['text_primary'],
                               font=('Segoe UI', 12, 'bold'), relief='flat',
                               padx=30, pady=12, cursor='hand2')
        analyze_btn.pack()
        
    def create_results_section(self, parent):
        # Results card
        self.results_card = tk.Frame(parent, bg=self.colors['bg_card'], padx=25, pady=20)
        self.results_card.pack(fill=tk.X, pady=(0, 15))

        # Title
        results_title = tk.Label(self.results_card, text="Quick Analysis Summary",
                                bg=self.colors['bg_card'], fg=self.colors['text_primary'],
                                font=('Segoe UI', 14, 'bold'))
        results_title.pack(anchor=tk.W, pady=(0, 15))

        # Strength display
        self.strength_display_frame = tk.Frame(self.results_card, bg='#ffffff',
                                              padx=20, pady=15, relief='solid', borderwidth=2)
        self.strength_display_frame.pack(fill=tk.X, pady=(0, 10))

        # Strength level
        self.strength_level = tk.Label(self.strength_display_frame, text="Enter a password to analyze",
                                      bg='#ffffff', fg='#666666',
                                      font=('Segoe UI', 18, 'bold'))
        self.strength_level.pack(pady=(0, 8))

        # Score display
        self.score_display = tk.Label(self.strength_display_frame, text="Score: --/100",
                                     bg='#ffffff', fg='#333333',
                                     font=('Segoe UI', 14, 'bold'))
        self.score_display.pack(pady=(0, 10))

        # Strength bar
        self.strength_bar_frame = tk.Frame(self.strength_display_frame, bg='#e0e0e0', height=25)
        self.strength_bar_frame.pack(fill=tk.X, pady=(0, 10))

        self.strength_bar = tk.Frame(self.strength_bar_frame, bg='#cccccc', height=25)

        # Time to crack
        self.crack_time = tk.Label(self.strength_display_frame, text="Time to crack: --",
                                  bg='#ffffff', fg='#333333',
                                  font=('Segoe UI', 12, 'bold'))
        self.crack_time.pack()

        # Quick summary
        self.quick_summary = tk.Label(self.strength_display_frame, text="",
                                     bg='#ffffff', fg='#333333',
                                     font=('Segoe UI', 10), wraplength=600, justify=tk.CENTER)
        self.quick_summary.pack(pady=(10, 0))
        
    def create_detailed_analysis_section(self, parent):
        # Detailed analysis card
        self.analysis_card = tk.Frame(parent, bg=self.colors['bg_card'], padx=25, pady=20)
        self.analysis_card.pack(fill=tk.BOTH, expand=True)

        # Title
        analysis_title = tk.Label(self.analysis_card, text="📊 Comprehensive Security Analysis & Recommendations",
                                 bg=self.colors['bg_card'], fg=self.colors['text_primary'],
                                 font=('Segoe UI', 14, 'bold'))
        analysis_title.pack(anchor=tk.W, pady=(0, 15))

        # Analysis text area with better sizing
        analysis_frame = tk.Frame(self.analysis_card, bg='#ffffff', relief='solid', borderwidth=2)
        analysis_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        self.analysis_text = tk.Text(analysis_frame, wrap=tk.WORD,
                                    bg='#ffffff', fg='#333333',
                                    font=('Consolas', 10), relief='flat', borderwidth=0,
                                    padx=20, pady=20, state='disabled', height=15)

        scrollbar = tk.Scrollbar(analysis_frame, orient=tk.VERTICAL, command=self.analysis_text.yview)
        self.analysis_text.configure(yscrollcommand=scrollbar.set)

        self.analysis_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Initialize with placeholder text
        self.analysis_text.config(state='normal')
        self.analysis_text.insert(tk.END, "📝 Enter a password above to see comprehensive security analysis...\n\n")
        self.analysis_text.insert(tk.END, "The detailed analysis will include:\n")
        self.analysis_text.insert(tk.END, "• Character composition breakdown\n")
        self.analysis_text.insert(tk.END, "• Security vulnerability assessment\n")
        self.analysis_text.insert(tk.END, "• Pattern detection results\n")
        self.analysis_text.insert(tk.END, "• Specific improvement recommendations\n")
        self.analysis_text.insert(tk.END, "• Security best practices\n")
        self.analysis_text.config(state='disabled')
        
    def toggle_password_visibility(self):
        """Toggle password visibility"""
        if self.show_password.get():
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')
            
    def on_password_change(self, event=None):
        """Real-time analysis as user types"""
        password = self.password_entry.get()
        if password:
            self.analyze_password_strength(password)
        else:
            self.clear_analysis()
            
    def clear_analysis(self):
        """Clear all analysis displays"""
        self.strength_level.config(text="Enter a password to analyze", fg='#666666')
        self.score_display.config(text="Score: --/100")
        self.crack_time.config(text="Time to crack: --")
        self.strength_bar.place_forget()
        
        self.analysis_text.config(state='normal')
        self.analysis_text.delete(1.0, tk.END)
        self.analysis_text.insert(tk.END, "Enter a password above to see detailed security analysis...")
        self.analysis_text.config(state='disabled')
        
    def analyze_password(self):
        """Analyze button click handler"""
        password = self.password_entry.get().strip()
        if not password:
            messagebox.showwarning("No Password", "Please enter a password to analyze!")
            return
        self.analyze_password_strength(password)
        
    def analyze_password_strength(self, password):
        """Comprehensive password strength analysis with strict criteria"""
        if not password:
            self.clear_analysis()
            return
            
        # Calculate strength score and get detailed analysis
        score, strength_level, analysis_data = self.calculate_strength_score(password)
        
        # Update strength display
        self.update_strength_display(strength_level, score, analysis_data)
        
        # Update detailed analysis
        self.update_detailed_analysis(password, analysis_data, score)

    def calculate_strength_score(self, password):
        """Calculate password strength with strict security criteria"""
        score = 0
        analysis = {
            'length': len(password),
            'has_lower': bool(re.search(r'[a-z]', password)),
            'has_upper': bool(re.search(r'[A-Z]', password)),
            'has_digits': bool(re.search(r'[0-9]', password)),
            'has_symbols': bool(re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password)),
            'has_spaces': ' ' in password,
            'repeated_chars': self.check_repeated_characters(password),
            'sequential': self.check_sequential_patterns(password),
            'common_patterns': self.check_common_patterns(password),
            'dictionary_words': self.check_dictionary_words(password),
            'entropy': self.calculate_entropy(password),
            'crack_time': self.estimate_crack_time(password)
        }

        # STRICT scoring criteria (total 100 points)

        # Length (30 points max) - Very strict
        if analysis['length'] >= 16:
            score += 30
        elif analysis['length'] >= 12:
            score += 20
        elif analysis['length'] >= 8:
            score += 10
        else:
            score += 0  # Very short passwords get no points

        # Character variety (25 points max) - Must have all types for full points
        char_types = sum([analysis['has_lower'], analysis['has_upper'],
                         analysis['has_digits'], analysis['has_symbols']])
        if char_types == 4:
            score += 25
        elif char_types == 3:
            score += 15
        elif char_types == 2:
            score += 8
        else:
            score += 0

        # No repeated characters (15 points max)
        if analysis['repeated_chars'] == 0:
            score += 15
        elif analysis['repeated_chars'] <= 2:
            score += 8
        elif analysis['repeated_chars'] <= 4:
            score += 3

        # No sequential patterns (15 points max)
        if analysis['sequential'] == 0:
            score += 15
        elif analysis['sequential'] <= 1:
            score += 8
        elif analysis['sequential'] <= 2:
            score += 3

        # No common patterns (10 points max)
        if analysis['common_patterns'] == 0:
            score += 10
        elif analysis['common_patterns'] <= 1:
            score += 5

        # No dictionary words (5 points max)
        if analysis['dictionary_words'] == 0:
            score += 5

        # Determine strength level with VERY strict thresholds
        if score >= 95:
            strength_level = "Very Strong"
        elif score >= 85:
            strength_level = "Strong"
        elif score >= 70:
            strength_level = "Good"
        elif score >= 50:
            strength_level = "Fair"
        elif score >= 30:
            strength_level = "Weak"
        else:
            strength_level = "Very Weak"

        return score, strength_level, analysis

    def check_repeated_characters(self, password):
        """Count repeated character sequences"""
        repeated_count = 0
        for i in range(len(password) - 2):
            if password[i] == password[i+1] == password[i+2]:
                repeated_count += 1
        return repeated_count

    def check_sequential_patterns(self, password):
        """Check for sequential patterns (abc, 123, etc.)"""
        sequential_count = 0
        password_lower = password.lower()

        for i in range(len(password_lower) - 2):
            # Check for ascending sequences
            if (ord(password_lower[i+1]) == ord(password_lower[i]) + 1 and
                ord(password_lower[i+2]) == ord(password_lower[i]) + 2):
                sequential_count += 1
            # Check for descending sequences
            elif (ord(password_lower[i+1]) == ord(password_lower[i]) - 1 and
                  ord(password_lower[i+2]) == ord(password_lower[i]) - 2):
                sequential_count += 1

        return sequential_count

    def check_common_patterns(self, password):
        """Check for common password patterns"""
        common_patterns = [
            r'password', r'123456', r'qwerty', r'admin', r'login',
            r'welcome', r'monkey', r'dragon', r'master', r'shadow',
            r'abc123', r'111111', r'000000', r'letmein', r'trustno1'
        ]

        pattern_count = 0
        password_lower = password.lower()

        for pattern in common_patterns:
            if re.search(pattern, password_lower):
                pattern_count += 1

        return pattern_count

    def check_dictionary_words(self, password):
        """Check for common dictionary words"""
        common_words = [
            'password', 'admin', 'user', 'login', 'welcome', 'hello',
            'world', 'computer', 'internet', 'security', 'system',
            'access', 'account', 'service', 'network', 'server'
        ]

        word_count = 0
        password_lower = password.lower()

        for word in common_words:
            if word in password_lower:
                word_count += 1

        return word_count

    def calculate_entropy(self, password):
        """Calculate password entropy"""
        charset_size = 0

        if re.search(r'[a-z]', password):
            charset_size += 26
        if re.search(r'[A-Z]', password):
            charset_size += 26
        if re.search(r'[0-9]', password):
            charset_size += 10
        if re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password):
            charset_size += 32
        if ' ' in password:
            charset_size += 1

        if charset_size == 0:
            return 0

        entropy = len(password) * math.log2(charset_size)
        return round(entropy, 2)

    def estimate_crack_time(self, password):
        """Estimate time to crack password"""
        entropy = self.calculate_entropy(password)

        # Assume 1 billion guesses per second
        guesses_per_second = 1_000_000_000
        total_combinations = 2 ** entropy
        seconds_to_crack = total_combinations / (2 * guesses_per_second)  # Average case

        if seconds_to_crack < 1:
            return "Instantly"
        elif seconds_to_crack < 60:
            return f"{int(seconds_to_crack)} seconds"
        elif seconds_to_crack < 3600:
            return f"{int(seconds_to_crack / 60)} minutes"
        elif seconds_to_crack < 86400:
            return f"{int(seconds_to_crack / 3600)} hours"
        elif seconds_to_crack < 31536000:
            return f"{int(seconds_to_crack / 86400)} days"
        elif seconds_to_crack < 31536000000:
            return f"{int(seconds_to_crack / 31536000)} years"
        else:
            return "Centuries"

    def update_strength_display(self, strength_level, score, analysis_data):
        """Update the strength display section"""
        # Color mapping for strength levels
        strength_colors = {
            "Very Weak": self.colors['very_weak'],
            "Weak": self.colors['weak'],
            "Fair": self.colors['fair'],
            "Good": self.colors['good'],
            "Strong": self.colors['strong'],
            "Very Strong": self.colors['very_strong']
        }

        color = strength_colors.get(strength_level, '#666666')

        # Update strength level text
        self.strength_level.config(text=f"🔒 {strength_level}", fg=color)

        # Update score
        self.score_display.config(text=f"Security Score: {score}/100 points")

        # Update strength bar
        self.strength_bar.place_forget()
        self.strength_bar.configure(bg=color)
        width_percent = score / 100
        self.strength_bar.place(relwidth=width_percent, relheight=1)

        # Update crack time
        self.crack_time.config(text=f"⏱️ Estimated crack time: {analysis_data['crack_time']}")

        # Update quick summary with key findings
        char_types = sum([analysis_data['has_lower'], analysis_data['has_upper'],
                         analysis_data['has_digits'], analysis_data['has_symbols']])

        summary_parts = []
        summary_parts.append(f"Length: {analysis_data['length']} chars")
        summary_parts.append(f"Character types: {char_types}/4")

        if analysis_data['repeated_chars'] > 0:
            summary_parts.append(f"⚠️ {analysis_data['repeated_chars']} repeated sequences")
        if analysis_data['sequential'] > 0:
            summary_parts.append(f"⚠️ {analysis_data['sequential']} sequential patterns")
        if analysis_data['common_patterns'] > 0:
            summary_parts.append(f"❌ {analysis_data['common_patterns']} common patterns")
        if analysis_data['dictionary_words'] > 0:
            summary_parts.append(f"❌ {analysis_data['dictionary_words']} dictionary words")

        if not any(['⚠️' in part or '❌' in part for part in summary_parts]):
            summary_parts.append("✅ No major security issues detected")

        summary_text = " • ".join(summary_parts)
        self.quick_summary.config(text=summary_text)

    def update_detailed_analysis(self, password, analysis_data, score):
        """Update the detailed analysis section"""
        self.analysis_text.config(state='normal')
        self.analysis_text.delete(1.0, tk.END)

        # Header
        analysis = f"🔍 COMPREHENSIVE PASSWORD SECURITY ANALYSIS\n"
        analysis += f"{'='*60}\n\n"

        # Basic info
        analysis += f"📊 Password: {'*' * len(password)} (hidden for security)\n"
        analysis += f"📏 Length: {analysis_data['length']} characters\n"
        analysis += f"🎯 Overall Security Score: {score}/100 points\n"
        analysis += f"⏱️ Estimated Crack Time: {analysis_data['crack_time']}\n"
        analysis += f"🔢 Mathematical Entropy: {analysis_data['entropy']} bits\n\n"

        # WHY this score - Detailed scoring breakdown
        analysis += f"📈 SCORING BREAKDOWN (Why this score?):\n"
        analysis += f"{'─'*40}\n"

        # Length scoring explanation
        length_score = 0
        if analysis_data['length'] >= 16:
            length_score = 30
            analysis += f"✅ Length Score: 30/30 - Excellent length (16+ characters)\n"
        elif analysis_data['length'] >= 12:
            length_score = 20
            analysis += f"✅ Length Score: 20/30 - Good length (12+ characters)\n"
        elif analysis_data['length'] >= 8:
            length_score = 10
            analysis += f"⚠️ Length Score: 10/30 - Adequate length (8+ characters)\n"
        else:
            length_score = 0
            analysis += f"❌ Length Score: 0/30 - Too short (less than 8 characters)\n"

        # Character variety scoring explanation
        char_types = sum([analysis_data['has_lower'], analysis_data['has_upper'],
                         analysis_data['has_digits'], analysis_data['has_symbols']])
        char_score = 0
        if char_types == 4:
            char_score = 25
            analysis += f"✅ Character Variety: 25/25 - All 4 types (excellent)\n"
        elif char_types == 3:
            char_score = 15
            analysis += f"✅ Character Variety: 15/25 - 3 types (good)\n"
        elif char_types == 2:
            char_score = 8
            analysis += f"⚠️ Character Variety: 8/25 - Only 2 types (limited)\n"
        else:
            char_score = 0
            analysis += f"❌ Character Variety: 0/25 - Only 1 type (poor)\n"

        # Pattern scoring explanation
        repeat_score = 0
        if analysis_data['repeated_chars'] == 0:
            repeat_score = 15
            analysis += f"✅ Repeated Characters: 15/15 - No repetitions found\n"
        elif analysis_data['repeated_chars'] <= 2:
            repeat_score = 8
            analysis += f"⚠️ Repeated Characters: 8/15 - Some repetitions ({analysis_data['repeated_chars']})\n"
        else:
            repeat_score = 3
            analysis += f"❌ Repeated Characters: 3/15 - Many repetitions ({analysis_data['repeated_chars']})\n"

        seq_score = 0
        if analysis_data['sequential'] == 0:
            seq_score = 15
            analysis += f"✅ Sequential Patterns: 15/15 - No sequences found\n"
        elif analysis_data['sequential'] <= 1:
            seq_score = 8
            analysis += f"⚠️ Sequential Patterns: 8/15 - Some sequences ({analysis_data['sequential']})\n"
        else:
            seq_score = 3
            analysis += f"❌ Sequential Patterns: 3/15 - Many sequences ({analysis_data['sequential']})\n"

        pattern_score = 0
        if analysis_data['common_patterns'] == 0:
            pattern_score = 10
            analysis += f"✅ Common Patterns: 10/10 - No common patterns\n"
        else:
            pattern_score = 5 if analysis_data['common_patterns'] <= 1 else 0
            analysis += f"❌ Common Patterns: {pattern_score}/10 - Found {analysis_data['common_patterns']} patterns\n"

        dict_score = 0
        if analysis_data['dictionary_words'] == 0:
            dict_score = 5
            analysis += f"✅ Dictionary Words: 5/5 - No dictionary words\n"
        else:
            analysis += f"❌ Dictionary Words: 0/5 - Found {analysis_data['dictionary_words']} words\n"

        total_calculated = length_score + char_score + repeat_score + seq_score + pattern_score + dict_score
        analysis += f"\n📊 Total Calculated Score: {total_calculated}/100\n\n"

        # Character composition with detailed counts
        analysis += f"🔤 DETAILED CHARACTER COMPOSITION:\n"
        analysis += f"{'─'*40}\n"

        lower_count = sum(1 for c in password if c.islower())
        upper_count = sum(1 for c in password if c.isupper())
        digit_count = sum(1 for c in password if c.isdigit())
        symbol_count = sum(1 for c in password if c in string.punctuation)
        space_count = password.count(' ')

        analysis += f"{'✅' if analysis_data['has_lower'] else '❌'} Lowercase letters: {lower_count} characters\n"
        analysis += f"{'✅' if analysis_data['has_upper'] else '❌'} Uppercase letters: {upper_count} characters\n"
        analysis += f"{'✅' if analysis_data['has_digits'] else '❌'} Numbers: {digit_count} characters\n"
        analysis += f"{'✅' if analysis_data['has_symbols'] else '❌'} Special symbols: {symbol_count} characters\n"
        analysis += f"{'✅' if space_count == 0 else '⚠️'} Spaces: {space_count} characters\n"

        # Character distribution analysis
        total_chars = len(password)
        if total_chars > 0:
            analysis += f"\n📊 Character Distribution:\n"
            if lower_count > 0:
                analysis += f"   • Lowercase: {lower_count}/{total_chars} ({lower_count/total_chars*100:.1f}%)\n"
            if upper_count > 0:
                analysis += f"   • Uppercase: {upper_count}/{total_chars} ({upper_count/total_chars*100:.1f}%)\n"
            if digit_count > 0:
                analysis += f"   • Numbers: {digit_count}/{total_chars} ({digit_count/total_chars*100:.1f}%)\n"
            if symbol_count > 0:
                analysis += f"   • Symbols: {symbol_count}/{total_chars} ({symbol_count/total_chars*100:.1f}%)\n"
        analysis += f"\n"

        # Detailed security vulnerability analysis
        analysis += f"🛡️ SECURITY VULNERABILITY ANALYSIS:\n"
        analysis += f"{'─'*45}\n"

        # Length vulnerability
        if analysis_data['length'] >= 16:
            analysis += f"✅ LENGTH SECURITY: Excellent protection against brute force\n"
            analysis += f"   → 16+ characters provide exponential security increase\n"
        elif analysis_data['length'] >= 12:
            analysis += f"✅ LENGTH SECURITY: Good protection against most attacks\n"
            analysis += f"   → 12+ characters are generally secure for most use cases\n"
        elif analysis_data['length'] >= 8:
            analysis += f"⚠️ LENGTH SECURITY: Minimum acceptable length\n"
            analysis += f"   → Consider increasing to 12+ characters for better security\n"
        else:
            analysis += f"❌ LENGTH SECURITY: CRITICAL VULNERABILITY\n"
            analysis += f"   → Passwords under 8 characters are easily cracked\n"

        # Character variety vulnerability
        char_types = sum([analysis_data['has_lower'], analysis_data['has_upper'],
                         analysis_data['has_digits'], analysis_data['has_symbols']])
        if char_types == 4:
            analysis += f"✅ CHARACTER SECURITY: Maximum character space utilized\n"
            analysis += f"   → Using all 4 character types maximizes entropy\n"
        elif char_types == 3:
            analysis += f"✅ CHARACTER SECURITY: Good character diversity\n"
            analysis += f"   → Missing {'symbols' if not analysis_data['has_symbols'] else 'uppercase' if not analysis_data['has_upper'] else 'digits'} reduces search space\n"
        elif char_types == 2:
            analysis += f"⚠️ CHARACTER SECURITY: Limited character diversity\n"
            analysis += f"   → Attackers can focus on smaller character sets\n"
        else:
            analysis += f"❌ CHARACTER SECURITY: MAJOR VULNERABILITY\n"
            analysis += f"   → Single character type is extremely predictable\n"

        # Pattern vulnerability analysis
        if analysis_data['repeated_chars'] == 0:
            analysis += f"✅ PATTERN SECURITY: No character repetition detected\n"
        else:
            analysis += f"⚠️ PATTERN SECURITY: Repeated sequences found\n"
            analysis += f"   → {analysis_data['repeated_chars']} sequences make password more predictable\n"

        if analysis_data['sequential'] == 0:
            analysis += f"✅ SEQUENCE SECURITY: No sequential patterns detected\n"
        else:
            analysis += f"⚠️ SEQUENCE SECURITY: Sequential patterns found\n"
            analysis += f"   → {analysis_data['sequential']} sequences (abc, 123) are easily guessed\n"

        if analysis_data['common_patterns'] == 0:
            analysis += f"✅ PATTERN SECURITY: No common password patterns\n"
        else:
            analysis += f"❌ PATTERN SECURITY: MAJOR VULNERABILITY\n"
            analysis += f"   → {analysis_data['common_patterns']} common patterns found (password, 123456, etc.)\n"

        if analysis_data['dictionary_words'] == 0:
            analysis += f"✅ DICTIONARY SECURITY: No common words detected\n"
        else:
            analysis += f"❌ DICTIONARY SECURITY: VULNERABILITY DETECTED\n"
            analysis += f"   → {analysis_data['dictionary_words']} dictionary words make it vulnerable to attacks\n"

        # Specific, actionable recommendations
        analysis += f"\n💡 SPECIFIC IMPROVEMENT RECOMMENDATIONS:\n"
        analysis += f"{'─'*50}\n"

        if score < 30:
            analysis += f"🚨 CRITICAL SECURITY ALERT: Immediate action required!\n\n"
            analysis += f"PRIORITY 1 - Length:\n"
            if analysis_data['length'] < 8:
                analysis += f"   → Increase length to at least 12 characters (currently {analysis_data['length']})\n"
            analysis += f"PRIORITY 2 - Character Types:\n"
            if not analysis_data['has_upper']:
                analysis += f"   → Add uppercase letters (A-Z)\n"
            if not analysis_data['has_digits']:
                analysis += f"   → Add numbers (0-9)\n"
            if not analysis_data['has_symbols']:
                analysis += f"   → Add special symbols (!@#$%^&*)\n"
            analysis += f"PRIORITY 3 - Avoid Predictable Patterns:\n"
            analysis += f"   → Don't use common words, dates, or keyboard patterns\n"

        elif score < 50:
            analysis += f"🔴 HIGH PRIORITY: This password needs major improvements\n\n"
            specific_issues = []
            if analysis_data['length'] < 12:
                specific_issues.append(f"Increase length from {analysis_data['length']} to 12+ characters")
            if char_types < 3:
                missing = []
                if not analysis_data['has_upper']: missing.append("uppercase")
                if not analysis_data['has_digits']: missing.append("numbers")
                if not analysis_data['has_symbols']: missing.append("symbols")
                specific_issues.append(f"Add {', '.join(missing)} characters")
            if analysis_data['common_patterns'] > 0:
                specific_issues.append("Remove common password patterns")
            if analysis_data['dictionary_words'] > 0:
                specific_issues.append("Replace dictionary words with random characters")

            for i, issue in enumerate(specific_issues, 1):
                analysis += f"   {i}. {issue}\n"

        elif score < 70:
            analysis += f"🟡 MODERATE PRIORITY: Good foundation, needs refinement\n\n"
            improvements = []
            if analysis_data['length'] < 16:
                improvements.append(f"Consider increasing length to 16+ characters (currently {analysis_data['length']})")
            if char_types < 4:
                missing = []
                if not analysis_data['has_symbols']: missing.append("symbols")
                if not analysis_data['has_upper']: missing.append("uppercase")
                if missing:
                    improvements.append(f"Add {', '.join(missing)} for maximum security")
            if analysis_data['repeated_chars'] > 0:
                improvements.append("Reduce character repetition")
            if analysis_data['sequential'] > 0:
                improvements.append("Avoid sequential patterns (abc, 123)")

            for i, improvement in enumerate(improvements, 1):
                analysis += f"   {i}. {improvement}\n"

        elif score < 85:
            analysis += f"🟢 LOW PRIORITY: Strong password with minor optimizations\n\n"
            optimizations = []
            if analysis_data['length'] < 20:
                optimizations.append("Consider extending to 20+ characters for maximum security")
            if analysis_data['repeated_chars'] > 0 or analysis_data['sequential'] > 0:
                optimizations.append("Fine-tune to eliminate any remaining patterns")
            optimizations.append("Ensure this password is unique across all accounts")

            for i, opt in enumerate(optimizations, 1):
                analysis += f"   {i}. {opt}\n"

        else:
            analysis += f"🔵 EXCELLENT: Outstanding password security!\n\n"
            analysis += f"✅ This password meets all security best practices\n"
            analysis += f"✅ Excellent protection against all common attack methods\n"
            analysis += f"✅ Suitable for high-security applications\n\n"
            analysis += f"Maintenance recommendations:\n"
            analysis += f"   • Keep this password confidential\n"
            analysis += f"   • Use unique passwords for each account\n"
            analysis += f"   • Store securely (password manager recommended)\n"
            analysis += f"   • Monitor for any security breaches\n"

        # Security tips
        analysis += f"\n🔐 GENERAL SECURITY TIPS:\n"
        analysis += f"{'─'*30}\n"
        analysis += f"• Never reuse passwords across multiple accounts\n"
        analysis += f"• Enable two-factor authentication when available\n"
        analysis += f"• Use a reputable password manager\n"
        analysis += f"• Change passwords if you suspect compromise\n"
        analysis += f"• Avoid passwords based on personal information\n"

        self.analysis_text.insert(tk.END, analysis)
        self.analysis_text.config(state='disabled')


def main():
    root = tk.Tk()
    app = PasswordAnalyzerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
