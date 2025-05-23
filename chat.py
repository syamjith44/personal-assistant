import requests
from rich.console import Console
from rich.prompt import Prompt

API_URL = "http://localhost:8000/chat/"
console = Console()

console.print("[bold green]Terminal Chat[/bold green] — type 'exit' to quit")

while True:
    user_input = Prompt.ask("[bold blue]You[/bold blue]")
    if user_input.lower() == "exit":
        requests.post(API_URL, json={"input": user_input, "exit": True})
        break

    response = requests.post(API_URL, json={"input": user_input, "exit": False})
    if response.status_code == 200:
        reply = response.json()["bot"]
        console.print(f"[bold magenta]AI:[/bold magenta] {reply}")
    else:
        console.print("[red]Error communicating with server.[/red]")