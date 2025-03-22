import os
import shutil
import subprocess
import requests
import requests, os, sys, uuid, hashlib, time
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
import os
import time
import uuid
import hashlib
import requests
import sys
from datetime import datetime
from rich.console import Console
from rich.panel import Panel

console = Console()

# ✅ GitHub Key Storage (RAW Link)
GITHUB_KEYS_URL = "https://raw.githubusercontent.com/Ubermanue/keye/main/key.txt"
REVOKED_KEYS_URL = "https://raw.githubusercontent.com/Ubermanue/keye/main/revoked.txt"
LOCAL_KEY_FILE = "key.txt"

# 💰 Subscription Prices
PRICING = {
    "LIFETIME": "₱50",
    "1-MONTH": "₱45",
    "RENT": "₱25",
    "TRIAL (2 Days)": "₱5"
}

# 🛡️ Generate HWID-Based Permanent Key
def generate_permanent_key():
    """Generates a permanent device key based on HWID."""
    if os.path.exists(LOCAL_KEY_FILE):
        with open(LOCAL_KEY_FILE, "r") as f:
            stored_key = f.read().strip()
            if stored_key:
                return stored_key  

    hwid = hashlib.sha256(str(uuid.getnode()).encode()).hexdigest()[:16]  
    key = f"BOOST-{hwid.upper()}"

    with open(LOCAL_KEY_FILE, "w") as f:
        f.write(key)

    return key

# 🛑 Check if Key is Revoked
def is_key_revoked(key):
    try:
        response = requests.get(REVOKED_KEYS_URL, timeout=5)
        if response.status_code == 200:
            revoked_keys = response.text.splitlines()
            if key in revoked_keys:
                return True
    except:
        return False  
    return False

# 🔑 Check Key Approval
def approval():
    """Checks if the stored/generated key is approved."""
    user_key = generate_permanent_key()

    console.print(Panel(f"[cyan]🔑 Your Boosting Key:[/cyan] [bold yellow]{user_key}[/bold yellow]",
                        title="[bold white]🔹 JHON & KYZIN BOOST 🔹[/bold white]", style="blue"))

    # 💰 Show Pricing
    pricing_text = "\n".join([f"💰 {plan}: {price}" for plan, price in PRICING.items()])
    console.print(Panel(f"[bold magenta]Subscription Prices:[/bold magenta]\n\n{pricing_text}\n\n"
                        "📩 Facebook: [cyan]https://www.facebook.com/kyzinnot[/cyan]\n"
                        "👑 Owner: Kyzin & Jhon",
                        style="red", title="[bold yellow]💸 Subscription Plans 💸[/bold yellow]"))

    try:
        # ✅ Fetch Approved Keys
        response = requests.get(GITHUB_KEYS_URL, timeout=5)
        if response.status_code != 200:
            raise Exception("❌ Failed to fetch approval list.")

        approved_keys = response.text.splitlines()

        # 🛑 Check if Key is Revoked
        if is_key_revoked(user_key):
            console.print(Panel("[red]❌ Key Revoked! Contact support.[/red]", style="red"))
            os.remove(LOCAL_KEY_FILE)  
            sys.exit(1)

        # 🔍 Validate Key
        if user_key in approved_keys:
            console.print(Panel(f"[green]✅ Key Approved! Boosting Started![/green]", style="cyan"))
            time.sleep(1)
        else:
            console.print(Panel("[red]🚫 Key Not Approved! Contact Jhon & Kyzin.[/red]", style="red"))
            input("[yellow]Press Enter To Request Approval[/yellow]")
            os.system(f"xdg-open https://www.facebook.com/kyzinnot?message=Hello%20Sir!%20Please%20Approve%20My%20Boosting%20Key:%20{user_key}")
            sys.exit(1)
    except Exception as e:
        console.print(Panel(f"[red]⚠ Error: {e}[/red]", style="red"))
        sys.exit(1)

# 🚀 Start Tool
approval()
console.print("\n[bold green]🚀 Boosting Started... Let's Win![/bold green]\n")
# ORIGINAL CODE STARTS BELOW
import os, sys, time, random
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn

console = Console()

# 🔊 Cross-Platform Beep Sound
def beep():
    try:
        os.system("echo -e '\a'")  # Works on Linux/Android
    except:
        pass  # Ignore errors

