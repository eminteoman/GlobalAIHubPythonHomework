firstName = input("Enter your first name\n")
lastName  = input("Enter your last name\n")
age       = input("Enter your age\n")
dateOfBirth = input("Enter your birth day(only year)\n")

userInfo = [firstName,lastName,age,dateOfBirth]
for ele in userInfo:
    print(ele,"\n")
if int(age) >= 18:
    print("You can go out to the street.")
else:
    print("You can't go out beacuse it's too dangerous")