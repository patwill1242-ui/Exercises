usernames=['Jaden','Yugi','Yusei','admin','Yuma','Yuya','Yusaku']

if not usernames:
    print("The list is empty")
else:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again")

usernames=[]

if not usernames:
    print("The list is empty")
else:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again")