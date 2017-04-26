import os.path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.transforms as mtransforms
import matplotlib.text as mtext


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





class MyLine(lines.Line2D):
    def __init__(self, *args, **kwargs):
        # we'll update the position when the line data is set
        self.text = mtext.Text(0, 0, '')
        lines.Line2D.__init__(self, *args, **kwargs)

        # we can't access the label attr until *after* the line is
        # inited
        self.text.set_text(self.get_label())

    def set_figure(self, figure):
        self.text.set_figure(figure)
        lines.Line2D.set_figure(self, figure)

    def set_axes(self, axes):
        self.text.set_axes(axes)
        lines.Line2D.set_axes(self, axes)

    def set_transform(self, transform):
        # 2 pixel offset
        texttrans = transform + mtransforms.Affine2D().translate(2, 2)
        self.text.set_transform(texttrans)
        #lines.Line2D.set_transform(self, transform)

    def set_data(self, x, y):
        if len(x):
            self.text.set_position((x[3], y[3]))

        lines.Line2D.set_data(self, x, y)

    def draw(self, renderer):
        # draw my label at the end of the line with 2 pixel offset
        lines.Line2D.draw(self, renderer)
        self.text.draw(renderer)


fig, ax = plt.subplots()
x, y = np.random.rand(2, 20)
line = MyLine(x, y, mfc='red', ms=12, label=name)
#line.text.set_text('line label')
line.text.set_color('red')
line.text.set_fontsize(16)


ax.add_line(line)


plt.show()
