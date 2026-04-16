import os
from pathlib import Path

class DemoPage:
    def __init__(self, page):
        self.page = page
        # путь к локальному файлу
        html_path = Path(__file__).parent.parent / "testsite" / "form.html"
        self.url = f"file://{html_path.resolve()}"

    def open(self):
        self.page.goto(self.url)

    def fill_form(self, name, email):
        self.page.fill("#userName", name)
        self.page.fill("#userEmail", email)
        self.page.click("#submit")

    def get_output(self):
        return self.page.inner_text("#output")