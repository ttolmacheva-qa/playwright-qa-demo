
from pages.demo_page import DemoPage

def test_form_submit(page):
    demo = DemoPage(page)
    demo.open()
    demo.fill_form("Tolmacheva QA", "ttolmacheva@test.com")
    output = demo.get_output()
    assert "Tolmacheva QA" in output
    assert "ttolmacheva@test.com" in output
