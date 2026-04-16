
class DemoPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://demoqa.com/text-box"

    def open(self):
        self.page.goto(self.url)

    def fill_form(self, name, email):
        self.page.fill("#userName", name)
        self.page.fill("#userEmail", email)
        self.page.click("#submit")

    def get_output(self):
        return self.page.text_content("#output")
