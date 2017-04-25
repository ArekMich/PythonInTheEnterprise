import logging

module_logger = logging.getLogger('wc_app')

logging.getLogger('logger')
logging.basicConfig(filename='logfile.log', level=logging.DEBUG)

class NoSuchFile(Exception):
    def __init__(self,message):
        print message

class WordCounter:
    def __init__(self):
        self.num_lines = 0
        self.num_words = 0
        self.num_chars = 0
        module_logger.info("INITIALIZATION")

    def ReadFile(self,FILE):
        try:
            with open(FILE, 'r+') as f:
                 for line in f:
                     words = line.split()

                     self.num_lines += 1
                     self.num_words += len(words)
                     self.num_chars += len(line)
                     module_logger.info("OPEN FILE")
        except:
            raise NoSuchFile("NO SUCH FILE")
            module_logger.error("exit")
        finally:
            pass

    def Print(self):
        print "Ilosc lini: ", self.num_lines
        print "Ilosc slow: ", self.num_words
        print "Ilosc znakow: ", self.num_chars


counter= WordCounter()
counter.ReadFile("tekst.txt")
counter.Print()
del counter

module_logger.info("INFO: ...  module_logger")
module_logger.debug("DEBUG: ... module_logger")
module_logger.error("ERROR: ... module_logger")
module_logger.warning("WARNING: ... module_logger")

logging.info("INFO: ...  logging")
logging.debug("DEBUG: ... logging")
logging.error("ERROR: ... logging")
logging.warning("WARNING: ... logging")


