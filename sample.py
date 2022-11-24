import os
os.system("playwright install")

from playwright.sync_api import sync_playwright
import streamlit as st
from playwright_stealth import stealth_sync

st.title('Starting')
with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36")
        stealth_sync(page)
        page.goto('https://www.manta.com/mb_33_C4_000/restaurants_and_bars')
        st.text(page.title())
        browser.close()
