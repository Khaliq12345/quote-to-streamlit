import os
os.system("playwright install")

from playwright.sync_api import sync_playwright
import streamlit as st
from playwright_stealth import stealth_sync
st.title('Starting')
with sync_playwright() as p:
        # Can be "msedge", "chrome-beta", "msedge-beta", "msedge-dev", etc.
        browser = p.chromium.launch()
        page = browser.new_page(user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
        stealth_sync(page)
        page.goto('https://www.manta.com/mb_33_C4_000/restaurants_and_bars')
        st.text(page.title())
        page.screenshot(path="screenshot.png")
        st.image('screenshot.png')
        page.goto('https://www.whitepages.com/business/LA/New-Orleans/Doctors')
        st.text(page.title())
        page.screenshot(path="screenshot.png")
        st.image('screenshot.png')
        browser.close()
