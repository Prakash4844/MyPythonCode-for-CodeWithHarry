# Solution of Practice Set Q2

Letter = '''Dear <|NAME|>,
                You are Selected!
Date:<|DATE|>
'''
Name = input("Enter recipient's Name: ")
Date = input("enter Date: ")

Letter = Letter.replace("<|NAME|>", Name)
Letter = Letter.replace("<|DATE|>", Date)

print(Letter)
