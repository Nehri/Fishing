# Let's go fishing!
from random import randint


# this generates a random name for the fish
def genFish():
    vowel = False # counter for when a vowel is chosen
    vowel2 = False # counter for when there are two vowels in a row
    consonant = False # counter for when a consonant is chosen
    consonant2 = False # counter for when there are two consonants in a row
    maxLen = 12 # the length of the fish's name
    randNum = 0
    randQuit = False #20% chance that the name ends after every letter
    fishName = ""
    while maxLen > 0 and randQuit == False:
        num = randint(0, 25)
        # checks to see if there are two vowels in a row
        if vowel == True and vowel2 == True:
        	# if the next number is a vowel, it skips to the next generated int
            if num == 0 or 4 or 8 or 14 or 20 or 24:
                continue
            # if the next int is a consonant, it resets the counters
            else:
                vowel = False
                vowel2 = False

        # checks to see if there are two consonants in a row
        if consonant == True and consonant2 == True:
        	# if the next number is a consonant, it has a 67% chance of skipping to the next generation
            if num != 0 and num != 4 and num != 8 and num != 14 and num != 20 and num != 24:
                randNum = randint(0,2)
                if randNum != 2:
                    continue
                # if randNum is 2, the third consonant in a row is allowed (33% chance of this)
            # if the next int is a consonant, it resets the counters
            else:
                vowel = False
                vowel2 = False

		# adds the letter to the fish's name
        fishName = fishName + chr(ord('a')+num)
        print('added letter')
        # if num is a vowel
        if num == 1 or 4 or 8 or 14 or 20 or 24:
            if vowel == True:
                vowel2 = True
            else:
                vowel = True
                vowel2 = False
            consonant = False
            consonant2 = False
        # if num is a consonant
        else:
            if consonant == True:
                consonant2 = True
            else:
                consonant = True
                consonant2 = False
            vowel = False
            vowel2 = False
        maxLen -= 1

        # if the fish's name is already 2 letters long, there is a 20% chance of the name randomly stopping)
        if maxLen <= 10:
            randNum = randint(1,5)
            if randNum == 5:
                randQuit = True
    return fishName

def fish():
    num = randint(0,3)

    # 25% chance of catching nothing
    if num == 2:
        print("You've caught nothing this time.")
    else:
        name = genFish()
        print("You've caught a " + name + "!")


# asks the user to fish, and gives them a fish if they choose to
def main():
    response = input("Would you like to go fishing?\n")
    if response == 'Yes' or 'yes' or 'YES' or 'yes!' or 'Yes!' or 'Ya':
        fish()
        print("Thanks for fishing with us today!\nCome back again soon!")
    else:
        print("That's too bad.\nCome again later, 'kay?")

if __name__ == "__main__":
    main()
