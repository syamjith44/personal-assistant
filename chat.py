from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
import requests
import sys
import os

from llama import LlamaChat

API_URL = "http://localhost:8000/chat/"
console = Console()
terminal_width = console.size.width

def get_hidden_input():
    """Get input and attempt to hide the echo"""
    console.print("[bold cyan]You:[/bold cyan] ", end="")
    user_input = input()
    
    # Try to clear the input line (works on most modern terminals)
    try:
        # Move cursor up and clear line
        print("\033[A\033[2K", end="")  # ANSI: up one line, clear entire line
        
        # Reprint just our styled prompt with the input
        text = Text(f"{user_input}", style="bold cyan")
        panel = Panel(text, border_style="cyan", title="You", title_align="left", box=box.ROUNDED)
        aligned = Align.left(panel, width=terminal_width)
        console.print(aligned)
        
    except:
        # Fallback: just add some visual separation
        console.print()
    
    return user_input

def styled_bot_msg(msg: str):
    text = Text(msg, style="bold magenta")
    panel = Panel(text, border_style="magenta", title="AI", title_align="right", box=box.ROUNDED)
    aligned = Align.right(panel, width=terminal_width)
    console.print(aligned)

console.print("[bold green]🤖 Terminal Chat[/bold green] — type 'exit' to quit")
console.print()

while True:
    user_input = get_hidden_input()

    if user_input.lower() == "exit":
        chat = LlamaChat(
            chat_input=user_input,
            exit=True
        )
        break
    # try:
    chat = LlamaChat(chat_input=user_input)
    # except:
    #     console.print("[red]Error communicating with model.[/red]")
    # else:
    styled_bot_msg(chat.response)
        
    
    console.print()  # Add spacing between exchanges
    