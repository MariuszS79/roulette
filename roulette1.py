import random
import sys

#what can you bet:
number=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
odd=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
even=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
red=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black=[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
green=[0]
first_column=[1,4,7,10,13,16,19,22,25,28,31,34]
second_column=[2,5,8,11,14,17,20,23,26,29,32,35]
third_column=[3,6,9,12,15,18,21,24,27,30,33,36]
first_eighteen=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
second_eighteen=[19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
first_dozen=[1,2,3,4,5,6,7,8,9,10,11,12]
second_dozen=[13,14,15,16,17,18,19,20,21,22,23,24]
third_dozen=[25,26,27,28,29,30,31,32,33,34,35,36]

starting_balance=1000 #starting amount is 1000 GBP

name=input("Hello gambler. What is your name?")
print ("Hello "+name+". You will get 1000 GBP on the house. \nWith this amount and the roulette you can change your life for better, \nor for worse. Who knows? ;-)")
print("----------")
balance=starting_balance
print(name," you have ",balance,"GBP")
print("Type in bet of your choice by chosing number from 1 to 36\nor one of commands: \nodd, \neven, \nred, \nblack, \ngreen, \nfc for first_column,\nsc for second_column,\ntc for third_column, \nfe for first_eighteen, \nse for second_eighteen, \nfd for first_dozen, \nsd for second_dozen, \ntd for third_dozen")
print("----------")
while True:
  
  while balance==0:
    print("You lost all your money. Time to go home")
    sys.exit("Good bye")
    break

  while balance>0:
    print("Would you like to continue? y means yes and n means no")
    carryon=input("")
    while carryon not in ["y","n"]:
      print("Would you like to continue? y means yes and n means no")
      carryon=input("")
      continue

    while carryon=="y":
      print("Let's carry on ;-)")
      break
    while carryon=="n":
      while balance>1000:
        print("Well done, you won",(balance-starting_balance),"GBP")
        break
      while balance==1000:
        print("You won nothing, at least you lost nothing ;-)")
        break
      while balance<1000:
        print("You lost",(starting_balance-balance),"GBP" )
        break
      sys.exit("Farewell")
    break
      

  choice=input("Choose your bet:")
    
  while choice not in ["odd","even","red","black","green","fc","sc","tc","fe","se","fd","sd","td","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36"]:
    print("Type in proper command")
    choice=input("Chose your bet:")
    continue
  

  bet=int(input("How much are you willing to bet?:"))
  while bet>balance:
    print("You don't have that much.")
    bet=int(input("How much are you willing to bet?:"))
    continue
  print("----------")
  balance=balance-bet
  print(name," you have ",balance,"GBP")
  print("Let's spin the wheel!")
  spin=random.choice(number)
  print("----------")
  print("The wheel stopped and the result is",spin)
  
  def win():
    print("Congratulations, you won!")
    print(name," you have ",balance,"GBP")
    print("----------")
  
  if choice=="odd" and spin in odd:
    bet=bet*2
    balance=balance+bet
    win()
    continue
  
  elif choice=="even" and spin in even:
    bet=bet*2
    balance=balance+bet
    win()
    continue
  
  elif choice=="red" and spin in red:
    bet=bet*2
    balance=balance+bet
    win()
    continue
  
  elif choice=="black" and spin in black:
    bet=bet*2
    balance=balance+bet
    win()
    continue
  
  elif choice=="green" and spin in green:
    bet=bet*18
    balance=balance+bet
    win()
    continue

  elif choice=="fc" and spin in first_column:
    bet=bet*3
    balance=balance+bet
    win()
    continue
  
  elif choice=="sc" and spin in second_column:
    bet=bet*3
    balance=balance+bet
    win()
    continue
  
  elif choice=="tc" and spin in third_column:
    bet=bet*3
    balance=balance+bet
    win()
    continue
  
  elif choice=="fe" and spin in first_eighteen:
    bet=bet*2
    balance=balance+bet
    win()
    continue
  
  elif choice=="se" and spin in second_eighteeen:
    bet=bet*2
    balance=balance+bet
    win()
    continue
  
  elif choice=="fd" and spin in first_dozen:
    bet=bet*3
    balance=balance+bet
    win()
    continue
  
  elif choice=="sd" and spin in second_dozen:
    bet=bet*3
    balance=balance+bet
    win()
    continue
  
  elif choice=="td" and spin in third_dozen:
    bet=bet*3
    balance=balance+bet
    win()
    continue
  
  elif choice==str(spin):
    bet=bet*18
    balance=balance+bet
    win()
    continue

  else:
    print("You lost this time")
    print(name," you have ",balance,"GBP")
    print("----------")
    continue
  
  continue
    