# Practice set Q1
# Author: Prakash

f = open("Chapter 9/Practice Set/Q1/poem.txt", 'r')
t = f.read()

if "Twinkle" in t:
    print("Twinkle is present.")
else:
    print("Twinkle isn't present.")
f.close()
