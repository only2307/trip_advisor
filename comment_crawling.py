import sys
import csv
from selenium import webdriver
import time

# default number of scraped pages
num_page = 10

# default tripadvisor website of restaurant
test_url = "https://www.tripadvisor.com/Hotel_Review-g293925-d577218-Reviews-Park_Hyatt_Saigon-Ho_Chi_Minh_City.html"

# Import the webdriver
driver = webdriver.Edge('msedgedriver.exe')
driver.get(test_url)

# Open the file to save the review
# First we need to write column name
with open('hoteldata.csv', 'w', encoding="utf-8") as file:
    csvWriter = csv.writer(file)
    csvWriter.writerow(['Date', 'Rating', 'Title', 'Review'])
    # change the value inside the range to save more or less reviews
    for i in range(0, num_page):
        
        # expand the review 
        time.sleep(2)
        driver.find_element_by_xpath("//span[@class='Ignyf _S Z']").click()

        container = driver.find_elements_by_xpath(".//div[@class='YibKl MC R2 Gi z Z BB pBbQr']")

        for j in range(len(container)):

            title = container[j].find_element_by_xpath(".//div[@class='KgQgP MC _S b S6 H5 _a']/a/span").text
            date = container[j].find_element_by_xpath(".//span[@class='teHYY _R Me S4 H3']").text
            rating = container[j].find_element_by_xpath(".//div[@class='Hlmiy F1']/span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3]
            review = container[j].find_element_by_xpath(".//div[@class='fIrGe _T']/q[@class='QewHA H4 _a']/span").text.replace("\n", " ")

            csvWriter.writerow([date, rating, title, review]) 

        # change the page
        driver.find_element_by_xpath(".//a[@class='ui_button nav next primary ']").click()
file.close()
driver.close()