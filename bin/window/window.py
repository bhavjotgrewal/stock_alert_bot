from typing import List
from rich.console import Console
from rich.table import Table
from datetime import datetime
import pyttsx3

class Window():
    def __init__(self) -> None:
        """ Initializer for the window that displays results.
        """
        self.console = Console()

        self.table = Table(show_header=True, header_style="bold magenta")
        self.table.add_column("Store", width=12)
        self.table.add_column("Product")
        self.table.add_column("In Stock", justify="right")
        self.table.add_column("Quantity", justify="right")
        self.table.add_column("Last Checked", justify="right")
        self.engine = pyttsx3.init()

    def add_row(self, store: str, product: str, in_stock: bool, quantity: str, last_checked: str):

        if store == "Newegg":
            color = "bright_red"

        elif store == 'Memory Express':
            color = "bright_green"

        elif store == 'Canada Computers':
            color = 'bright_blue'

        if in_stock:
            self.engine.say(store)
            self.engine.say(product)
            self.table.add_row(f"[{color}]{store}[/{color}]", product, "[green]YES[/green]", quantity, last_checked)
        else:
            self.table.add_row(f"[{color}]{store}[/{color}]", product, "[red]NO[/red]", quantity, last_checked)
        pass

    def fill(self, store, quantity, scraped):

        for process in scraped:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.add_row(store, process[0], process[1], quantity, current_time)

    def speak(self):
        self.engine.runAndWait()

    def display(self):
        self.console.print(self.table)

    def reset(self):
        self.__init__()
