import os
os.system("playwright install")

from playwright.sync_api import sync_playwright
import streamlit as st
from playwright_stealth import stealth_sync
st.title('Starting')
with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(user_agent = "Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36")
        # stealth_sync(page)
        page.goto('www.manta.com')
        st.text(page.title())
        browser.close()
