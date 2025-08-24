import os
import sys

# List of websites to block
BLOCKED_SITES = [
    "www.pornhub.com",
    "www.xvideos.com",
    "www.redtube.com",
    "www.4chan.org",
    "www.bet365.com",
    "www.gambling.com",
    "www.violence.com",
    "www.gore.com",
    "www.darkweb.com",
    "www.instagram.com",
    "www.facebook.com"

]

# Location of the hosts file (varies by OS)
HOSTS_PATH = "/etc/hosts" if os.name != "nt" else r"C:\Windows\System32\drivers\etc\hosts"
REDIRECT_IP = "127.0.0.1"  # Redirect to localhost to block

def is_admin():
    try:
        if os.name == "nt":
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin()
        else:
            return os.geteuid() == 0
    except:
        return False

def block_sites():
    try:
        with open(HOSTS_PATH, "r+") as file:
            content = file.read()
            for site in BLOCKED_SITES:
                entry = f"{REDIRECT_IP} {site}\n"
                if site not in content:
                    file.write(entry)
        print("✅ Sites blocked successfully.")
    except PermissionError:
        print("❌ Permission denied. Run this script as administrator.")
    except Exception as e:
        print(f"❌ Error: {e}")

def unblock_sites():
    try:
        with open(HOSTS_PATH, "r") as file:
            lines = file.readlines()
        with open(HOSTS_PATH, "w") as file:
            for line in lines:
                if not any(site in line for site in BLOCKED_SITES):
                    file.write(line)
        print("✅ Sites unblocked successfully.")
    except PermissionError:
        print("❌ Permission denied. Run this script as administrator.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if not is_admin():
        print("❗ Please run this script as administrator/root.")
        sys.exit()

    print("SafeSurf - Website Blocker")
    print("1. Block sites")
    print("2. Unblock sites")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        block_sites()
    elif choice == "2":
        unblock_sites()
    else:
        print("❌ Invalid option.")
