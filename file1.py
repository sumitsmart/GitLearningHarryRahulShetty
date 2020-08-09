from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="//Users//sumitshivhare//My_Workspace//chromedriver")
driver.implicitly_wait(5)
driver.get("https://www.google.com")
print("Tile of Page is: ",driver.title)
driver.find_element(By.NAME,"q").send_keys("NaveenAutomtion Labs")
time.sleep(4)
search_result = driver.find_elements(By.XPATH,"//ul[@class='erkvQe']//li//span")
#print(type(search_result))
print(len(search_result))
if len(search_result)  == 10:
    print("Pass")
else:
    print("Failed")

for i in search_result:
    #print(i.text)
    if i.text == "naveen automation labs cucumber":
        i.click()
        break
print("Text Clicked")
driver.quit()