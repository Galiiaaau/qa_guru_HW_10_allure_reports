from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_selene():
    browser.open("https://github.com")
    s(by.text("Search or jump to...")).click()
    s("#query-builder-test").send_keys("Galiiaaau/qa_guru_HW_8_oop").press_enter()

    s(by.link_text("Galiiaaau/qa_guru_HW_8_oop")).click()
    s("#issues-tab").click()
    s(by.partial_text("Welcome to issues!")).should(be.visible)
    