# ⚠ Flashing Warning Screen
def flashing_warning():
    for _ in range(3):
        console.clear()
        time.sleep(0.2)
        console.print(Panel("[bold red]⚠ WARNING! Unauthorized Use Detected! ⚠[/bold red]", style="red", title="[bold white]SYSTEM ALERT[/bold white]"))
        time.sleep(0.2)

# 🟢 Matrix-Style Glitch Effect
def matrix_effect():
    console.clear()
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    
    for _ in range(10):  # Adjust for longer effect
        matrix_text = "".join(random.choice(chars) for _ in range(50))
        console.print(f"[bold green]{matrix_text}[/bold green]", end="\r")
        time.sleep(0.1)

# 🔄 Loading Bar Effect
def loading_bar():
    with Progress(
        TextColumn("[cyan]🚀 Boosting System Initializing...[/cyan]"),
        BarColumn(bar_width=None),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task("Loading...", total=100)
        for i in range(100):
            time.sleep(0.03)  # Adjust speed
            progress.update(task, advance=1)

# 🔥 High-Tech Logo
logo = f"""
╔══════════════════════════════════════════╗
║                                          ║
║    🚀  JHON BOOST 101  - v1.8  🚀       ║
║                                          ║
╠══════════════════════════════════════════╣
║  ⚡ Developer: Kyzin                        ║
║  ⚡ Features: Boosting, Automation         ║
║  ⚡ Version: 1.8                           ║
║  ⚡ Status: Active ✅                     ║
║  ⚡ Facebook: Kyzin                        ║
╠══════════════════════════════════════════╣
║  ⚠ Warning: Unauthorized use is prohibited! 💀  ║
╚══════════════════════════════════════════╝
"""

# 🔥 Run High-Tech Intro
beep()
flashing_warning()
matrix_effect()
loading_bar()
console.print(logo)
beep()

red = "\033[1;31m"    
c = "\033[1;96m"      
g = "\033[1;34m"      
r = "\033[0m"         
wh = "\033[1;37m"     

def clear_screen():
    os.system('clear')

def count_lines(file_path):
    try:
        with open(file_path, 'r') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        return 0  # Return 0 if the file does not exist

def overview():
    print(logo)  # Print the logo
    print("\033[1;34m┌──────────────────────DASHBOARD──────────────────────┐")
    total_accounts = count_lines("/sdcard/Test/toka.txt")
    total_pages = count_lines("/sdcard/Test/tokp.txt")
    print(f"│ 📂 Total Accounts: {total_accounts} │ 📑 Total Pages: {total_pages} │")
    print("└────────────────────────────────────────────────────┘\033[0m")  # Closing box

def git_pull_repository():
    repo_path = '.'  
    try:
        print(f"{c}Updating the repository...{r}")
        subprocess.run(['git', 'pull'], cwd=repo_path, check=True)
        print(f"{wh}Repository updated successfully.{r}")
    except subprocess.CalledProcessError as e:
        print(f"{red}Error occurred while updating the repository: {e}{r}")

def clone_and_run(repo_url, script_name):
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    
    if not os.path.exists(repo_name):
        os.system(f'git clone {repo_url}')
    
    os.chdir(repo_name)
    os.system(f'python {script_name}')
    os.chdir('..')

def main_menu():
    clear_screen()
    overview()  

    print("┌────────────────────────────────────────────────────────┐")
    print("│                   MENU TOOL                            │")
    print("├───────────────────────────┬───────────────────────────┤")
    print("│ [0]  Update Tool          │ [9]  Auto Reacts for Reels│")
    print("│ [1]  Extract Account      │ [10] Auto Join Groups    │")
    print("│ [2]  Auto FB Followers    │ [11] Auto Comments Reels │")
    print("│ [3]  Auto Comments        │ [12] Auto Comments Vids  │")
    print("│ [4]  Auto Reply Comments  │ [13] Spam Shares         │")
    print("│ [5]  Auto Reacts          │ [14] Bundle Reactions    │")
    print("│ [6]  Auto Create Page     │ [15] Auto Comment P&V    │")
    print("│ [7]  Auto React Comment   │ [16] Guard On            │")
    print("│ [8]  Auto Reacts Videos   │ [ARD] Auto Remove Dead   │")
    print("│ [RDP] Remove Duplicates   │ [R]   Reset              │")
    print("│ [E]   Exit                │                           │")
    print("└───────────────────────────┴───────────────────────────┘")
    choice = input("Enter your choice: ").strip().upper()

    if choice == '0':
        update()  
    elif choice == '1':
        extract_account()
    elif choice == '2':
        auto_facebook_followers()
    elif choice == '3':
        auto_comments()
    elif choice == '4':
        auto_reply_to_comments()
    elif choice == '5':
        auto_reacts()
    elif choice == '6':
        auto_create_page()
    elif choice == '7':
        auto_react_comment()
    elif choice == '8':
        auto_working_vid()
    elif choice == '9':
        auto_reacts_reels()
    elif choice == '10':
        auto_join_groups()
    elif choice == '11':
        auto_comments_reels()
    elif choice == '12':
        auto_comments_vids()
    elif choice == '13':
        spam_share()
    elif choice == '14':
        bundle_reacts()
    elif choice == '15':
        easy_comments()
    elif choice == '16':
     	guard_on()
    elif choice == 'C':
        acc_checker()
    elif choice == 'RDP':
        dupli_remover()
    elif choice == 'R':
        reset()
    elif choice == 'E':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice, please try again.")
        main_menu()

def update():
    # Paths to the local repositories
    main_repo_path = '.'  # Assuming the script is in the main repo directory
    boosting_repo_path = './BOOSTING'  # Path to the local BOOSTING repository

    # Update the main repository
    try:
        print(f"{c}Updating the main repository...{r}")
        subprocess.run(['git', 'pull'], cwd=main_repo_path, check=True)
        print(f"{wh}Main repository updated successfully.{r}")
    except subprocess.CalledProcessError as e:
        print(f"{red}Error occurred while updating the main repository: {e}{r}")

    # Check if the BOOSTING repo exists locally
    if not os.path.exists(boosting_repo_path):
        print(f"{red}BOOSTING repository not found locally. Please clone it first.{r}")
        return  # Exit if the repository is not found

    # Update the BOOSTING repository
    try:
        print(f"{c}Pulling the latest changes from the BOOSTING repository...{r}")
        subprocess.run(['git', 'pull'], cwd=boosting_repo_path, check=True)
        print(f"{wh}BOOSTING repository updated successfully.{r}")
    except subprocess.CalledProcessError as e:
        print(f"{red}Error occurred while updating the BOOSTING repository: {e}{r}")
              
def extract_account():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'extract-acc.py'
    clone_and_run(repo_url, script_name)

def auto_facebook_followers():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'auto-follow.py'
    clone_and_run(repo_url, script_name)

def auto_comments():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'auto_comment.py'
    clone_and_run(repo_url, script_name)

def auto_reply_to_comments():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'atrc.py'
    clone_and_run(repo_url, script_name)

def auto_reacts():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'auto-reacts.py'
    clone_and_run(repo_url, script_name)

def auto_create_page():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'atc_page.py'
    clone_and_run(repo_url, script_name)

def auto_react_comment():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'auto-react-comment.py'
    clone_and_run(repo_url, script_name)

def auto_working_vid():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'working-vid.py'
    clone_and_run(repo_url, script_name)

def auto_reacts_reels():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'reels_reacts.py'
    clone_and_run(repo_url, script_name)

def auto_join_groups():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'join_group.py'
    clone_and_run(repo_url, script_name)

def auto_comments_reels():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'reels_comments.py'
    clone_and_run(repo_url, script_name)

def auto_comments_vids():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'video_comments.py'
    clone_and_run(repo_url, script_name)

def spam_share():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'spam_share.py'
    clone_and_run(repo_url, script_name)
    
def bundle_reacts():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'bundle_reacts.py'
    clone_and_run(repo_url, script_name)

def easy_comments():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'easy_comments.py'
    clone_and_run(repo_url, script_name)

def acc_checker():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'acc_checker.py'
    clone_and_run(repo_url, script_name)
    
def dupli_remover():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'dupli_remover.py'
    clone_and_run(repo_url, script_name)
    
def guard_on():
	repo_url ='https://github.com/KYZER02435/BOOSTING'
	script_name = 'guard_on.py'
	clone_and_run(repo_url, script_name)

def reset():
    folder_path = '/sdcard/Test'
    
    # Check if the folder exists
    if os.path.exists(folder_path):
        try:
            # Delete the folder and all its contents
            shutil.rmtree(folder_path)
            print(f"Successfully deleted the folder: {folder_path}")
        except Exception as e:
            print(f"Error while deleting the folder: {e}")
    else:
        print(f"The folder {folder_path} does not exist.") 

if __name__ == "__main__":
    main_menu()
