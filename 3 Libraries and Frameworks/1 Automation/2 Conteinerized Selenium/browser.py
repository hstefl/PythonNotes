from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.options import ArgOptions


class BrowserOptionsFactory:
    @staticmethod
    def get_instance(browser_id: str) -> ArgOptions:
        browser_options = {
            "chrome": BrowserOptionsFactory.__get_chrome_options,
            "firefox": BrowserOptionsFactory.__get_firefox_options,
        }

        try:
            return browser_options[browser_id.lower()]()
        except KeyError:
            raise ValueError("Unsupported browser: Use 'chrome' or 'firefox'")

    @staticmethod
    def __get_chrome_options() -> ArgOptions:
        options: ChromeOptions = ChromeOptions()
        prefs = {
            "profile.default_content_setting_values.notifications": 2,  # Disable notifications
            "profile.default_content_setting_values.cookies": 2  # Block cookies dialog
        }
        options.add_experimental_option("prefs", prefs)
        return options

    @staticmethod
    def __get_firefox_options() -> ArgOptions:
        options: FirefoxOptions = FirefoxOptions()
        options.set_preference("dom.webnotifications.enabled", False)  # Disable notifications
        options.set_preference("network.cookie.cookieBehavior", 2)  # Block cookies dialog
        return options
