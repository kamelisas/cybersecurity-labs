password = input("Enter password: ")

if len(password) < 8:
    print("Weak password")
else:
    print("Password length OK")