print("1. Forward Chaining")
print("2. Backward Chaining")
chooseMenu=(int(input(">>")))
if chooseMenu == 1:
    #ai forward
    def meats():
        print("1. Eats Meat")
        print("2. Eats Fruit and Plants")
        choose = int(input(">> "))
        if choose == 1:
            print("1. Have Spots")
            print("2. No Spots")
            choose = int(input(">> "))
            if choose == 1:
                print("1. The fastest Animal on Ground")
                print("2. Fast")
                choose = int(input(">> "))
                if choose == 1:
                    print("The Result is Cheetah")
                else:
                    print("Not Cheetah")
            else:
                print("Not Cheetah")
        else:
            print("Not Cheetah")

    print("Guess The Cheetah")
    print("1. Has Hair")
    print("2. No Hair")
    choose = int(input(">> "))
    if choose == 1:
        print("Mammals")
        print("1. Has Claws")
        print("2. No Claws")
        choose = int(input(">> "))
        if choose == 1:
            print("1. Has Sharp Teeth")
            print("2. No Sharp Teeth")
            choose = int(input(">> "))
            if choose == 1:
                print("1. Forward Pointing Eye")
                print("2. Side Pointing Eye")
                choose = int(input(">> "))
                if choose == 1:
                    meats()
                else:
                    meats()
            else:
                meats()
        else:
            meats()

    elif choose == 2:
        print("Not Cheetah")
    else:
        print("Please Choose The Right Number")

elif chooseMenu == 2:
    print("Backward Chaining")
    print("There's a fact of Cheetah")
    print("1. Mammals")
    print("2. Other")
    choose = int(input(">> "))
    if choose == 1:
        mammals = True
        print("1. Has Hair")
        print("2. No Hair")
        choose = int(input(">> "))
        if choose == 1:
            hair = True
        elif choose == 2:
            hair = False
    else:
        mammals = False
        hair = False
    print("1. Carnivora")
    print("2. Herbivora or Other")
    choose = int(input(">> "))
    if choose == 1:
        carnivore = True
        print("1. Has Claws")
        print("2. Other")
        choose = int(input(">> "))
        if choose == 1:
            claws = True
            print("1. Sharp Teeth")
            print("2. Other Teeth")
            choose = int(input(">> "))
            if choose == 1:
                sharpTeeth = True
                print("1. Forward Pointing")
                print("2. Side Pointing Eyes")
                choose = int(input(">> "))
                if choose == 1:
                    eyes = True
                else:
                    eyes = False
            else:
                sharpTeeth = False
        else:
            claws = False
            sharpTeeth = False
            eyes = False
        print("1. Eat Meats")
        print("2. Other")
        choose = int(input(">> "))
        if choose == 1:
            eats = True
        else:
            eats = False
    else:
        carnivore = False
        claws = False
        sharpTeeth = False
        eyes = False
        eats = False
    print("1. Spots")
    print("2. No Spots")
    choose = int(input(">> "))
    if choose == 1:
        spots = True
    else:
        spots = False
    print("1. Very Fast")
    print("2. No Spots")
    choose = int(input(">> "))
    if choose == 1:
        fast = True
    else:
        fast = False

    print("========================")
    print("Fact Output : ")
    print(f"Mammals : {mammals}")
    print(f"Hair : {hair}")
    print(f"Carnivora: {carnivore}")
    print(f"Claws : {claws}")
    print(f"Teeth : {sharpTeeth}")
    print(f"Forward Pointing Eye : {eyes}")
    print(f"Eat Meats : {eats}")
    print(f"Spots : {spots}")
    print(f"Very Fast: {fast}")
    print("========================")

    def checkLeopard(mammals,hair,carnivore,claws,sharpTeeth,eyes,eats,spots,fast):
        if mammals == True and hair == True and carnivore == True and claws == True and sharpTeeth == True and eyes == True and eats == True and spots == True and fast == True:
            print("The Fact of Cheetah is Right")
        else:
            print("The Fact of Cheetah is wrong")

    checkLeopard(mammals,hair,carnivore,claws,sharpTeeth,eyes,eats,spots,fast)
