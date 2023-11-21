import platform
class Background:
    def RGB(color1: int, color2: int, color3: int) -> str:
        try:
            return f"\u001b[48;2;{color1};{color2};{color3}m"
        except:
            return f"\u001b[49m"
    def Gradient(text: str = "", color1: tuple = (255, 0, 0), color2: tuple = (0, 0, 255)) -> str:
        return "".join(f"\u001b[48;2;{r};{g};{b}m{char}" for char, (r, g, b) in zip(text, [
            tuple(int(c1 + (c2 - c1) * i / (len(text) - 1)) for c1, c2 in zip(color1, color2))
            for i in range(len(text))
        ]))
    def RESET() -> str:
        return f"\u001b[49m"
    
class Fore:
    def RGB(color1: int, color2: int, color3: int) -> str:
        try:
            return f"\u001b[38;2;{color1};{color2};{color3}m"
        except:
            return f"\u001b[39m"
    def Gradient(text: str = "", color1: tuple = (255, 0, 0), color2: tuple = (0, 0, 255)) -> str:
        return "".join(f"\u001b[38;2;{r};{g};{b}m{char}" for char, (r, g, b) in zip(text, [
            tuple(int(c1 + (c2 - c1) * i / (len(text) - 1)) for c1, c2 in zip(color1, color2))
            for i in range(len(text))
        ]))
    def RESET() -> str:
        return f"\u001b[39m"
    
class Style:
    def RESET() -> str:
        return f"\u001b[0m"
    def BOLD() -> str:
        return f"\u001b[1m"
    def UNDERLINE() -> str:
        return f"\u001b[4m"
    def BLINK() -> str:
        return f"\u001b[5m"
    def REVERSE() -> str:
        return f"\u001b[7m"
    def DIM() -> str:
        return f"\u001b[2m"

if platform.system() == "Windows": #Enable ANSI escape codes in command prompt
    from ctypes import windll
    windll.kernel32.SetConsoleMode(windll.kernel32.GetStdHandle(-11), 7)
