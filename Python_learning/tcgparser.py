import ssl

from bs4 import BeautifulSoup
import requests
##The orginal Neopets JS code for opening a card.
#function showCard(EDID, CARDID) {
				# window.open("displayCard.phtml?edid=" + EDID + "&id=" + CARDID, "CardDisplay", "width=300, height=420, location=no, status=no");
			# };
from Python_learning.Card import Card
from Python_learning.NetworkHelpers.NeoTLSConnector import NeoTLSConnector
from Python_learning.TableCrawler import TableCrawler

with open("NeopetsTCGChecklist.html", "r", encoding="utf-8") as neotcg:
    doc = BeautifulSoup(neotcg, "html.parser")

# tables = TableCrawler(doc)
# tables.crawl()

wandConfusion = Card(232, 1, "Wand of Confusion", "R")
print(ssl.OPENSSL_VERSION)

# session = requests.Session()
# session.verify = False
# session.mount("https://", NeoTLSConnector())
#
# response = session.get(wandConfusion.showCard())
# session = requests.Session()
# session.verify = False
# session.mount("https://", requests.adapters.HTTPAdapter(pool_connections=1, pool_maxsize=1, max_retries=3, pool_block=False, ssl_version=ssl.PROTOCOL_TLSv1_2))
#
# response = session.get(wandConfusion.showCard())

r = requests.get(wandConfusion.showCard(),verify=False)
print(r.url)


