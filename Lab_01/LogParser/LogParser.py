import os.path

class NotSuchFile(Exception):
    pass


class InputFileValidator:
    def validator(self,name_file):
        my_File= os.path.abspath("/home/arek/PycharmProjects/Lab_1/" + name_file)
        if os.path.isfile(my_File):
            True
        else:
            raise NotSuchFile




class LogParser:
    def __init__(self):
        self.val=InputFileValidator()


    def main(self,str_name,str_search):

        self.val.validator(str_name)

        file = open(str_name, 'r')
        lines = file.readlines()
        file.close()


        countYES=0
        num=0
        list = []

        for num, line in enumerate(lines,1):
            answer = line.find(str_search)
            if(answer==0):
                countYES +=1
                list.append(num)


        print ("Przeszukiwany plik: {} ".format(str_name) )
        print ("Po zliczeniu: {} ".format(countYES))
        print ("Ilosc lini: {}".format(list))
        print "__________________________________________________________________"


#__________________MAIN______________________

parser= LogParser()

name=[]
name.append('baseline_BdJPsiKs_MagD.log')
name.append('DR_BdJPsiKs_MagD_1k.log')
name.append('DR_NE_BdJPsiKs_MagD.log')
name.append('DR_NE_BdJPsiKs_MagD_1k.log')

search_str = 'PrChecker.Downs'
ile=name.__len__()



parser.main(name[0],search_str)
parser.main(name[1],search_str)
parser.main(name[2],search_str)
parser.main(name[3],search_str)



