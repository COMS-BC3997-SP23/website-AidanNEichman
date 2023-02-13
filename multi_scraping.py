import concurrent.futures
import datetime
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def get_game_ids(url, ids):
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    elements = driver.find_elements(By.CSS_SELECTOR, "a.AnchorLink")
    for element in elements:
        href = element.get_attribute("href")
        if href and "/mlb/game?gameId=" in href:
            ids.add(href)
    driver.quit()

    
start = datetime.datetime(2017, 4, 1)
end = datetime.datetime(2023, 2, 11)
curr = start                                                                
ids = set()
with concurrent.futures.ThreadPoolExecutor() as executor: 
    while curr <= end:
        url = "https://www.espn.com/mlb/schedule/_/date/"
        date = curr.strftime("%Y%m%d")
        curr += datetime.timedelta(days=1)
        url += date
        executor.submit(get_game_ids, url, ids)

