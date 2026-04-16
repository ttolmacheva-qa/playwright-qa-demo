from pages.checkbox_page import CheckboxPage

def test_checkboxes_select_two(page):
    cb = CheckboxPage(page)
    cb.open()
    cb.select("cb1", "cb3")  # выбираем Manual и Playwright
    cb.show_result()
    result = cb.get_result()
    assert "Manual" in result
    assert "Playwright" in result
    assert "API" not in result
