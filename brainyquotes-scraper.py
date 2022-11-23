import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape(keyword, page):
    quote_list = []
    for p in range(1, int(page)):
        response = requests.get(f'https://www.brainyquote.com/topics/{keyword}-quotes_{p}')
        st.text(f'Page {p}')
        soup = BeautifulSoup(response.text,'lxml')
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
    return st.dataframe(df)

if __name__ == '__main__':
    st.title('brainyquote.com Scraper')
    st.text('Instruction on how to input the topic')
    st.text('1. The topic needs to be in lower case (age, experience)')
    st.text('2. Use hypen instead of space (new-year, mother-day)')
    st.text("3. Do not use apostrophe (') instead just add it to the keyword [(Valentine's day ==> valentines-day), (New Year's) ==> (new-years)")
    with st.form('Scrape'):
        keyword = st.text_input('What topic will you like to scrape')
        page = st.number_input('Number of pages to scrape (Always add +1 to the number of pages you want)')
        search = st.form_submit_button('Scrape')
        if search:
            scrape(keyword, page)


