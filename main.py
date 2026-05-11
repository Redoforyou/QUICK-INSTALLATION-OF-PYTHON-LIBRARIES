import subprocess
import sys
import os

class LinuxDevInstaller:
    def __init__(self):
        self.lang = 'ru'
        # Цвета для терминала
        self.CLR = "\033[94m"    # Blue
        self.OK  = "\033[92m"    # Green
        self.ERR = "\033[91m"    # Red
        self.CYAN = "\033[96m"   # Cyan
        self.END = "\033[0m"     # Reset

        # Твой стандартный набор библиотек
        self.core_libs = ["requests", "numpy", "pandas", "opencv-python", "flask", "pygame", "pillow"]
        
        self.texts = {
            'ru': {
                'title': "--- LINUX LIB INSTALLER ---",
                'm1': "1. Установить стандартный набор",
                'm2': "2. Поиск и установка по названию",
                'm3': "3. Сменить язык (RU)",
                'm4': "4. Выход",
                'ask': "Выберите пункт: ",
                'search_ask': "Введите название библиотеки: ",
                'installing': "Установка {}...",
                'done': "Готово!",
                'error': "Ошибка при установке ",
                'select_pkg': "Выберите вариант (0 - отмена): "
            },
            'en': {
                'title': "--- LINUX LIB INSTALLER ---",
                'm1': "1. Install core libraries",
                'm2': "2. Search and install by name",
                'm3': "3. Change language (EN)",
                'm4': "4. Exit",
                'ask': "Select option: ",
                'search_ask': "Enter library name: ",
                'installing': "Installing {}...",
                'done': "Done!",
                'error': "Error installing ",
                'select_pkg': "Select option (0 - cancel): "
            }
        }

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def install(self, name):
        t = self.texts[self.lang]
        print(f"\n{self.CYAN}{t['installing'].format(name)}{self.END}")
        
        try:
            # Флаг --break-system-packages позволяет ставить пакеты на Arch/CachyOS без venv
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", 
                name, "--break-system-packages"
            ])
            print(f"{self.OK}{t['done']}{self.END}")
        except Exception as e:
            print(f"{self.ERR}{t['error']} {name}{self.END}")
        
        input("\nPress Enter to continue...")

    def search_menu(self):
        t = self.texts[self.lang]
        name = input(f"{self.CLR}{t['search_ask']}{self.END}").strip()
        if not name: return

        # Предлагаем варианты названий
        options = [name, f"python-{name}", f"py{name}", f"{name}-tools"]
        
        print(f"\n{self.CLR}{t['title']}{self.END}")
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")
        
        try:
            choice = int(input(f"\n{t['select_pkg']}"))
            if 0 < choice <= len(options):
                self.install(options[choice-1])
        except ValueError:
            pass

    def run(self):
        while True:
            self.clear()
            t = self.texts[self.lang]
            header = f"{'='*35}"
            print(f"{self.CLR}{header}")
            print(f"  {t['title']}")
            print(f"{header}{self.END}")
            print(f"{self.OK}{t['m1']}{self.END}")
            print(f"{self.OK}{t['m2']}{self.END}")
            print(f"{self.CYAN}{t['m3']}{self.END}")
            print(f"{self.ERR}{t['m4']}{self.END}")
            print(f"{self.CLR}{header}{self.END}")

            choice = input(t['ask'])

            if choice == '1':
                for lib in self.core_libs:
                    self.install(lib)
            elif choice == '2':
                self.search_menu()
            elif choice == '3':
                self.lang = 'en' if self.lang == 'ru' else 'ru'
            elif choice == '4':
                print(f"{self.ERR}Exit...{self.END}")
                break

if __name__ == "__main__":
    installer = LinuxDevInstaller()
    installer.run()
