# التعريف للعبه و التحدث الي اللاعب

print("Imagine yourself walking alone in safety.🚶‍♂️.....")
input("Press Enter to continue...")
print("ops! A group criminals are kidnapping you!😱")
input("Press Enter to continue...")
print("luckily for you, the criminals didn't kill you; instead, they took you to an underground room in a massive house.🏚️")
input("to start playing, press Enter...^_^")

# بداية اللعب و اختيار اللاعب و محاولة الهروب من المبني

# المرحله الاولي الهروب من الغرفه

print("""you are lucky again.😊
you overheard one of the criminals say thet the key to the door🚪is hidden beneath one of the floor tiles; however, there are three tiles of different colorsn before you:
""")
print("But beware! there are things other than the key. Be careful as you choose; so, what tile will you choose?")
tiles = ["floor tile 1 🔳", "floor tile 2 🔳", "floor tile 3 🔳"]
print(tiles)
choice = input("Enter the number of the tile you want to choose:\n")
if choice == "1":
    print("you found the key!🔑")
    print("Well done! 🤩\nlet's move on to the next stage...")
    
    # المرحلهالثانيه من اللعبه و هي الهروب من المبني
    
    print("you are now trying to get out from underground, but there is a problem: in front of you are four doors.🚪")
    print("Which door will you choose?")
    doors = ["door 1 🚪", "door 2 🚪", "door 3 🚪", "door 4 🚪"]
    print(doors)
    choice = input("Enter the number of the door you want to choose:\n")
    if choice == "1":
        print("ops! 😥\nyou have entered the leader's room! 🥷")
        print("""

░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
""")
    elif choice == "2":
        print("ops! 😥\nyou entered the sniper's room! 🎯🥷")
        print("""

░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
""")
    elif choice == "3":
        print("ops! 😥\nyou entered the assassin's room! 🗡️🥷")
        print("""

░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
""")
    elif choice == "4":
        print("very good! 🤩\nyou have come to the right door 🚪.🥳")
       
        # مرحله الثالثه و الاخيرة من اللعبه و هي الهروب من المبني
       
        print("you are now trying to get out from the house, but there is a problem:the criminals have learned that you escaped from the room 😱")
        print("However, you have a chance to get out: you can exit through the window.🪟")
        print("But before you lie two windows: either you escape and win🥳😊, or you lose and die.😵☠️")
        windows = ["window 1 🪟", "window 2 🪟"]
        print(windows)
        choice = input("Enter the number of the window you want to choose:\n")
        if choice == "1":
            print("good luck! 🤩\nyou escaped and returned to your home! 🏠🥳🥳")
            print("""

██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝
""")
        elif choice == "2":
            print("ops! 😥\nyou have fallen in, and now you are dead.😵☠️")
            print("""

░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
""")
    else:
        print("Invalid choice. Please choose a valid door number (1, 2, 3, or 4).")

# تكملة المرحله الاولي من اللعبه و هي الهروب من الغرفه

elif choice == "2":
    print("ops! 😥\nyou grabbed a venomous snake!😵☠️")
    print("""

░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
""")
elif choice == "3":
    print("ops! 😥\nyou fell into avery deep hole!😵☠️")
    print("""

░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
""")
else:
    print("Invalid choice. Please choose a valid tile number (1, 2, or 3).")