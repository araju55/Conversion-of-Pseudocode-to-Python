password = input("Please enter password")
i = 2
k = 0
duplicates = False
while i <= len(password) and duplicates == False:
    k = 1
    while 2*k <= i and duplicates == False:

        duplicates = password[i-2*k:i-k] == password[i-k:i]
        k += 1


    i += 1

if duplicates:
    print("Password is not Accepted")
else:
    print("Password is Accepted")
