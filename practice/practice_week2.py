def mentee (name, age):
    print ("Name: "), name
    print ("Age: "), age
    return;
mentee (name="Iulia", age = 24)
score = int(raw_input("Enter score: "))
if score > 9 and score <= 10:
 print ("A")
elif score > 8 and score <= 9:
 print ("B")
elif score > 7 and score <= 8:
 print ("C")
elif score > 5 and score <= 7:
 print ("D")
elif score <= 5 and score >= 0:
 print ("fail")
else:
    print ("You entered an invalid score.")
    list = [0,1,2,3,4,5,6,7,8,9,10]
    list.reverse()
    print ("Enter one of this values"), list
