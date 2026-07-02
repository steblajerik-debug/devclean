#!/usr/bin/env python3
import os
import sys
import shutil
import ctypes
import time
from pathlib import Path

# Fix terminal colors for Windows Command Prompt / PowerShell
if sys.platform == "win32":
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# ANSI styles & colors for a gorgeous terminal look
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
CYAN = "\033[96m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

JUNK_TARGETS = {
    "node_modules": "Node.js Modules",
    "__pycache__": "Python Cache",
    ".pytest_cache": "Pytest Cache",
    "target": "Rust Build Artifacts",
    "bin": "Compiled Binaries",
    "obj": "C# Build Objects",
    ".vs": "Visual Studio Config"
}

def get_dir_size(path: Path) -> int:
    total = 0
    try:
        for entry in os.scandir(path):
            if entry.is_file(follow_symlinks=False):
                total += entry.stat().st_size
            elif entry.is_dir(follow_symlinks=False):
                total += get_dir_size(Path(entry.path))
    except PermissionError:
        pass
    return total

def format_size(bytes_size: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024
    return f"{bytes_size:.2f} TB"

def draw_header():
    print(f"{BLUE}┌────────────────────────────────────────────────────────┐{RESET}")
    print(f"{BLUE}│{RESET}  {BOLD}{CYAN}🚀 DEVCLEAN v1.1{RESET}                                      {BLUE}│{RESET}")
    print(f"{BLUE}│{RESET}  {DIM}The ultimate cross-platform developer bloat cleaner{RESET}   {BLUE}│{RESET}")
    print(f"{BLUE}└────────────────────────────────────────────────────────┘{RESET}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_header()
    
    scan_dir = Path.cwd()
    print(f"\n📂 {BOLD}Target Workspace:{RESET} {YELLOW}{scan_dir}{RESET}")
    print(f"{DIM}🔍 Scanning for build caches and junk directories...{RESET}\n")
    
    found_junk = []
    total_wasted = 0
    spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    idx = 0

    for root, dirs, _ in os.walk(scan_dir):
        for d in list(dirs):
            if d in JUNK_TARGETS:
                junk_path = Path(root) / d
                
                # Visual live-spinner animation while calculation happens
                print(f"  {CYAN}{spinner[idx % len(spinner)]}{RESET} Analyzing: {DIM}...{junk_path.name}{RESET}", end="\r")
                idx += 1
                
                size = get_dir_size(junk_path)
                total_wasted += size
                found_junk.append((junk_path, size))
                dirs.remove(d) 

    print(" " * 80, end="\r")  # Clear scanner animation line

    if not found_junk:
        print(f"✨ {GREEN}{BOLD}Your workspace is sparkling clean!{RESET} No developer junk found.")
        return

    # Visual Table Layout for Data
    print(f"{BOLD}┌──────────────────────────────────────────────┬──────────────┐{RESET}")
    print(f"{BOLD}│ Detected Bloat Folder                        │ Space Wasted │{RESET}")
    print(f"{BOLD}├──────────────────────────────────────────────┼──────────────┤{RESET}")
    
    for path, size in found_junk:
        try:
            display_name = str(path.relative_to(scan_dir))
        except ValueError:
            display_name = str(path)
            
        # Truncate string if it's too long for the table column
        if len(display_name) > 42:
            display_name = "..." + display_name[-39:]
            
        space_str = format_size(size)
        print(f"│ {YELLOW}{display_name:<44}{RESET} │ {RED}{space_str:>12}{RESET} │")
        
    print(f"{BOLD}└──────────────────────────────────────────────┴──────────────┘{RESET}")
    print(f"📊 {BOLD}Total Recoverable Space:{RESET} {GREEN}{BOLD}{format_size(total_wasted)}{RESET}\n")
    
    try:
        # Styled confirmation box
        confirm = input(f"⚠️  {BOLD}{YELLOW}Permanently purge these targets? (y/N):{RESET} ").strip().lower()
        if confirm == 'y':
            print(f"\n{BLUE}🧼 Purging targets...{RESET}")
            for path, _ in found_junk:
                try:
                    shutil.rmtree(path)
                    print(f"  {GREEN}✔{RESET} Successfully deleted {DIM}{path.name}{RESET}")
                except Exception as e:
                    print(f"  {RED}✘ Failed to delete {path.name}:{RESET} {e}")
            print(f"\n🎉 {GREEN}{BOLD}Done! Your drive thanks you.{RESET}\n")
        else:
            print(f"\n{YELLOW}❌ Operation cancelled. Files left intact.{RESET}\n")
    except (KeyboardInterrupt, EOFError):
        print(f"\n\n{RED}Process interrupted. Exiting safely.{RESET}\n")

if __name__ == "__main__":
    main()
