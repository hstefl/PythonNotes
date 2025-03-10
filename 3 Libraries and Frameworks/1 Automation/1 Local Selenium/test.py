from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def main():
    chrome_options = Options()

    # Add preferences to disable dialogs
    prefs = {
        "profile.default_content_setting_values.notifications": 2,  # Disable notifications
        "profile.default_content_setting_values.cookies": 2  # Block cookies dialog
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Set up the WebDriver (use the path to your WebDriver executable if not in PATH)
    driver = webdriver.Chrome(options=chrome_options)  # For Firefox, use webdriver.Firefox()

    try:
        # Open a webpage
        driver.get("http://www.google.com")

        # Find an element
        search_box = driver.find_element("name", "q")

        # Interact with the element
        search_box.send_keys("Selenium Python")
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
