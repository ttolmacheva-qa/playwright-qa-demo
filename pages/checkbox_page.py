from pathlib import Path

class CheckboxPage:
    def __init__(self, page):
        self.page = page
        html_path = Path(__file__).parent.parent / "testsite" / "checkbox.html"
        self.url = f"file://{html_path.resolve()}"

    def open(self):
        self.page.goto(self.url)

    def select(self, *ids):
        for cb_id in ids:
            self.page.check(f"#{cb_id}")

    def show_result(self):
        self.page.click("#show")

    def get_result(self):
        return self.page.inner_text("#result")
