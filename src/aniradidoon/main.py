from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Tabs
import sys

Channels = [
    "Onsen",
    "Settings"
]

class aniradidoonApp(App):
    BINDINGS = [("d", "toggleDark", "Dark"), ("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True, name="AniradiDoon - Control")
        yield Tabs(Channels[0], Channels[1])
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(Tabs).focus()

    def action_toggleDark(self) -> None:
        self.dark = not self.dark

    def action_quit(self) -> None:
        sys.exit()

if __name__ == "__main__":
    app = aniradidoonApp()
    app.run()