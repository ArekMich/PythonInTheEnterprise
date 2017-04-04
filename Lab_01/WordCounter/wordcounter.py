import logging

logging.getLogger('example')
logging.basicConfig(filename='logfile.log', level=logging.DEBUG)

class WordCounter:
    def __init__(self):
        self.num_lines = 0
        self.num_words = 0
        self.num_chars = 0
        logging.info('Inicjalizacja zmiennych sluzacych do zliczania')

    def ReadFile(self,FILE):
         with open(FILE, 'r+') as f:
             for line in f:
                 words = line.split()

                 self.num_lines += 1
                 self.num_words += len(words)
                 self.num_chars += len(line)
         logging.debug("DEBUG: Zliczylo zmienne")

    def Print(self):
        print "Ilosc lini: ", self.num_lines
        print "Ilosc slow: ", self.num_words
        print "Ilosc znakow: ", self.num_chars

        logging.warn('Wyswietlono zmienne')


counter= WordCounter()
counter.ReadFile("tekst.txt")
counter.Print()
del counter

logging.error("ERROR: mamy peoblem")
logging.warning("Ostrzezenie")
