password = input("Enter a string for password: ")
digit_count = 0
for character in password:
    if character.isdigit():
        digit_count = digit_count + 1
if len(password) >= 8 and digit_count >= 2:
    print("valid password")
else:
    print("invalid password")
