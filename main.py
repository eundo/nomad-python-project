from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 구글 브라우저 생성
browser = webdriver.Chrome(options=options)

browser.get("https://www.indeed.com/jobs?q=python&limit=50")
