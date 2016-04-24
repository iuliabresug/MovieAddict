import PIL
from PIL import Image
import os
path_easy = "C:\Users\Iulia\PycharmProjects\MovieAddict\MovieAddict\EASY"
path_medium = "C:\Users\Iulia\PycharmProjects\MovieAddict\MovieAddict\MEDIUM"
path_hard = "C:\Users\Iulia\PycharmProjects\MovieAddict\MovieAddict\HARD"

list = [path_hard, path_medium, path_easy]
for p in list:
        path = p

        dir = os.listdir(path)
        f = [movie for movie in dir]   #list with all the movies in the chosen level of difficulty folder

        for i in f:
            m = os.path.join(path, i)
            #create the paths to images in the folders
            img1 = os.path.join(m, 'image_1.jpg')
            img2 = os.path.join(m, 'image_2.jpg')

            #set the width to 550 pixels
            basewidth = 550

            i1 = Image.open(img1)
            i2 = Image.open(img2)

            wpercent = (basewidth/float(i1.size[0]))
            hsize = int((float(i1.size[1])*float(wpercent)))
            i1 = i1.resize((basewidth,hsize), PIL.Image.ANTIALIAS)

            wpercent = (basewidth/float(i2.size[0]))
            hsize = int((float(i2.size[1])*float(wpercent)))
            i2 = i2.resize((basewidth,hsize), PIL.Image.ANTIALIAS)

            i1.save(img1)
            i2.save(img2)



