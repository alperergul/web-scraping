from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import time
from dotenv import load_dotenv  # for python-dotenv method
load_dotenv()

web = "https://twitter.com/search?q=python&src=typed_query"
path = os.environ.get("DRIVER_PATH")
driver = webdriver.Chrome(path)
driver.get(web)


def get_tweet(element):
    try:
        user = element.find_element_by_xpath('.//span[contains(text(),"@")]').text
        text = element.find_element_by_xpath('.//div[@lang]').text
        tweets_data = [user, text]
    except:
        tweets_data = ['user', 'text']

    return tweets_data


user_data = []
text_data = []
tweets = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located(
    (By.XPATH, "//article[@role='article']")))

for tweet in tweets:
    tweet_list =  get_tweet(tweet)
    user_data.append(tweet_list[0])
    text_data.append(" ".join(tweet_list[1].split()))

driver.quit()

df = pd.DataFrame({'user': user_data, 'text': text_data})

df.to_csv('tweets.csv', index=False)
print(df)
