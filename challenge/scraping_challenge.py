# Import Dependencies
import pandas as pd
import datetime as dt
from datetime import datetime
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup

def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    news_title, news_paragraph = mars_news(browser)
    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "cerberus_images": cerberus_images(browser),
        "schiaparelli_images": schiaparelli_images(browser),
        "syrtis_images": syrtis_images(browser),
        "valles_images": valles_images(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
        }
    return data

def mars_news(browser):
    # Featured Article 
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    # Set up the HTML parser:
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')
        # Chain .find onto our previously assigned variable, "slide_elem."
        slide_elem.find("div", class_='content_title')
        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find("div", class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
        
    except AttributeError:
        return None, None
    return news_title, news_p

def featured_image(browser):
    # Mars Images
    # # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()
    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()
    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    try:
        # Find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")
        
    except AttributeError:
        return None
    # Use the base URL to create an absolute URL
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    
    return img_url
    



def cerberus_images(browser):
    # Mars Image URLs
    # Visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    # Find and click the hemisphere link button
    image_elem = browser.find_by_css('a.product-item h3')
    image_elem.click()
    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    # Find the title
    title_elem= img_soup.find("h2", class_="title").get_text()
    title_elem
    # Find the sample button and click
    sample_elem= browser.find_by_text('Sample')
    sample_elem.click()
    try:
        # Find the relative image url
        img_url_rel = img_soup.find_all('img')[4]["src"]
    except AttributeError:
        return None
    # Use the base URL to create an absolute URL
    img_url = f'https://astrogeology.usgs.gov{img_url_rel}'
    
    return img_url

def schiaparelli_images(browser):
    # Mars Image URLs
    # Visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    # Find and click the hemisphere link button
    image_elem = browser.find_by_css('a.product-item h3')
    image_elem.click()
    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    # Find the title
    title_elem= img_soup.find("h2", class_="title").get_text()
    title_elem
    # Find the sample button and click
    sample_elem= browser.find_by_text('Sample')
    sample_elem.click()
    try:
        # Find the relative image url
        img_url_rel = img_soup.find_all('img')[10]["src"]
    except AttributeError:
        return None
    # Use the base URL to create an absolute URL
    img_url = f'https://astrogeology.usgs.gov{img_url_rel}'
    
    return img_url

def syrtis_images(browser):
    # Mars Image URLs
    # Visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    # Find and click the hemisphere link button
    image_elem = browser.find_by_css('a.product-item h3')
    image_elem.click()
    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    # Find the title
    title_elem= img_soup.find("h2", class_="title").get_text()
    title_elem
    # Find the sample button and click
    sample_elem= browser.find_by_text('Sample')
    sample_elem.click()
    try:
        # Find the relative image url
        img_url_rel = img_soup.find_all('img')[9]["src"]
    except AttributeError:
        return None
    # Use the base URL to create an absolute URL
    img_url = f'https://astrogeology.usgs.gov{img_url_rel}'
    
    return img_url

def valles_images(browser):
    # Mars Image URLs
    # Visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    # Find and click the hemisphere link button
    image_elem = browser.find_by_css('a.product-item h3')
    image_elem.click()
    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    # Find the title
    title_elem= img_soup.find("h2", class_="title").get_text()
    title_elem
    # Find the sample button and click
    sample_elem= browser.find_by_text('Sample')
    sample_elem.click()
    try:
        # Find the relative image url
        img_url_rel = img_soup.find_all('img')[7]["src"]
    except AttributeError:
        return None
    # Use the base URL to create an absolute URL
    img_url = f'https://astrogeology.usgs.gov{img_url_rel}'
    
    return img_url
    
    
def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]

    except BaseException:
        return None
    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars']
    df.set_index('Description', inplace=True)
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()
    
if __name__ == "__main__":
        # If running as script, print scraped data
        print(scrape_all())