import os.path

class NotSuchFile(Exception):
    pass


class InputFileValidator:
    def validator(self,name_file):
        my_File= os.path.abspath("/home/arek/PycharmProjects/Lab_1/" + name_file)
        if os.path.isfile(my_File):
            True
        else:
            raise NotSuchFile("No Such File")




class LogParser:
    def __init__(self):
        self.val=InputFileValidator()


    def searchString(self,nameFile,str_search):

        self.val.validator(nameFile)

        file = open(nameFile, 'r')
        lines = file.readlines()
        file.close()

        fileResult = open("Wyniki.txt", 'a')

        countYES=0
        num=0
        list = []

        for num, line in enumerate(lines,1):
            answer = line.find(str_search)
            if(answer==0):
                countYES +=1
                list.append(num)


        print ("Przeszukiwany plik: {} ".format(nameFile) )
        print ("Po zliczeniu: {} ".format(countYES))
        print ("Tab[numer_linii]: {}".format(list))
        print "__________________________________________________________________"

        fileResult.write("Przeszukiwany plik: {} \n".format(nameFile))
        fileResult.write("Po zliczeniu: {} \n".format(countYES))
        fileResult.write("Tab[numer_linii]: {} \n".format(list))
        fileResult.write("__________________________________________________________________ \n")

        fileResult.close()


#__________________MAIN______________________

parser= LogParser()

name=[]
name.append('baseline_BdJPsiKs_MagD.log')
name.append('DR_BdJPsiKs_MagD_1k.log')
name.append('DR_NE_BdJPsiKs_MagD.log')
name.append('DR_NE_BdJPsiKs_MagD_1k.log')

search_str = 'PrChecker.Downs'

parser.searchString(name[0],search_str)
parser.searchString(name[1],search_str)
parser.searchString(name[2],search_str)
parser.searchString(name[3],search_str)



