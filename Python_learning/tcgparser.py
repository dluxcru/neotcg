from bs4 import BeautifulSoup
import requests



#TODO: Github Repo

##The orginal Neopets JS code for opening a card.
#function showCard(EDID, CARDID) {
				# window.open("displayCard.phtml?edid=" + EDID + "&id=" + CARDID, "CardDisplay", "width=300, height=420, location=no, status=no");
			# };
def showCard(edID, cardID):
    #TODO: find proper request url. Missing directory path to `displayCard.phtml`.
    # Also determine if this will send an html response to a script. May require workarounds.
    requestUrl =  "http://www.neopets.com/displayCard.phtml?edid=" + str(edID) + "&id=" + str(cardID)
    return requestUrl

with open("NeopetsTCGChecklist.html", "r", encoding="utf-8") as neotcg:
    doc = BeautifulSoup(neotcg, "html.parser")

# print(doc.prettify())
tables = doc.find_all("table")
table = doc.find(style="border:1px solid #000000;")

# row = table.tbody.find_all("tr")[1]
# print(row.td)
## load the rows and delete the first row of junk data.
rows = table.tbody.find_all("tr")
del rows[0]
## iterate over rows
for row in rows:
    # print(row)
    # print(row.find_all("td")[0])
    row_cells = row.find_all("td")
    card_id = row_cells[0].string
    card_name= row_cells[1].a.strong.string
    card_rarity = row_cells[2].string
    rowCard = Card(card_id, 1, card_name)
    print(rowCard)

# print(table.tbody)


