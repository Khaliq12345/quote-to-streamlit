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
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"}
        response = requests.get(f'https://quotes.toscrape.com/', headers = headers)
        progress.metric('Pages Scraped', p)
        soup = BeautifulSoup(response.text,'html.parser')
        st.text(soup.text)
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


