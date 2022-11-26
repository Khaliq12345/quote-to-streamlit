import requests
import streamlit as st
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
ua = UserAgent()

def scrape(keyword, pages):
    quote_list = []
    col1, col2 = st.columns(2)
    progress = col1.metric('Pages Scraped', 0)
    for p in range(1, int(pages)):
        headers = {'User-Agent': ua.random}
        response = requests.get(f'https://quotes.toscrape.com/tag/{keyword}/page/{p}/', headers = headers)
        progress.metric('Pages Scraped', p)
        soup = BeautifulSoup(response.text,'lxml')
        cards = soup.select('.quote')
        for card in cards:
            try:
                #name
                author = card.select_one('.author').text
            except:
                name = None

            try:
                #quote
                quote = card.select_one('.text').text
            except:
                quote = None

            quotes = {
            'Author': author,
            'Quote': quote
            }
            quote_list.append(quotes)

    df = pd.DataFrame(quote_list)
    with st.spinner("Loading..."):
        sleep(5)

    col2.metric('Total data scraped', value = len(df))
    st.dataframe(df)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        "Press to Download",
        csv,
        f"{keyword}-quote-data.csv",
        "text/csv",
        key='download-csv'
    )

if __name__ == '__main__':
    st.title('QUOTETOSCRAPE.COM SCRAPER')
    st.caption('Fields to be scraped are: Author name and quote')
    with st.form('Scrape'):
        keyword = st.selectbox(
        'What tags would you like to scrape?',
         ('love', 'inspirational', 'life', 'humor', 'books', 'reading', 'friendship', 'friends', 'truth')
        )
        pages = st.number_input('Number of pages to scrape (Always add +1 to the number of pages you want)')
        search = st.form_submit_button('Scrape')
    if search:
        scrape(keyword, pages)
        st.balloons()
        st.success('Success')


