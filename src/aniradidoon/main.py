from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
import sys

class aniradidoonApp(App):
    BINDINGS = [("d", "toggleDark", "Dark"), ("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def action_toggleDark(self) -> None:
        self.dark = not self.dark

    def action_quit(self) -> None:
        sys.exit()

if __name__ == "__main__":
    app = aniradidoonApp()
    app.run()