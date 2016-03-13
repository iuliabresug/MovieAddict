#read sentences from a text file and show them to the user one by one
quote = open('quote.txt')
ls = quote.readlines()
count = 1
for i in range(len(ls)):
  if raw_input() == (" "):
      if count <(len(ls)):
           j = ls[count]
           count = count + 1
           j = j.rstrip()
           print j
