import os
os.system("playwright install")

from playwright.sync_api import sync_playwright
import streamlit as st

st.title('Starting')
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://playwright.dev")
    st.text(page.title())
    browser.close()
