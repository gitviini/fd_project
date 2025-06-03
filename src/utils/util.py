import os

def clear() -> None:
    os.system("clear" if os.name == "posix" else "cls")