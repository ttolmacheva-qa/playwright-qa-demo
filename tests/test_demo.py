from pages.demo_page import DemoPage

def test_form_submit_valid(page):
    demo = DemoPage(page)
    demo.open()
    demo.fill_form("Tolmacheva QA", "ttolmacheva@test.com")
    output = demo.get_output()
    assert "Tolmacheva QA" in output
    assert "ttolmacheva@test.com" in output

def test_form_submit_with_special_chars(page):
    demo = DemoPage(page)
    demo.open()
    demo.fill_form("QA Тест", "qa+test@example.com")
    output = demo.get_output()
    assert "QA Тест" in output
    assert "qa+test@example.com" in output