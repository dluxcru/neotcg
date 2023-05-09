from bs4 import BeautifulSoup
import requests
##The orginal Neopets JS code for opening a card.
#function showCard(EDID, CARDID) {
				# window.open("displayCard.phtml?edid=" + EDID + "&id=" + CARDID, "CardDisplay", "width=300, height=420, location=no, status=no");
			# };
from Python_learning.Card import Card
from Python_learning.TableCrawler import TableCrawler

with open("NeopetsTCGChecklist.html", "r", encoding="utf-8") as neotcg:
    doc = BeautifulSoup(neotcg, "html.parser")

tables = TableCrawler(doc)
tables.crawl()




