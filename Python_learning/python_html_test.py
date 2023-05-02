from html.parser import HTMLParser


# from .NeoHTMLParser import NeoHTMLParser
class NeoHTMLParser(HTMLParser):
    # def handle_starttag(self, tag, attrs):
    # print("Encounter start:", tag)
    # def handle_endtag(self, tag):
    # print("Encountered an end tag")
    def handle_data(self, data):
        print(data)
        # print("Encounter data: ", data)


tcgPage = open("NeopetsTCGChecklist.html", encoding="utf8")
parser = NeoHTMLParser()
parser.feed(tcgPage.read())
