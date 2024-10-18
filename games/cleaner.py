import os
class Cleaner:
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
