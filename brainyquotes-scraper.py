import os
os.system("playwright install")
import requests
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
from playwright.sync_api import sync_playwright
import streamlit as st
from playwright_stealth import stealth_sync

def scrape(keyword, pages):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
        stealth_sync(page)
        quote_list = []
        for p in range(1, int(pages)):
            sleep(2)
            page.goto(f'https://www.brainyquote.com/topics/{keyword}-quotes_{p}')
            st.text(f'Page {p}')
            page.is_visible('div#pos_1_2', timeout = 60.0)
            html = page.inner_html("div#quotesList")
            soup = BeautifulSoup(html,'lxml')
            cards = soup.find_all('div',{'class':'grid-item qb clearfix bqQt'})
            for card in cards:
                try:
                    #name
                    name = card.find('a',{'title':'view author'}).text
                except:
                    name = 'N/A'

                try:
                    #quote
                    quote = card.find('a',{'title':'view quote'}).text.strip()
                except:
                    quote = 'N/A'

                quotes = {
                'Author': name,
                'Quote': quote
                }
                quote_list.append(quotes)

        df = pd.DataFrame(quote_list)
        return st.dataframe(df)
    browser.close()

if __name__ == '__main__':
    st.title('brainyquote.com Scraper')
    st.text('Instruction on how to input the topic')
    st.text('1. The topic needs to be in lower case (age, experience)')
    st.text('2. Use hypen instead of space (new-year, mother-day)')
    st.text("3. Do not use apostrophe (') instead just add it to the keyword [(Valentine's day ==> valentines-day), (New Year's) ==> (new-years)")
    with st.form('Scrape'):
        keyword = st.text_input('What topic will you like to scrape')
        pages = st.number_input('Number of pages to scrape (Always add +1 to the number of pages you want)')
        search = st.form_submit_button('Scrape')
        if search:
            scrape(keyword, pages)


