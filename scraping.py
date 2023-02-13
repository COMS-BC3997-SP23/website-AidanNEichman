from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta

driver = webdriver.Chrome()

start = datetime(2017, 4, 1)
end = datetime(2023, 2, 11)
curr = start


driver.get("https://www.espn.com/mlb/schedule/_/date/20170401")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
ids = set()

while curr <= end:
    url = "https://www.espn.com/mlb/schedule/_/date/"
    date = curr.strftime("%Y%m%d")
    curr += timedelta(days=1)

    url += date
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    elements = driver.find_elements(By.CSS_SELECTOR, "a.AnchorLink")
    for element in elements:
        
        href = element.get_attribute("href")
        if href and "/mlb/game?gameId=" in href:
            ids.add(href)


    

"""
wait = WebDriverWait(driver, 10)
buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "AtBatAccordion__header")))

for button in buttons:
    try:
        button.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    hit_zone_icons = soup.find_all("div", class_="HitzoneIcon")
    count = 0
    for hit_zone_icon in hit_zone_icons:
        count+=1
        print(hit_zone_icon)

print(count)
"""
driver.quit()
