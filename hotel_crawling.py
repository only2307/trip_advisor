import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# default number of scraped pages
num_page = 20

url = 'https://www.tripadvisor.com'
# Import the webdriver
driver = webdriver.Edge('msedgedriver.exe')
driver.get(url)

# find search input form
search = driver.find_element_by_xpath(".//div[@class='QvCXh cyIij fluiI']//input[@class='qjfqs _G B- z _J Cj R0']")
time.sleep(3)
search.send_keys("Ho Chi Minh City")
time.sleep(2)
search.send_keys(Keys.ENTER)
# switch to Hotels tab
time.sleep(2)
hotel = driver.find_element_by_xpath(".//*[@id='search-filters']/ul/li[2]/a")
hotel.click()
time.sleep(2)
# Initialize list to store results
hotel_names = []
hotel_ratings = []
hotel_reviews = []
hotel_links = []
# select all attributes of each hotel
for i in range(num_page):
    xpath = ".//div[@class='ui_column is-9-desktop is-8-mobile is-9-tablet content-block-column']/div[@class='location-meta-block']"

    names = driver.find_elements_by_xpath(xpath + "/div[@class='result-title']/span")
    ratings = driver.find_elements_by_xpath(xpath + "/div[@class='rating-review-count']/div/span")
    reviews = driver.find_elements_by_xpath(xpath + "/div[@class='rating-review-count']/div/a[@class='review_count']")

    for j in range(30):
        name = names[j].text
        rating = ratings[j].get_attribute('alt').split(' ')[0]
        review = reviews[j].text.split(' ')[0]
        link = reviews[j].get_attribute('href')
        hotel_names.append(name)
        hotel_ratings.append(rating)
        hotel_reviews.append(review)
        hotel_links.append(link)
        
    driver.find_element_by_xpath(".//a[@class='ui_button nav next primary ']").click()
    time.sleep(2)
#hotel_names.append(name)
# ratings = driver.find_elements_by_xpath(xpath + "/div[@class='rating-review-count']/div/span").get_attribute('alt').split(' ')[0]
# print(rating)
# #hotel_ratings.append(rating)
# reviews = driver.find_elements_by_xpath(xpath + "/div[@class='rating-review-count']/div/a[@class='review_count']").text.split(' ')[0]
# print(review)
# #hotel_reviews.append(review)
# links = driver.find_elements_by_xpath(xpath + "/div[@class='rating-review-count']/div/a[@class='review_count']").get_attribute('href')
# print(link)
# #hotel_links.append(link)
# i += 1

my_dict = {
    "Hotel": hotel_names,
    "Rating": hotel_ratings,
    "Review": hotel_reviews,
    "Link": hotel_links,
}

test_df = pd.DataFrame(my_dict)
test_df.to_csv('test.csv', index=False)

driver.close()