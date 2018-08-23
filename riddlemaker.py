def riddlemaker():
    animalormanmade = input ("Which do you like better, animals or things that are manufactured")
    if animalormanmade == "animals":
        domesticorwild = input ("Which do you like better, domestic animals or wild animals")
        if domesticorwild == "domestic":
            whichone = input ("What type of domestic animal do you like?")
            print "Here is your riddle"
            whatami = input ("I have four legs, and I am cute.What am I?")
            if whatami == whichone:
                print ("That answer is correct. "  +   " Your favourite animal is "  +  whichone  + " isn't it!")
            else:
                print ("That answer is wrong. "  +   " The correct answer is  "  +  whichone) 
        else:
            whichone2 = input ("What type of wild animal do you like better? Mammal or reptile or bird?")
            if whichone2 == "mammal":
                whichone3 = input ("Which mammal do you like?")
                whatami2 = input ("I either live on land or in the sea.And I don't lay eggs.What type of mammal am I?")
                if whatami2 == whichone3:
                    print ("That answer is correct. "  +   " Your favourite animal is "  +  whichone3  + " isn't it!")
                else:
                    print ("That answer is wrong. "  +   " The correct answer is  "  +  whichone3)
            elif whichone2 == "reptile":
                whichone4 = input ("Which reptile do you like?")
                whatami3 = input ("I live in the swamp or on land, and I lay eggs.What type of reptie am I?")
                if whatami3 == whichone4:
                    print ("That answer is correct. "  +   " Your favourite animal is "  +  whichone4  + " isn't it!")
                else:
                    print ("That answer is wrong. "  +   " The correct answer is  "  +  whichone4)
            elif whichone2 == "bird":
                whichone5 = input ("Which bird do you like?")
                whatami4 = input ("I lay eggs and make nests.What type of bird am I?")
                if whatami4 == whichone5:
                     print ("That answer is correct. "  +   " Your favourite animal is "  +  whichone5  + " isn't it!")
                else:
                    print ("That answer is wrong. "  +   " The correct answer is  "  +  whichone5)
            else:
                print "Restart the whole code please."
                print "                              "
                    
    else:
        whichone6 = input("What type of manmade object do you like?")
        whatami5 = input ("You probabaly use me everyday.What am I?")
        if whatami5 == whichone6:
            print ("That answer is correct. "  +  " Your favourite manmade object is " +  whichone6 + " isn't it!") 
        else:
            print ("That answer is wrong. "  +  " The correct answer is " +  whichone6) 
