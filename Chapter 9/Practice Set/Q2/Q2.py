# Practice set Q2
# Author: Prakash


def game():
    hs = int(input("Enter Your Score: "))
    return hs


score = game()

with open("Chapter 9/Practice Set/Q2/HiScore.txt",'r') as f:
    hiscorestr = f.read()

if hiscorestr == '':
    with open("Chapter 9/Practice Set/Q2/HiScore.txt",'w') as f:
        f.write(str(score))

elif (score > int(hiscorestr)):
    with open("Chapter 9/Practice Set/Q2/HiScore.txt",'w') as f:
        f.write(str(score))
