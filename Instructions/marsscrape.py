
# %%
import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from flask import Flask, render_template
import pymongo


# %%

def init_browser():
    executable_path = {"executable_path":"chromedriver.exe"}
    browser = Browser('chrome',**executable_path, headless=False)

def scrape_info():
    browser=init_browser

# %%
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")
    
    articles = soup.find_all("div", class_="list_text")
    
    for article in articles:
        title = article.find('div', class_='content_title').text
        body = article.find('div', class_='article_teaser_body').text
        
       

        
    #browser.click_link_by_partial_text('Next')


def scrape_featured():
    browser=init_browser

# %%
    feature = 'https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA00271'
    browser.visit(feature)

def scrape_hemi1():
    browser=init_browser

    hemi1='https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(hemi1)

def scrape_hemi2():
    browser=init_browser

    scrape_hemi2='https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced''
    browser.visit(hemi2)

def scrape_hemi3():
    browser=init_browser

    scrape_hemi3='https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(hemi3)

def scrape_hemi4():
    browser=init_browser

    scrape_hemi4='https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(hemi4)

    # Store data in a dictionary
    marsdict = {
        "featured_img": featured_img,
        "url2":
    }

    

browser.quit()
       

# %%
import pandas as pd        
url = 'https://space-facts.com/mars/'
        

# %%
tables = pd.read_html(url)
print(tables[0])

tables[2].head()
    
    
# %%
type(tables)


# %%
df=tables[0]
df.columns = ['Measure', 'Fact']
df.head()


# %%
#def init_browser():
    #executable_path = {"executable_path":"chromedriver.exe"}
    #return Browser("chrome", **executable_path, headless=False)


# %%
df = df.iloc[1:]
df.set_index('Measure', inplace=True)
df.head()


# %%
html_table = df.to_html()
html_table


# %%
html_table.replace('\n', '')


# %%



# %%
#for abb in med_abbreviations:
    #print(abb, df.loc[abb].full_name)


# %%
#def scrape():
    #browser = init_browser()
    


