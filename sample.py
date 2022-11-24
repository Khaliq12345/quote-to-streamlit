import os
os.system("playwright install")

from playwright.sync_api import sync_playwright
import streamlit as st
from playwright_stealth import stealth_sync
st.title('Starting')
with sync_playwright() as p:
        # Can be "msedge", "chrome-beta", "msedge-beta", "msedge-dev", etc.
        browser = p.chromium.launch()
        page = browser.new_page(user_agent = "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36")
        stealth_sync(page)
        page.goto('https://www.whitepages.com/business/CA/Manhattan-Beach/Restaurants')
        st.text(page.title())
        page.screenshot(path="screenshot.png")
        st.image('screenshot.png')
        browser.close()
