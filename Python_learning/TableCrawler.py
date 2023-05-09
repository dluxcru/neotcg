from bs4 import BeautifulSoup

from Python_learning.Card import Card


class TableCrawler():
    def __init__(self, document):
        self.doc = document

    def crawl(self):
        tables = self.doc.find_all("table")
        table = self.doc.find(style="border:1px solid #000000;")
        ## load the rows and delete the first row of junk data.
        rows = table.tbody.find_all("tr")
        del rows[0]
        ## iterate over rows
        for row in rows:
            row_cells = row.find_all("td")
            card_id = row_cells[0].string
            card_name = row_cells[1].a.strong.string
            card_rarity = row_cells[2].string
            rowCard = Card(card_id, 1, card_name, card_rarity)
            print(rowCard)
            print(rowCard.showCard())
