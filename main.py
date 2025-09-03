#!/usr/bin/env python3
"""
Password Generator - Main Launcher
Choose between command-line interface or graphical interface
"""

import sys
import os

def show_menu():
    print("🔍 Password Strength Analyzer")
    print("=" * 40)
    print("Choose your interface:")
    print("1. 🖥️  Modern GUI Analyzer")
    print("2. 💻 Classic Command Line Generator")
    print("3. ❌ Exit")
    print("=" * 40)

def launch_analyzer():
    try:
        from password_analyzer import main as analyzer_main
        print("Launching Password Analyzer...")
        analyzer_main()
    except ImportError as e:
        print(f"Error: Could not import analyzer module: {e}")
        print("Make sure password_analyzer.py is in the same directory.")
    except Exception as e:
        print(f"Error launching analyzer: {e}")

def launch_cli():
    try:
        # Import and run the original CLI version
        import password_generator
        print("CLI version completed.")
    except ImportError as e:
        print(f"Error: Could not import CLI module: {e}")
        print("Make sure password_generator.py is in the same directory.")
    except Exception as e:
        print(f"Error launching CLI: {e}")

def main():
    while True:
        show_menu()
        try:
            choice = input("Enter your choice (1-3): ").strip()

            if choice == "1":
                launch_analyzer()
                break
            elif choice == "2":
                launch_cli()
                # After CLI completes, show menu again
                input("\nPress Enter to return to menu...")
                continue
            elif choice == "3":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please enter 1, 2, or 3.")
                input("Press Enter to continue...")

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
