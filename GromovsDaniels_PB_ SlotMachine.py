from time import sleep
from os import system
import random

#Variables
bet = 0
money = 100
slot1 = "P"
slot2 = "A"
slot3 = "Y"
slot1cha = 0
slot2cha = 0
slot3cha = 0
lastbet = 0
notenough = False
prize = 0
notvalue = False

#Display that can get updated
def display():
    print(f"""
money: {money}
bet: {bet}


 ___________
  | SLOTS |
  |=======|
  | {slot1} {slot2} {slot3} |
  |-------|
  |_______|


""")

#Winning animation
def Win():
  for b in range(5):
      system("cls")
      print(f"""
  money: {money}
  bet: {bet}
    >        '
      \\  _      '
  /___________  ~
    | SLOTS |
    |=======| ~
    | {slot1} {slot2} {slot3} |
  . |-------|  
    |_______|
  ~         ,   *

  You won {prize}$
  """)
      sleep(0.5)
      system("cls")
      print(f"""
  money: {money}
  bet: {bet}
      ~       |
  <        '      
   ___________    '
   /| SLOTS |   
    |=======|   ~
    | {slot1} {slot2} {slot3} | ~
    |-------|  
   .|_______|
                
  ~         ,   *
  You won {prize}$
  """)
      sleep(0.5)
      system("cls")
      print(f"""
  money: {money}
  bet: {bet}
    `          
      ~      /    
   ___________    
    | SLOTS |     '
  / |=======|   
    | {slot1} {slot2} {slot3} |   ~
    |-------|  ~
    |_______|
  .        ~      
            
  You won {prize}$
  """)
      sleep(0.5)




#Main loop
while True:
  system("cls")
  display()
  if money <= 0:
    system("cls")
    print("No more money :(")
    break
#money input. If not intiger or money isnt enough a loop starts and ends when the value is acceptable.
  bet = input("what is your bet: ")
  
  if bet == "":
    bet = lastbet
  elif bet.isdigit():
    bet = int(bet)
  else:
    notvalue = True
    print("Use intiger and don't use 0!!!")
    while notvalue == True:
      bet = input("what is your bet: ")

      if bet.isdigit():
        notvalue = False
        bet = int(bet)
      else:
        print("Not intiger")
  if bet > money:
    notenough = True
    print("Not enough")
#input loop if not enough money for the bet you input
    while notenough == True:
      bet = input("what is your bet: ")
      bet = int(bet)
      if bet > money:
        print("Not enough")
      else:
        notenough = False
  bet = int(bet)
  money -= bet
  input("SPIN")

#Rolling animation that also generates the numbers
  for a in range(30):
    system("cls")
    slot1cha = random.randint(1,15)
    slot2cha = random.randint(1,15)
    slot3cha = random.randint(1,15)

#Changes the chance of rolling to the number 
    if slot1cha in (1,2,3,4,5):
      slot1 = 1
    elif slot1cha in (6,7,8,9):
      slot1 = 2
    elif slot1cha in (10,11,12):
      slot1 = 3
    elif slot1cha in (13,14):
      slot1 = 4
    elif slot1cha == 15:
      slot1 = 5

    if slot2cha in (1,2,3,4,5):
      slot2 = 1
    elif slot2cha in (6,7,8,9):
      slot2 = 2
    elif slot2cha in (10,11,12):
      slot2 = 3
    elif slot2cha in (13,14):
      slot2 = 4
    elif slot2cha == 15:
      slot2 = 5

    if slot3cha in (1,2,3,4,5):
      slot3 = 1
    elif slot3cha in (6,7,8,9):
      slot3 = 2
    elif slot3cha in (10,11,12):
      slot3 = 3
    elif slot3cha in (13,14):
      slot3 = 4
    elif slot3cha == 15:
      slot3 = 5
    display()
    sleep(0.1)
  

  #Checks if first 2 numbers are the same and if true then multiplies ur bet
  if slot1 == slot2:
    if slot1 == 1:
      prize += bet * 0.5
    elif slot1 == 2:
      prize += bet * 1
    elif slot1 == 3:
      prize += bet * 1.5
    elif slot1 == 4:
      prize += bet * 2
    elif slot1 == 5:
      prize += bet * 2.5
    money += prize
    Win()
    system("cls")
    display()
    
  #Checks if all numbers are the same and if true then multiplies ur bet 
  elif slot1 == slot2 == slot3:
    if slot1 == 1:
      prize += bet * 1
    elif slot1 == 2:
      prize += bet * 2
    elif slot1 == 3:
      prize += bet * 3
    elif slot1 == 4:
      prize += bet * 4
    elif slot1 == 5:
      prize += bet * 10
    money =+ prize
    Win()
    system("cls")
    display()
  #If none are true that means they are not the same, so you get nothing.
  else:
    print("You got nothing.")
  lastbet = bet
  input("Press ENTER to continue  ")
