
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
driver.implicitly_wait(8)
my_element = driver.find_element("id", "downloadButton")
my_element.click()

# progress_element = driver.find_element("class name", "progress-label")
# print(f"{progress_element.text == 'Completed!'}")

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
    (By.CLASS_NAME, 'progress-label'), # Element Filtration
    'Complete!' # The Expected Text
    )
)