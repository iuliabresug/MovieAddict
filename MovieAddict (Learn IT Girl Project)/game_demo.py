import os
path = "C:\Users\Iulia\PycharmProjects\MovieAddict\MovieAddict\EASY"
import sys
#function for reading the files
def read(filename):
    fh = open(filename)
    print fh.read()
    fh.close()

dir = os.listdir(path)
f = [movie for movie in dir]   #list with all the movies in EASY folder
h = []

#iterating through all movie folders in EASY folder
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
    tips = {'another quote': q2, 'easy image': img1, 'hard image': img2,'fun fact': ff}
    def tip():
        choice = raw_input("Type tip:")
        if choice in tips:
            read(tips[choice])

    #iterating through each file in the specific movie folder
    #display details of the movie
    for film in h:
            print ("What is the movie?\n")
            read (q1)
            print ("Movie details:")
            read (help)
            print ("\nTips: another quote, easy image, hard image, fun fact")
            print ("Type 'guess' to type the movie name or 'i give up' if you give up\n")

            #ask the user to answer or give up
            option = raw_input("Type 'guess' or 'i give up':")
            while True:
               if option == "guess":
                   correct = raw_input("Type the movie name (or: type 'tip' for tip, type 'i give up' if you don't know the movie):")
                   if correct == i:    #guess right
                       print ("Correct\n")
                       read(details)
                       quitnext = raw_input("Quit or next?")
                       #if the user types "next" it goes to the next movie; if "quit" is typed, the game ends
                       if quitnext == 'next':
                           break
                       elif quitnext == 'quit':
                           sys.exit()
                   elif correct == "tip":   #choose a tip
                       tip()

                   #if the guess of the movie is not correct the user can try again, quit or go to the next movie
                   elif correct != "tip" and correct != "i give up":  #guess wrong
                       print ("That's not the movie.")
                       print ("Would you like to try again?")
                       nextmove = raw_input("Type 'try again', 'next' or 'quit':")
                       if nextmove == "try again":
                           continue
                       elif nextmove == "quit":
                           sys.exit()
                       elif nextmove == "next":
                           break
                   elif correct == "i give up":   #give up
                       read(details)
                       quitnext = raw_input("Quit or next?")
                       if quitnext == 'next':
                          break
                       elif quitnext == 'quit':
                          sys.exit()
               elif option == "i give up": #give up
                   read(details)
                   quitnext = raw_input("Quit or next?")
                   if quitnext == 'next':
                       break
                   elif quitnext == 'quit':
                       sys.exit()






