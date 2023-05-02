# dragons = ["Hikari", "Kyra", "Krianna", "Kariel", "Zaria"]
# for dragon in dragons:
#     print(dragon)
#     if dragon == "Kariel":
#         break

from html.parser import HTMLParser


def formatter(text):
    test_format = "{} : {}"
    return test_format.format(type(text), text)

# x = 10
# print(formatter(x))

# x = str(11)
# print(formatter(x))

# print(open("NeopetsTCGChecklist.html").readline())
tcgPage = open("NeopetsTCGChecklist.html")

# tcgContents = tcgPage.read()
class NeoHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Ecounter start:", tag)
    def handle_endtag(self, tag):
        print("Encountered an end tag")
    def handle_data(self, data):
        print("Encounter data: ", data)
parser = NeoHTMLParser()
parser.feed(tcgPage.read)
