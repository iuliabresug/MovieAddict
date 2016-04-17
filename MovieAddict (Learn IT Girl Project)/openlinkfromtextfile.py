import os
path = "C:\Users\Iulia\PycharmProjects\MovieAddict\MovieAddict\EASY"
import sys

#function for reading the files USING RETURN
def read(filename):
    fh = open(filename)
    return fh.read()

dir = os.listdir(path)
from random import shuffle     #choose movie names randomly
f = [movie for movie in dir]   #list with all the movies in the chosen level of difficulty folder
shuffle(f)
h = []
#iterating through all movie folders in the folder
for i in f:
    #create the paths for the movie folders
    m = os.path.join(path, i)

    imdb = os.path.join(m, 'imdblink.txt')

import webbrowser
k = read(imdb)
print k
webbrowser.open(k)