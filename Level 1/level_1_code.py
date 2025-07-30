'''
LEVEL 1 CHALLENGE - HAPPY PRIDE MONTH
    Write a program that prints "Hello World" every 0.1 seconds, forever.
    Each printed line should be a different color than the previous line.
'''

# This is an "import", ignore this for now, you're too hot and rich to understand this.
import time
from rich import print

while True:
    print("[red]Hello World")
    sleep(.1)
    print("[orange]Hello World")
    sleep(.1)
    print("[yellow]Hello World")
    sleep(.1)
    print("[green]Hello World")
    sleep(.1)
    print("[blue]Hello World")
    sleep(.1)
    print("[purple]Hello World")
    sleep(.1)
    pass # TODO - Replace this with your code!
