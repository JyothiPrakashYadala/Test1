from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# The URL of the YouTube video page
url = 'https://www.youtube.com/watch?v=gRLHr664tXA&t=109s'

# Set up the Selenium driver
driver = webdriver.Chrome()
driver.get(url)

# Scroll to the bottom of the page to load all comments
while True:
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="continuations"]/yt-next-continuation/paper-button/yt-formatted-string')
    except:
        break

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the element that contains the comment count
count_element = soup.find('yt-formatted-string', {'class': 'count-text style-scope ytd-comments-header-renderer'})

# Check if the count element was found
if count_element is None:
    print('Could not find the comment count')
else:
    # Extract the text content of the count element
    comment_count = count_element.text.strip()

    # Print the comment count
    print(f'Number of comments: {comment_count}')

# Close the Selenium driver
driver.quit()
