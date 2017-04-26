__author__ = 'Arkadiusz'

from BeautifulSoup import BeautifulSoup

class ParseConfig():

    # values = []

    def parse(self):
        with open("config.xml") as f:
            content = f.read()

        y = BeautifulSoup(content)
        self.player = y.player.contents[0]
        # self.computer = y.computer.contents[0]

    def getPlayer(self):
        return self.player

    # def getComputer(self):
    #     return self.computer