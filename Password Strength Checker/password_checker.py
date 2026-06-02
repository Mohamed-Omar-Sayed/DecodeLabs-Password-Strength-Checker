import string
score=0
password = input("Enter your password to check its strength: ")
upper_case =any( c in string.ascii_uppercase  for c in password)
lower_case =any( c in string.ascii_lowercase  for c in password)
special =any( c in string.punctuation  for c in password)
digits =any( c in string.digits  for c in password)
length=len(password)
characters=[upper_case,lower_case,special,digits]
names = ["Upper Case", "Lower Case", "Special Character", "Digit"]
with open('commen.txt' ,'r')as f:
    commen=set(f.read().splitlines())
if 8 <= length <= 20:
    score+=1
if sum(characters)==4:
    score+=4
if password in commen:
    print("password was found in commen plz change u pass ")
    score=0
    exit()
if score>4:
  print("=> your password is passed")
else:
    for index, value in enumerate(characters):
        if value == 0: 
            print(f"Error: {names[index]} is Missing!")
    print("write again your password")

