import json
from os import path
import tqdm
THIS_FOLDER = path.dirname(path.abspath(__file__))
emails = path.join(THIS_FOLDER, "accounts.json")
dictlist = []

with open(emails) as x:
    dictlist = json.load(x)


devices = open("deviceids.txt", 'r')
for x in dictlist:
    email = x['email']
    password = x['password']
    Device = devices.readline()
    device = Device.strip()
    with open("newaccounts.json", 'a') as b:
        acc = f'\n{{"email": "{email}","password": "{password}","device": "{device}"}},'
        b.write(acc)

print('[\033[1;32m✔\033[m] \033[1;97mSaved accounts to newaccounts.json\n\033[m')
print('[\033[1;32m✔\033[m] \033[1;97mScript Finished')
