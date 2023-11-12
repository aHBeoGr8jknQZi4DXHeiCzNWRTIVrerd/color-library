class Background:
    def RGB(color1: int, color2: int, color3: int) -> str:
        try:
            return f"\u001b[48;2;{color1};{color2};{color3}m"
        except Exception as e:
            return f"\u001b[0m"
    def RESET() -> str:
        return f"\u001b[48m"
    
class Fore:
    def RGB(color1: int, color2: int, color3: int) -> str:
        try:
            return f"\u001b[38;2;{color1};{color2};{color3}m"
        except Exception as e:
            return f"\u001b[38m"
    def RESET() -> str:
        return f"\u001b[38m"
    
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
