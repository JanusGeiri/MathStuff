import pandas as pd
import requests
import lxml.html as lh
import certifi
from bs4 import BeautifulSoup

url = 'https://tandur.3cxhysing.sip.is/management/Reports/Daglegsk%C3%BDrsla_0110_WPHAgAxEOBwMeXtxvhZn.html'
page = requests.get(url, verify=False)

text = page.text
i = text.find('Total:</td>')
print(i)
