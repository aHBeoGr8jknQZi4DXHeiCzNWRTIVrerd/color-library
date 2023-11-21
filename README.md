
# Color Library

A simple color library in python

I fixed the Fore.RESET and Background.RESET, also added Gradient() for both
Added ANSI escape codes support for command prompt
## Importing

```py
from modules.colors import Fore, Backgroundy Style
```
## Changing Fore
```py
print(Fore.RGB(150,150,150) + 'Hello')
```
## Changing Background
```py
print(Background.RGB(255,50,0) + 'Hello')
```
## Styles
### Underline
```py
print(Style.UNDERLINE() + 'Hello')
```
### Blink
```py
print(Style.BLINK() + 'Hello')
```
### Bold
```py
print(Style.BOLD() + 'Hello')
```
### Reset ALL
```py
print(Style.RESET() + 'Hello')
```


