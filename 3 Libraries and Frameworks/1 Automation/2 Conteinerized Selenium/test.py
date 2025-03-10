# Before running scripts start docker compose
# `docker-compose up` and get famaliar with logs


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from browser import BrowserOptionsFactory


def main():
    browser_id: str = "firefox"

    options = BrowserOptionsFactory.get_instance(browser_id)

    # Set up the WebDriver to connect to the Selenium Grid Hub
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )

    try:
        # Open a webpage
        driver.get("http://www.google.com")

        # Find an element
        search_box = driver.find_element("name", "q")

        # Interact with the element
        search_box.send_keys(f"Selenium Python {browser_id}")
        search_box.send_keys(Keys.RETURN)

        # Wait for results to load
        time.sleep(1)

        # Print the title of the page
        print(driver.title)
    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    main()
