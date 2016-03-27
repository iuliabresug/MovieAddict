import os
path = "C:\Users\Iulia\PycharmProjects\MovieAddict\MovieAddict\EASY"
import sys
def read(filename):   #function for reading the files
    fh = open(filename)
    print fh.read()
    fh.close()

dir = os.listdir(path)
f = [movie for movie in dir]   #list with all the folders in EASY (the movies)
h = []
for i in f:
    m = os.path.join(path, i)  #created the paths for the movie folders
    q1 = os.path.join(m, 'quote_1.txt')
    q2 = os.path.join(m, 'quote_2.txt')
    img1 = os.path.join(m, 'image_1.jpg')
    img2 = os.path.join(m, 'image_2.jpg')
    ff = os.path.join(m, 'funfact.txt')
    details = os.path.join(m, 'details.txt')
    imdb = os.path.join(m, 'imdblink.txt')
    help = os.path.join(m, 'help.txt')
    rt = os.path.join(m, 'rtlink')   #paths to all the files in the folders
    g = [m, q1, q2, img1, img2, ff, details, imdb, rt]
    h.append(g) #list of lists of files in each folder

    tips = {'another quote': q2, 'easy image': img1, 'hard image': img2,'fun fact': ff}
    for film in h:    #indentation for going to the next movie
        if raw_input("Type start to start the game:") == 'start':
            print ("What is the movie?\n")
            read (q1)
            print ("Movie details:")
            read (help)
            print ("\nChoose a tip: another quote, easy image, hard image, fun fact")
            print ("Type 'guess' to type the movie name or 'i give up' if you give up\n")
            option = raw_input("Guess or give up:")
            while True:
               if option == "guess":
                   correct = raw_input("Guess the movie (or type 'tip' for tip):")
                   if correct == i:    #guess right
                       print ("Correct\n")
                       read(details)
                       quitnext = raw_input("Quit or next?")
                       if quitnext == 'next':
                           break
                       elif quitnext == 'quit':
                           sys.exit()
                   elif correct == "tip":   #choose a tip
                       choice = raw_input("Type tip:")
                       if choice in tips:
                           read(tips[choice])
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

