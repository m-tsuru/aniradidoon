from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Tabs, DataTable, Placeholder
import sys
import onsen

onsenBaseData = onsen.OnsenAPIData()

class aniradidoonApp(App):
    BINDINGS = [("d", "toggleDark", "Dark"), ("q", "quit", "Quit")]
    class onsenListScreen(Screen):

        def compose(self) -> ComposeResult:
            self.success = True
            yield Header(show_clock=True, name="AniradiDoon - Control")
            yield Tabs("Onsen")
            if onsenBaseData.result == True:
                try:
                    yield DataTable()
                except Exception as e:
                    yield Placeholder(f"Summary Could not be got: {e}")
                    self.success = False
            else:
                yield Placeholder(f"{onsenBaseData.error}")
                self.success = False
            yield Footer()
            
        def on_mount(self) -> None:
            if self.success != False:
                summary = onsenBaseData.summary()
                table = self.query_one(DataTable)
                table.cursor_type = "row"
                table.zebra_stripes = True
                table.add_columns(*summary[0])
                table.add_rows(summary[1:])

    class preferencesScreen(Screen):
        def compose(self) -> ComposeResult:
            yield Header(show_clock=True, name="AniradiDoon - Control")
            yield Placeholder("Preferences")
            yield Footer()

    MODES = {
        "Onsen": onsenListScreen,
        "Download": downloadScreen,
        "Preferences": preferencesScreen,
    }

    BINDINGS.append(("p", "switch_mode('Preferences')", "Preferences"))

    def on_mount(self) -> None:
        self.switch_mode("Onsen")

    def on_data_table_row_selected(self):
        self.switch_mode('Download')

    def action_toggleDark(self) -> None:
        self.dark = not self.dark

    def action_quit(self) -> None:
        sys.exit()


if __name__ == "__main__":
    app = aniradidoonApp()
    app.run()
