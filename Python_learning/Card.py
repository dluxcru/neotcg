class Card():
    cardID = 0
    edID = 0
    rarity = "N"
    name = "None"
    tags = "None"
    ruleText = "None"
    descText = "None"
    strength = 0
    agility = 0
    magic = 0
    intelligence = 0
    def __init__(self, cardID, edID, name):
        self.cardID = cardID
        self.edID = edID
        self.name = name
        # self.tags = tags
        # self.ruleText = ruleText
        # self.descText = descText
        # self.strength = strength
        # self.agility = agility
        # self.magic = magic
        # self.intelligence = intelligence
    def __str__(self):
        return f"{self.cardID} {self.name}"


