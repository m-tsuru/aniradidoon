from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Tabs, DataTable, Placeholder, Select, Label, Input, Button, Log
import sys
import onsen

onsenBaseData = onsen.OnsenAPIData()

class aniradidoonApp(App):
    CSS_PATH = "style.scss"
    BINDINGS = [("d", "toggleDark", "Dark"),
                ("q", "quit", "Quit"),
                ("l", "switch_mode('Onsen')", "Program List")]
    


    class onsenListScreen(Screen):

        def compose(self) -> ComposeResult:
            self.success = True
            self.selectedOnsenProgram = ""
            yield Header(show_clock=True, name="AniradiDoon - Control")
            Header.screen_title = "Aniradi Doon"
            Header.screen_sub_title = "All Programs List"
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

    class downloadScreen(Screen):
        def compose(self) -> ComposeResult:
            yield Header(show_clock=True, name="AniradiDoon - Control")
            Header.screen_title = "Aniradi Doon"
            Header.screen_sub_title = "Download Option"
            yield Label("Program Detail:", classes="labelLeft")
            yield DataTable(id="detailProgram")
            yield Label("Download Content:", classes="labelLeft")
            yield Select.from_values(["第1回 (1/5, Movie, Free)【Guest: hoge】", "第2回 (1/5, Movie, Free)【Guest: hoge】"])
            yield Label("Convert Option:", classes="labelLeft")
            yield Select.from_values(["Original", "Sound Only"])
            yield Label("Execute FFmpeg:", classes="labelLeft")
            yield Input(placeholder="Select Download Content!", disabled=True)
            yield Button(label="Execute")
            yield Log()
            yield Footer()

        def on_mount(self) -> None:
            onsenDetailData = onsen.OnsenAPIDetailData(selectedOnsenProgram)
            detailProgram = onsenDetailData.summary()[0]
            table = self.query_one(DataTable)
            table.cell_padding = True
            table.zebra_stripes = False
            table.show_cursor = False
            table.add_columns(*detailProgram[0])
            table.add_rows(detailProgram[1:])
            log = self.query_one(Log)
            log.write_line("Info: Get Program Data from Onsen API")
            log.write_line("Info: " + str(detailProgram))
    class preferencesScreen(Screen):
        def compose(self) -> ComposeResult:
            yield Header(show_clock=True, name="AniradiDoon - Control")
            yield Placeholder("Preferences will be available soon!")
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
            self.selectedOnsenProgram = "gurepa"
            self.switch_mode('Download')

    def action_toggleDark(self) -> None:
        self.dark = not self.dark

    def action_quit(self) -> None:
        sys.exit()


if __name__ == "__main__":
    app = aniradidoonApp()
    app.run()
