from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

import os
from dotenv import load_dotenv  # for python-dotenv method
load_dotenv()


website = "https://www.adamchoi.co.uk/overs/detailed"
path = os.environ.get("DRIVER_PATH")
driver = webdriver.Chrome(path)
driver.get(website)

all_matches_button = driver.find_element_by_xpath(
    '//label[@analytics-event="All matches"]')
all_matches_button.click()


drop_down = Select(driver.find_element_by_id('country'))
drop_down.select_by_visible_text('Turkey')

time.sleep(3)

matches = driver.find_elements_by_tag_name('tr')

date = []
home_team = []
score = []
away_team = []


for match in matches:
    date.append(match.find_element_by_xpath('./td[1]').text)
    home = match.find_element_by_xpath('./td[2]').text
    print(home)
    home_team.append(match.find_element_by_xpath('./td[2]').text)
    score.append(match.find_element_by_xpath('./td[3]').text)
    away_team.append(match.find_element_by_xpath('./td[4]').text)


df = pd.DataFrame({'date': date, 'home_team': home_team,
                  'score': score, 'away_team': away_team})

df.to_csv('football_data.csv', index=False)
print(df)

# driver.quit()
