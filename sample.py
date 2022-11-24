import os
os.system("playwright install")

from playwright.sync_api import sync_playwright
import streamlit as st
from playwright_stealth import stealth_sync

st.title('Starting')
with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch()
        page = browser.new_page()
        stealth_sync(page)
        page.goto('http://whatsmyuseragent.org/')
        st.text(page.title())
        browser.close()
