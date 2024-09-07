'''
                            [THE PERFECT GUESS {TPG}] Game
                        Programming Language used --> Python  
'''
def tpg():                          # Main/Head Function
    import random
    rn = random.randint(1,100)

    # print(rn)                     # Cheating tool
                                    # {already prints the number,which is to be guessed by the Player}
                                    
    # g = 0                         # g  --> Guess {initially it can be 0 or None}
    g = None                       
    tg = 0                          # tg --> Total Guesses {initially = 0}

# Player's Turn !!

    while(g != rn):

# If wrong option is choosed by the Player !!

        while True:                 # If option choosed is not of an Integer type {Exception handling}
            try:                    
                g = int(input(
                    '''Guess any value {between 1 - 100} : '''
                    ))
                break
            except ValueError:
                print('''
                !! Entered value is Invalid !!
                Attention  ---> Value is not an Integer
                Suggestion ---> Try again {Integer value is acceptable only}
                ''')

        if (g<=0 or g>100):         # If option choosed is Out of Range
            print('''
            !!! Value Out of Range !!!
            {You have choosed a value which is not b/w 1-100 }
            Attention  ---> Value choosed is either <= 0 or > 100
            Suggestion ---> Please choose value b/w {1 -100} only !!
            ''')
            break

# If correct option is choosed by the Player !!

        else:
            tg = tg + 1

            if (g==rn):
                print('''
                Woohhhoooooo!!!
                Congratulations, Your Guess is 100 % Correct
                ''')
    
# Correct value & Total number of attempts taken by the Player to achieve correct guess !!

                print('''
                Correct value is ---> ''',rn)
                print('''
                Total number of valid attempts to guess a correct value is ---> ''',tg)

# Player's Performance !!

                if tg<=3:                   # If Total Guesses lies b/w 1 - 3
                    print('''
                    Excellent Performance !!
                    {You Guessed the required value in just less than 4 attempts}
                    ''')

                elif tg>=4 and tg<=6:       # If Total Guesses lies b/w 4 - 6
                    print('''
                    Good Performance !!
                    {You Guessed the required value in just less than 7 attempts}
                    ''')

                elif tg>=7  and tg<=1:      # If Total Guesses lies b/w 7 - 10
                    print('''
                    Average Performance !!
                    {You Guessed the required value in just less than 11 attempts}
                    ''')

                else:                       # If Total Guesses are > 10
                    print('''
                    Very Bad Performance !!
                    Try to improve.
                    {You Guessed required value in more than 11 attempts}
                    ''')

# While Player is guessing !!  

            else:
                if(g>rn):
                    print('''
                    Ooopss!!!
                    Sorry, Your Guess is W R O N G !! 
                    {HINT :- enter a smaller value} 
                    ''')
                else:
                    print('''
                    Ooopss!!!
                    Sorry, Your Guess is W R O N G !! 
                    {HINT :- enter a larger value} 
                    ''')

# Want to Continue or Exit ?

    print("\n")
    ec = input('''
    Want to Play again or Continue ?? ---> Press 1
    Want to E X I T ?? ---> Press any key except 1
    ''')
    if ec == "1":
        tpg()               # Main Function Call
    else:
        exit()              # exit Function Call

# Main Function Call

tpg()

'''********************END OF THE CODE********************'''