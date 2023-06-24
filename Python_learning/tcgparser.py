import ssl
import requests
import html


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


from Python_learning.Card import Card
from Python_learning.NetworkHelpers.NeoTLSConnector import NeoTLSConnector
from Python_learning.TableCrawler import TableCrawler

"""The orginal Neopets JS code for opening a card.
function showCard(EDID, CARDID) {
				 window.open("displayCard.phtml?edid=" + EDID + "&id=" + CARDID, "CardDisplay", "width=300, height=420, location=no, status=no");
			 };
"""

with open("NeopetsTCGChecklist.html", "r", encoding="utf-8") as neotcg:
    doc = BeautifulSoup(neotcg, "html.parser")

# tables = TableCrawler(doc)
# tables.crawl()

wandConfusion = Card(232, 1, "Wand of Confusion", "R")

# r = requests.get(wandConfusion.showCard(), verify=False)
# # print(r.url)
# # print(r.text)
# cardHTML = r.text
# formatted = html.escape(cardHTML)
# # print(cardHTML)
## Code Base: https://www.youtube.com/watch?v=SPM1tm2ZdK4
options = Options()
options.add_experimental_option("detatch", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(wandConfusion.showCard())

