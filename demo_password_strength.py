#!/usr/bin/env python3
"""
Demo script to showcase the password strength evaluation feature
"""

from password_generator_gui import PasswordGeneratorGUI
import tkinter as tk

def demo_password_analysis():
    """Demonstrate password strength analysis with various examples"""
    
    # Create a temporary GUI instance to use the evaluation method
    root = tk.Tk()
    root.withdraw()  # Hide the window
    app = PasswordGeneratorGUI(root)
    
    # Test passwords with different strength levels
    test_passwords = [
        ("123", "Very weak - too short, only digits"),
        ("password", "Very weak - common word, no variety"),
        ("Password1", "Weak - common pattern, limited variety"),
        ("MyP@ssw0rd", "Fair - better variety but still predictable"),
        ("Tr0ub4dor&3", "Good - decent length and variety"),
        ("X9#mK2$vN8@qR5!wL7", "Strong - excellent length and variety"),
        ("correct horse battery staple", "Fair - long but predictable pattern"),
        ("C0rr3ct-H0rs3-B@tt3ry-St@pl3!", "Strong - long with good variety")
    ]
    
    print("🔍 Password Strength Analysis Demo")
    print("=" * 60)
    
    for password, description in test_passwords:
        strength, score, feedback = app.evaluate_password_strength(password)
        
        print(f"\nPassword: '{password}'")
        print(f"Description: {description}")
        print(f"Strength: {strength} (Score: {score}/100)")
        print("Analysis:")
        for item in feedback[:3]:  # Show first 3 feedback items
            print(f"  • {item}")
        if len(feedback) > 3:
            print(f"  ... and {len(feedback) - 3} more criteria")
        print("-" * 40)
    
    root.destroy()

if __name__ == "__main__":
    demo_password_analysis()
