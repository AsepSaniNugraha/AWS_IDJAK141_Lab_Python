greet="Welcome, user"
print(greet)
print(type(greet))
print(f"{greet} is of the data type {type(greet)}")

firstName="John"
lastName="Doe"
fullName=f"{firstName} {lastName}"
print(fullName)

userName=input("Enter your user name: ")
print(userName)

role=input("Enter your role (teacher / student): ")
level=input("Enter your level (1 / 2 / 3): ")
print("Hello, {}! You are {} at level {}".format(userName,role,level))