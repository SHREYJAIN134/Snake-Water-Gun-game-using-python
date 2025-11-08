''' 
We all have played snake,water and gun game in our childhood. If you haven't ,google the rules of this game and enjoy.
'''

name=input("Enter your name: ").capitalize()
youDict = {"snake": 1, "water": -1,"gun": 0}
while True:
    youstr= input("Enter your choice (snake/water/gun): ").lower()
    import random
    computer = random.choice([-1, 0, 1])
    reverseDict = {1: "Snake",-1: "Water",0: "Gun"}
    you = youDict.get(youstr)
    if you is None:
            print("Enter the correct spelling🤣.")
    else:
            print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

            if(computer==you):
                print("its a draw🤝")

            else:
                # if((computer - you)== -1 or (computer - you)== 2):
                #     print("You loose!")
                # else:
                #     print("You win!")
        #using the above commented else if we have increased the readablity by just using the logic

                if(computer==-1 and you==1):
                    print("You win!🔥")

                elif(computer==-1 and you==0):
                    print("You loose!💔")

                elif(computer==1 and you==-1):
                    print("You loose!💔")

                elif(computer==1 and you==0):
                    print("You win!🔥")
                    
                elif(computer==0 and you==-1):
                    print("You win!🔥")

                elif(computer==0 and you==1):
                    print("You loose!💔")

                else:
                    print("Something went rong😅.")

    again = input("Do you want to play again? (y/n): ").lower()
    if(again != "y"):
        print(f"Thanks! for playing {name},See you next time👋👋.")
        break
    else:
         continue