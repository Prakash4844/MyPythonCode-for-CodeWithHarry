# Practice set Q1
# Author: Prakash

with open("Chapter 9/Practice Set/Q1/poem.txt",'r') as f:
    search_word = "Twinkle"

    if (search_word in f.read()):
        print("Twinkle is present.")
    else:
        print("Twinkle isn't present.")
