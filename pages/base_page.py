class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def get_inner_text(self, locator: str):
        actual = self.page.locator(locator).inner_text()
        assert actual != "", "Текст по локатору не найден"

    def get_text_content(self, locator: str, expected: str):
        actual = self.page.locator(locator).text_content()
        assert actual == expected, f"Ожидали '{expected}', а получили '{actual}'"

    def click(self, locator: str):
        self.page.locator(locator).click()

    def go_back(self,):
        self.page.go_back()

    def fill_and_press_enter(self, locator: str, text: str):
        self.page.locator(locator).fill(text)
        self.page.locator(locator).press("Enter")