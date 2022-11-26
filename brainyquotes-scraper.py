import os
os.system("playwright install")
import requests
from bs4 import BeautifulSoup
import pandas as pd
from playwright.sync_api import sync_playwright
import streamlit as st
from playwright_stealth import stealth_sync
from fake_useragent import UserAgent
ua = UserAgent()

def scrape(keyword, pages):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(user_agent = ua.random)
        quote_list = []
        for p in range(1, int(pages)):
            page.goto(f'https://www.brainyquote.com/topics/{keyword}-quotes_{p}')
            st.text(f'Page {p}')
            try:
                page.wait_for_selector('div#pos_1_2')
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
            except:
                pass

        df = pd.DataFrame(quote_list)
        st.dataframe(df)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Press to Download",
            csv,
            f"{keyword}-quote-data.csv",
            "text/csv",
            key='download-csv'
        )
        
        browser.close()

if __name__ == '__main__':
    st.title('BRAINYQUOTE.COM SCRAPER')
    st.markdown('<h2> Instruction on how to input the topics <h2/>', unsafe_allow_html=True)
    st.text('1. (Experience ==> experience)')
    st.text('2. (Mothers day ==> mothers-day)')
    st.text("3. (Valentine's day ==> valentines-day)")
    st.caption('Fields to be scraped are: Author name and quote')
    with st.form('Scrape'):
        keyword = st.text_input('What topic will you like to scrape')
        pages = st.number_input('Number of pages to scrape (Always add +1 to the number of pages you want)')
        search = st.form_submit_button('Scrape')
    if search:
        scrape(keyword, pages)
        st.balloons()
        st.success('Success')


