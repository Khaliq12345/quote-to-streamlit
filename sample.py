import os
os.system("playwright install")

from playwright.sync_api import sync_playwright
import streamlit as st
from playwright_stealth import stealth_sync

st.title('Starting')
with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        stealth_sync(page)
        page.goto('http://manta.com/')
        st.text(page.title())
        browser.close()
