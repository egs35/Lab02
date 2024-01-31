#Example 3.1
sh = input("Enter Hours: ") #string hours
sr = input("Enter Rate: ") #string rate
fh = float(sh) #float hours
fr = float(sr) #float rate
#print(fh, fr)
if fh > 40:
    print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * .5)
    xp = reg + otp #total pay
else:
    print("Regular")
xp = fh * fr
print("Pay: ", xp)

#Example 3.2
sh = input("Enter Hours: ") #string hours
sr = input("Enter Rate: ") #string rate
try: 
    fh = float(sh) #float hours
    fr = float(sr) #float rate
except:
    print("Error, please enter numeric input")
    quit()

#print(fh, fr)
if fh > 40:
    print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * .5)
    xp = reg + otp #total pay
else:
    print("Regular")
xp = fh * fr
print("Pay: ",xp)

#Example 5.1
num = 0 #running count
tot = 0.0 #running total
while True:
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    #print(fval)
    num = num + 1
    tot = tot + fval

#print('ALL DONE')
print(tot, num, tot/num)

#Strings, Files, Lists and the Guardian Pattern (Chapter 8) Example
#I don't have the files that Mr. Chuck Severance is using so cannot run the code on my own :/

#Dictionary Chapter 9
fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    #print(line)
    wds = line.split()
    #print(wds)
    for w in wds: 
       di[w] = di.get(w,0) + 1
       #print(w,'new', di[w])
        #print('**',w,di,get(w,-99)), this following code does same thing as lines 72 and 73
       #oldcount = di.get(w,0)
        #print(w,'old',oldcount)
        #newcount = oldcount + 1
        #di[w] = newcount
       
        #this code does same thing as this^, just different methods
        #if w in di : 
        #    di[w] = di[w] + 1
        #    print('**EXISTING**')
        #else:
        #    di[w] = 1
        #   print('**NEW**')
        #print(w, di[w])

    print(di)

    #find most common word
    largest = -1
    for k,v in di.items() :
        #print(k,v)
        if v > largest:
            largest = v
            theword = k 

    print(theword, largest)

#Project 2 - Number guessing game
import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")


