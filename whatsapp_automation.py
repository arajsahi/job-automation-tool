from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print("Scan the QR code then press Enter")
input()
time.sleep(3)

contact_name = "Carlous"
search_box = driver.find_element(By.XPATH, '//div[@aria-label="Search input textbox"]')
search_box.click()
search_box.send_keys(contact_name)
time.sleep(2)
search_box.send_keys(Keys.ENTER)
time.sleep(2)

message_box = driver.find_element(By.XPATH, '//div[@aria-label="Type a message"]')
message_box.click()
message_box.send_keys("Hello Carlous! This message was sent automatically by Python!")
time.sleep(1)
message_box.send_keys(Keys.ENTER)
print("Message sent successfully!")