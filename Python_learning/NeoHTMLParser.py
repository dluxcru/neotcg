class NeoHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Ecounter start:", tag)
    def handle_endtag(self, tag):
        print("Encountered an end tag")
    def handle_data(self, data):
        print("Encounter data: ", data)