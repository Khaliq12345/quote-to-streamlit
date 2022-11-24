import os
os.system("playwright install")

from playwright.sync_api import sync_playwright
import streamlit as st
from playwright_stealth import stealth_sync
st.title('Starting')
with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page("Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36")
        stealth_sync(page)
        page.goto('https://www.manta.com/c/mms0zjs/lambertville-trading-company')
        st.text(page.title())
        browser.close()
