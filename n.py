# Josh Dickey 11/11/16
# this is a program that shows people who made deposits or withdraws

# this is joe's account
import account
joe = account.Account("joe", 11111111111, 90019)
print(joe)

# joe withdraws 900 dollars
if joe.withdraw(900):
    print("joe withdraws 900 dollars from his account")
    print(joe)
else:
    print("joe tries to withdraw 900 dollars from his account, but is denied")

# this is amy's account
amy = account.Account("amy", 1234567890, 38)
print(amy)

# amy tries to withdraw 100000000000 dollars
if amy.withdraw(100000000000):
    print("amy withdraws 100000000000 dollars from her account")
    print(amy)
else:
    print("amy tries to withdraw 100000000000 dollars from her account, but is denied")

# this is chiedu's account
chiedu = account.Account("chiedu", 8946382, 740)
print(chiedu)

# chiedu deposits 1200 dollars
chiedu.deposit(1200)
print("chiedu desposits 1200 dollars into his account")
print(chiedu)
