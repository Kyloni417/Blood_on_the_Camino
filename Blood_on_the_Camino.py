def playagain():
    answer = input("Play again? yes or no... ")
    if answer == "yes":
        print("Buen Camino...")
        beginning()
    
    elif answer == "no":
        print("Buen Camino loser!")

def beginning():
  print("\n ------------    Blood on the Camino    ------------------")
  print("\n The year is 2052, you are traveling through France. \n ") 
  print("You end up in a small village just on the border of Spain called Saint Jean Pied de Port \n")
  print("You wander through the town until you come across a mysterious monk in a robe. \n")
  name = input("He looks up and asks you, 'what is your name?' " )
  print("-------------------------------------------------------------------------------------------------------------------------------")
  print(f"\n Greetings {name}, you look like you have come from far away. Would you be interested in doing the Camino de Santiago? \n \n It is an ancient pilgrimage, but these days it is very dangerous due to corruption.")
  start = input("\n Monk: 'Is it a yes or is it a no?' ")
  if start == 'yes':
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print(f" \n Monk: 'A wise choice you have made {name}!' \n ")
      print("You begin the Camino de Santiago, going over his warnings about the journey. \n ")
      print("After a few hours of walking, you come up to a fork in the road, and remember something the Monk said,")
      print("'the hill is faster, but is very treacherous.  And the path is easier, but swarming with criminals \n ")
      direction = input("Will you risk it on the hill?  Or will you play it safe with the path? ")
  else:
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n You don't do the Camino de Santiago.  One year later, to the day, you drown in a kiddie pool, and go to hell")
      print(" \n Buen Camino loser. The End. \n ")
      playagain()

  if direction == 'path':
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n You take the path, and it is a very lovely walk for a while.")
      print("\n After some time peacefully walking, you hear some screams coming from up the path!")
      print("\n There are three thugs surrounding a poor helpless merchant \n ")
      choice1 = input(" The man is screaming for anyone to help. You can see the thugs have weapons. Do you help? ")
  elif direction == 'hill':
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n You brave it with the hill.")
      print("\n It starts out fine at first, but then quickly you realize you're in over your head.")
      print("\n You lose your footing, snap both of your legs, and parish from starvation.")
      print("\n Also, you didn't finish the Camino, so you went to hell.")
      print("\n Buen Camino loser. The End. \n ")
      playagain()
  else: 
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n You didn't choose 'hill' or 'path', you never make a choice, and then you die and go to hell.")
      print("\n Buen Camino loser. The End. \n ")
      playagain()

  if choice1 == 'yes':
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n You bravely stop and confront the thugs. They turn their attention to you and quickly swarm you.")
      print("\n They quickly put an end to your life")
      print("\n All goes black, but you wake up in heaven!")
      print("\n Buen Camino loser. The End \n ")
      playagain()
  else:
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n You don't have any weapons, so you put your head down and ignore the scene, leaving the helpless man behind.")
      print("\n You walk for a while, feeling guilty, until you arrive at an albergue. You spend the night recovering from a long day.")
      print("\n You spend the next three days walking before you come to a town that looks very poor, but the people seem nice")
      print("\n You know that there is a city further ahead, but you are getting tired. \n")
      choice2 = input("Do you stay at the town, or do you continue to the city? ")
  if choice2 == 'city':
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n You continue to the city even though you are very tired. The thugs from earlier catch up to you in the night, and murder you.")
      print("\n You didn't finish the Camino.  You die and go to hell.")
      print("\n Buen Camino loser. The End \n ")
      playagain()
  elif choice2 == 'town':
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n You chose the town and the people are very very kind.")
      print("\n After a night of eating and drinking at the albergue, a mysterious woman comes up to you")
      print("\n Woman: 'You are a pilgrim.  We haven't had someone finish the Camino in over 20 years!'")
      print("\n Woman: If you really aim to finish the Camino, you will need these.")
      print("\n The woman pulls out a pendant and a sword, and you take them")
      print("\n You get a good nigh's rest, and then wake up to a hot breakfast")
      print("\n Woman: 'When you get to Santiago de Compostela, don't trust the cardinal. He is an evil man.")
      print("\n You pack your bag, collecting your pendant and sword")
      print("\n Woman: 'If you are ever in a situation where all seems to be lost, remember to 'pray'.")
      print("\n The woman shouts 'Buen Camino' as you walk away from the town.")
      print("\n After days of walking, you arrive at a glorious cathedral, but soldiers guard the way")
      print("\n After some thought, you realize there is no way around them. You can either attempt to sneak past them, or talk to them. \n")
      choice3 = input("Do you sneak, or do you talk? ")
  else:
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n You didn't choose the city or the town, and got lost and died, and went to hell like an idiot.")
      print("\n Buen Camino loser. The End. \n ")
      playagain()

  if choice3 == 'talk':
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n The guards look at you curiously as you approach them.")
      print("\n One goes to raise his sword to strike you, but his commander stops him")
      print("\n Commander: Stop! Don't you see that pendant?! This is what the Cardinal has been looking for!")
      print("\n The commander takes you into a small building just outside of the cathedral")
      print("\n Just in front of you is a man facing away from you, wearing red robes. It's the Cardinal!")
      print("\n The Cardinal turns towards you and has a sinister look in his eye.")
      print("\n Cardinal: You will not be finishing the Camino de Santiago today.")
      print("\n Cardinal: Leave the pendant with me and I will let you walk away peacefully. Refuse and you die. \n ")
      choice4 = input("You have an important decision to make 'give pendant' or 'fight'. ")
  elif choice3 == 'sneak':
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n You accidentally sneaze as you try to sneak past the guards.")
      print("\n All at once they surround you, and then the next day they string you up just outside of the cathedral, never to finish the Camino.")
      print("\n You die a slow, drawn out death... and then go to hell")
      print("\n Buen Camino loser, The End \n")
      playagain()
  else:
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n You just freeze there, until a guard sees you and then puts you in prison, never to finish the Camino.")
      print("\n Buen Camino loser, The End \n")
      playagain()

  if choice4 == 'fight':
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n You refuse to give the pendant")
      print("\n Just as the Cardinal is becoming outraged, you pull out your sword and stab him!")
      print("\n The Cardinal will not be able to stop you from completing the Camino now...")
      print("\n You shout at the Cardinal 'Buen Camino scumbag!")
      print("\n But... you look down and notice blood pouring from your abdomen, and a bloody dagger clutched in the Cardinal's hand!")
      print("\n The end of the Camino is just ahead of you, but you don't have the strength to continue... \n ")
      final_choice = input("It seems all is lost, you are so close... What do you do? ")
  elif choice4 == 'give pendant':
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n You give the pendant to the Cardinal like a coward and walk away.")
      print("\n You freely walk past the guards, and head back home living out the rest of your days in shame and misery.")
      print("\n You die of old age, alone, and ashamed of your very existence. And then you go to hell.")
      print("\n Buen Camino loser. The End. \n ")
      playagain()
  else:
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n You speak gibberish.")
      print("\n The Cardinal is annoyed, and then he stabs you with a dagger, taking the pendant from around your neck.")
      print("\n The Cardinal bends down to you just as your dying and says, 'Buen Camino loser.")
      print("\n The End... and you're in hell. \n")
      playagain()

  if final_choice == 'pray':
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n You remember the advice of the woman who gave you the pendant, and you pray.")
      print("\n You hold your wound as blood pours through, dropping to your knees to pray.")
      print("\n Your vision blurs...")
      print("\n Just as it all seems to be over, the pendant begins to glow!")
      print("\n Your vision comes back to you, the bleeding stops, and you miraculously are back on your feet!")
      print("\n You run to the cathedral doors and throw them open, light from outside pouring in all around you.")
      print("\n You have finished the Camino de Santiago, the first person to have done so in 20 years!")
      print("\n You leave Santiago de Compostela, ushering in a new era.")
      print("\n Pilgrims the world over can now embark upon the Camino de Santiago in peace, and it's all thanks to you!")
      print("\n You live out your days peacefully, eventually dying of old age surrounded by people you love.")
      print("\n You wake up in heaven! \n ")
      print(f"God: Buen Camino {name}, welcome home. \n ")
      print("The End... \n")
      print("or is it? \n")
      playagain()

  else:
      print("-------------------------------------------------------------------------------------------------------------------------------")
      print("\n You fumble around, in a panic, desperately crawling toward the end of the Camino")
      print("\n You get close, but so much blood has poured out that you just can't continue any further")
      print("\n You collapse to the ground just feet away from the Cathedral doors and the finish of the Camino.")
      print("\n You stare at the cathedral doors desperately as you fade into darkness.")
      print("\n And then you die, just before you can finish the Camino.")
      print("\n Buen Camino loser. The End...  You should have listened to the woman's advice. \n")
      playagain()

beginning()




