'''x = 1
while not x == 10:          # Addig megy a ciklus ujra meg ujra,ameddig x nem lesz 10. Utána leáll!
    print("x értéke:  ", x)
    x += 1
print("És mostmár ", x)     # Elszámoltunk 9 ig. Igy már kiirathatjuk az x értékét ami 10 lesz!
        
'''




# Gondoltam egy számra.. lvl.2 --> több probálkozás!
'''
attempt = 0
number  = 14
guess   = int(  input("T.Henry\'s kit number?..  ")  )

while not guess == number:
    attempt += 1
    print(" Nahhh..Try again!")
    print(  str("attempts: "), int(attempt), str("\n------------------------------")  )
    guess   = int(  input("T.Henry\'s kit number?..  ")  )
    
print(" Cool! U got it ;)" )
'''


# Printeld ki a számok hatványait 1 től 100 ig.
'''
x = 1
while not x == 101:
    print(x, "hatványa ---> ", x**2)
    x += 1
'''


# Printeld ki a 100 alatti páros természetes számokat.
'''
x = 0
while not x == 100:
    x += 1
    if x % 2 == 0:
        print( x )
'''        
        # vagy egy másik megoldás
        
'''        
x = 0
while x < 100:
    print (x)
    x += 2
'''

# Ird ki az összes 3 jegyű páratlan számot.
'''
x = 101
while 100 < x < 1000:
    print(x)
    x += 2
'''

# Irj egy programot ami addig kérdezi "szeretsz e" amig igennel nem válaszolsz.
'''
answer = None    
while not answer == "y":
    answer = input(" Do you love me?     (y/n)"   )
print( " Thats my babe :) ")
'''


#Kérj 2 számot, majd printeltesd ki a közte lévő számokat!
'''
no_1 = int(  input(" Mettől meddig számoljak el? add meg az első számot:  ")  )
no_2 = int(  input(" Add meg a második számot:  ")  )
#x = no_1
while no_1 <= no_2:
    print(no_1)
    no_1 += 1
'''

# Most kérdezze meg hányasával számoljon.
'''
no_1 = int(  input(" Mettől meddig számoljak el? add meg az első számot:  ")  )
no_2 = int(  input(" Add meg a második számot:  ")  )
ask  = int(  input(" Hányasával számoljak?  ")  )

while no_1 <= no_2:
    print(no_1)
    no_1 += ask
'''    

#Kérdezze meg hanyadik hatványát tüntesse fel a szám mellett.
'''
no_1   = int(  input(" Mettől meddig számoljak el? add meg az első számot:  ")  )
no_2   = int(  input(" Add meg a második számot:  ")  )
ask_1  = int(  input(" Hányasával számoljak?  ")  )
ask_2  = int(  input(" Hányadik hatványát írja a szám mellé?  ")  )
while no_1 <= no_2:
    print(no_1, no_1**ask_2)
    no_1 += ask_1
'''

#Ismét gondoltunk egy számra. Most viszont a 3.próbálkozás után legyen game over és legyen vége a programnak.
'''
attempt = 0
number  = 14
guess   = int(  input("T.Henry\'s kit number?..  ")  )

while not guess == number:
    attempt += 1
    print(" Nahhh..Try again!")
    print(  str("attempts: "), int(attempt), str("\n------------------------------")  )
    guess   = int(  input("T.Henry\'s kit number?..  ")  )
    if attempt == 2:
        print(" Your knowledge is shit..We gotta say goodbye!")
        import sys
        sys.exit(0)                # importáltam a sys könyvtárat,h letudjam állítani a programot.
print(" Cool! U got it ;)" )
'''

#Másik megoldás + reakciók + segítség hiba esetén:

number  = 14
success = False
attempt = 0

while not success and attempt <= 2:   # amig nem lesz success True és a próbálozások nem haladják meg a 3 at addíg ismétlődik a program.
    guess   = int(  input("Which number I guessed between 1-20?   ")  )
    attempt += 1                      # Looponként növeljük az értékét 1-el!
    if guess == number:               # Ha a guess és a number megegyezik akkor...
        success = True                # Success True lesz! és így megtörik a feltétel miszerint False.
        print(" Nice..;)")
    if guess != number:
        print(" The difference is:  ", abs(guess - number)  )  # abs function = abszolut érték. Ez lesz az eltérés a két szám között.
    if guess < number:
        print(" It\'s too short..try again..")
    if guess > number:
        print(" It\'s too much..try again..")
    if guess != number and attempt > 2:
        print(" Sorry but you failed..")
