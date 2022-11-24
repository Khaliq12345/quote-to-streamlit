import os
os.system("playwright install")

from cf_clearance import sync_cf_retry, sync_stealth
from playwright.sync_api import sync_playwright
import streamlit as st

st.title('Starting')
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    sync_stealth(page, pure=True)
    page.goto('https://nowsecure.nl')
    res = sync_cf_retry(page)
    if res:
        cookies = page.context.cookies()
        for cookie in cookies:
            if cookie.get('name') == 'cf_clearance':
                cf_clearance_value = cookie.get('value')
                st.text(cf_clearance_value)
        ua = page.evaluate('() => {return navigator.userAgent}')
        st.text(ua)
    else:
        st.text("cf challenge fail")
    browser.close()
