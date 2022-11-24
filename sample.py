import os
os.system("playwright install")

from playwright.sync_api import sync_playwright
import streamlit as st
from playwright_stealth import stealth_sync

st.title('Starting')
with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(user_agent="Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
        stealth_sync(page)
        page.goto('https://www.manta.com/mb_33_C4_000/restaurants_and_bars')
        st.text(page.title())
        page.goto('https://www.manta.com/c/mms0zjs/lambertville-trading-company')
        st.text(page.title())
        browser.close()
