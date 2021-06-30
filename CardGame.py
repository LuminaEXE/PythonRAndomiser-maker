import random
ABCINT = input("1 = Rules!/ 2 = play")
if int(ABCINT) == 1:
  print(
    "Hop into a discord call and share screens dont check others cards the person who draws the card with a greater no wins the round 'CARD' must be said to win the game also u can add cards to make it more op the elemnt is randomly genrated5 cant be added There is an adding pattern: 1 -> 2 3 -> 4 enjoy :)")
if int(ABCINT) == 2:
  #Card No. Gen
  Card1Gen =  random.randrange (1, 5, 2)
  Card2Gen =  random.randrange (1, 5, 2)
  Card3Gen =  random.randrange (1, 5, 2)
  Card4Gen =  random.randrange (1, 5, 2)
  Card5Gen =  random.randrange (1, 5, 2)
    
  #CardElementGen
  CardEleme1 = random.randrange(1, 3,)
  CardEleme2 = random.randrange(1, 3,)
  CardEleme3 = random.randrange(1, 3,)
  CardEleme4 = random.randrange(1, 3,)
  CardEleme5 = random.randrange(1, 3,)

  if CardEleme1 == 1:
    CardEleme1 = "Water"
    
  if CardEleme1 == 3:
    CardEleme1 = "Earth"     
  else:
  if CardEleme1 == 2:
   CardEleme1= "Fire"

  if CardEleme2 == 1:
    CardEleme2 = "Water"
    
  if CardEleme2 == 3:
    CardEleme2 = "Earth"     
  else:
  if CardEleme2 == 2:
    CardEleme2 = "Fire"

  if CardEleme3 == 1:
    CardEleme3 = "Water"
    
  if CardEleme3 == 3:
    CardEleme3 = "Earth"     
  else:
  if CardEleme3 == 2:
    CardEleme3= "Fire"

  if CardEleme4 == 1:
    CardEleme4 = "Water"
    
  if CardEleme4 == 3:
    CardEleme4 = "Earth"     
  else:
  if CardEleme4 == 2:
    CardEleme4= "Fire"

  if CardEleme5 == 1:
    CardEleme5 = "Water"
    
  if CardEleme5 == 3:
    CardEleme5 = "Earth"     
  else:
   if CardEleme5 == 2:
    CardEleme5= "Fire"



  print(Card1Gen)
  print( CardEleme1)
  print(Card2Gen)
  print(CardEleme2)

  print(Card3Gen)
  print(CardEleme3)
  print(Card4Gen)
  print(CardEleme4)
  print(Card5Gen)
  print(CardEleme5)
  print("Add Cards before start")
  Group1 = input("1/2/3/4/5   :")
  Group2 = input("1/2/3/4/5   :")
  if int(Group1) == 1:
  if int(Group2) == 2:
    CardElmeRandDecider1 = CardEleme1
    CardElmeRandDecider2 = CardEleme2
    CardElemeDecider = random.randrange(1,2)
    Group1and2 = Card1Gen + Card2Gen
    print(Group1and2)
    
    if CardElemeDecider == 1:
      print(CardElmeRandDecider1)
    else:
      print(CardElmeRandDecider2)
      
  
  
      
  if int(Group1) == 3:
  if int(Group2) == 4:
    CardElmeRandDecider3 = CardEleme3
    CardElmeRandDecider4 = CardEleme4
    CardElemeDecider = random.randrange(1,2)
    Group1and2 = Card1Gen + Card2Gen
    print(Group1and2)
    
    if CardElemeDecider == 1:
      print(CardElmeRandDecider3)
    else:
      print(CardElmeRandDecider4)
      
  
  
      
