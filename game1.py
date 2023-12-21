import random
tries=5

def myRandomNumberGenerator ():
    q=random.randint(1,50)
    return q

# Just gonna call my function to test.
r=myRandomNumberGenerator()
#print(r)
while tries!= 0:

    p=input('Enter Number:')
    p=int(p)
    if p>r :
        print('Too big,try Again', tries-1,' left')
    elif p<r :
        print('Too small,try again', tries-1,' left')
    else: 
        print('Youve won', ' want to plat again?y/n')
        PlayAgain = input()
        if PlayAgain=='y':
            r=myRandomNumberGenerator()
            tries=5

        break

    tries= tries-1
    if tries==0:
        print('You Loose', ' want to play again? y/n')
        PlayAgain = input()
        if PlayAgain=='y':
            r=myRandomNumberGenerator()
            tries=5
        
