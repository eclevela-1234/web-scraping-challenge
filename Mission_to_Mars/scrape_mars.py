from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit news site
    url = "https://redplanetscience.com/"
    browser.visit(url)
    time.sleep(1)
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    # Get the news
    news = soup.find('div', id='news')
    # Get the first headline
    news_title = news.find_all("div")[7].text
    # Get the synopsis
    news_para = news.find_all("div")[8].text



    # Visit image  site
    url2 = "https://spaceimages-mars.com/"
    browser.visit(url2)
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    # Store body tag elements
    imagepage = soup.find('body')
    # Scrape rel path
    image_rel_path = imagepage.find_all("img")[1]["src"]
    # concatonate with url
    featured_img = url2 + image_rel_path


    # Visit facts site & Scrape table using pandas
    marsdf = pd.read_html("https://galaxyfacts-mars.com/")[0]
    marsdfcode = marsdf.to_html()
    
    # # Visit facts site
    # url3 = "https://galaxyfacts-mars.com/"
    # browser.visit(url3)
    # # Scrape page into Soup
    # html = browser.html
    # soup = bs(html, "html.parser")
    # marsdfcode = soup.find_all('table')[0]

    
    
    # Visit Hemisphere + Splinter code to scrape image urls here


    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_para": news_para,
        "featured_img": featured_img,
        "marsdfcode": marsdfcode
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
