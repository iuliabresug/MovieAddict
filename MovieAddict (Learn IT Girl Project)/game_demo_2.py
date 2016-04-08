import os
path_easy = "C:\Users\Iulia\PycharmProjects\MovieAddict\MovieAddict\EASY"
path_medium = "C:\Users\Iulia\PycharmProjects\MovieAddict\MovieAddict\MEDIUM"
path_hard = "C:\Users\Iulia\PycharmProjects\MovieAddict\MovieAddict\HARD"
import sys

#function for reading the files
def read(filename):
    fh = open(filename)
    print fh.read()
    fh.close()

#loop fo choosing a level of difficulty
while True:
    choose_level = raw_input("Choose a level:easy('e'), medium('m'), hard('h'):")
    if choose_level == "e":
        path = path_easy
        break
    elif choose_level == 'm':
        path = path_medium
        break
    elif choose_level == "h":
        path = path_hard
        break
    else:
        print ("Type 'e', 'm' or 'h'.")
        continue

dir = os.listdir(path)
from random import shuffle     #choose movie names randomly
f = [movie for movie in dir]   #list with all the movies in the chosen level of difficulty folder
shuffle(f)
h = []
#iterating through all movie folders in the folder
for i in f:
    #create the paths for the movie folders
    m = os.path.join(path, i)
    #create the paths to all the files in the folders
    q1 = os.path.join(m, 'quote_1.txt')
    q2 = os.path.join(m, 'quote_2.txt')
    img1 = os.path.join(m, 'image_1.jpg')
    img2 = os.path.join(m, 'image_2.jpg')
    ff = os.path.join(m, 'funfact.txt')
    details = os.path.join(m, 'details.txt')
    imdb = os.path.join(m, 'imdblink.txt')
    help = os.path.join(m, 'help.txt')
    rt = os.path.join(m, 'rtlink')

    #list with all files
    g = [m, q1, q2, img1, img2, ff, details, imdb, rt]

    #list of lists with files for each folder
    h.append(g)

    #dictionary and function for the tips
    tips = {'q': q2, 'i': img1, 'j': img2,'f': ff}
    def tip(answer):
        if answer in tips:
            read(tips[answer]) #urmeaza sa fie facuta functionala si pentru imagini

    #iterating through each file in the specific movie folder
    for film in h:
            print ("What is the movie?\n")
            read (q1)
            print ("Movie details:")
            read (help)
            print ("\nTips: another quote(type 'q'), easy image(type'i'), hard image(type 'j'), fun fact(type 'f')")
            print ("Type the movie name or 'u' if you give up\n")
            while True:
               answer = raw_input("Guess:")
               answer = answer.lower()
               if answer == i:  #if the answer is correct it shows the movie details
                   print ("Correct\n")
                   read(details)
                   break
               elif answer in tips: #shows tip
                   tip(answer)
                   continue
               elif answer == "u": #if the answer is give up it shows the movie details
                   read(details)
                   break
               else:  #else for exceptional input and show help screen
                   print ("That's not the movie\n")
                   print ("If you don't know it you can call a tip. \n('q' for a quote, 'i' for an easy image, 'j' for a hard image or 'f' for the fun fact.")
                   print ("If you give up just type 'u' and go to the next question or quit.\n")
                   yesno = raw_input("Would you like to try again?\nType 'no' if you don't want to or any key to try again.")
                   if yesno == "no":  #ask the user if he wants to type again the movie name
                       break
                   else:
                       continue
            #choosing what to do next: quit or to display the next question
            while True:
                donext = (raw_input("Next question('n') or quit('q')?"))
                if donext == "n":
                    break
                elif donext == "q":
                    sys.exit()
                else:
                    print ("Type 'n' for the next question or 'q' to quit the game")
