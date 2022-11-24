import os
os.system("playwright install")

from playwright.sync_api import sync_playwright
import streamlit as st
from playwright_stealth import stealth_sync
ua = ["Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36"]
st.title('Starting')
with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(ua[0])
        stealth_sync(page)
        page.goto('https://www.manta.com/mb_33_C4_000/restaurants_and_bars')
        st.text(page.title())
        page = browser.new_page(ua[1])
        page.goto('https://www.manta.com/c/mms0zjs/lambertville-trading-company')
        st.text(page.title())
        browser.close()
