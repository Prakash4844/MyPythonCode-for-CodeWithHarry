# Practice set Q4
# Author: Prakash

with open(f"Chapter 9/Practice Set/Q4/Weird.txt",'r') as f:
      content = f.read()
      content = content.replace("donkey", "######")

with open(f"Chapter 9/Practice Set/Q4/Weird.txt",'w') as f:
      f.write(content)
