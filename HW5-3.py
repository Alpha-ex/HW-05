import os
import sys
from colorama import Fore, Style, init

# Ініціалізація colorama для кольорового виведення
init(autoreset=True)

def display_directory_structure(path, indent=0):
    try:
        items = os.listdir(path)
    except FileNotFoundError:
        print(Fore.RED + f"Директорії {path} не існує.")
        return
    except PermissionError:
        print(Fore.RED + f"Немає прав доступу до директорії {path}.")
        return

    for item in items:
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            print(Fore.BLUE + Style.BRIGHT + "  " * indent + f"📁 {item}")
            display_directory_structure(full_path, indent + 1)
        else:
            print(Fore.GREEN + Style.BRIGHT + "  " * indent + f"📄 {item}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python script.py <шлях_до_директорії>")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print(Fore.RED + f"{directory_path} не існує або не є директорією.")
        sys.exit(1)

    print(Fore.CYAN + Style.BRIGHT + f"Візуалізація структури директорії {directory_path}:\n")
    display_directory_structure(directory_path)