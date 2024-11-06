import requests
import json
import os

Token = '' # X-Crsf-Token

#############################################

os.chdir(os.path.dirname(__file__))

AvailableUsers = []

Payload = {
  "username": "test",
  "context": "Signup",
  "birthday": "2001-01-07T23:00:00.000Z"
}



with open('Ulist.json') as file:
    file = json.load(file)
    usernameList = file['Usernames']

def VerifyResponse(response, username):
    if response['code'] == 0 and response['message'] != 'Token Validation Failed':
        AvailableUsers.append(username)
        print(f'{username} - Available')
    if response['code'] == 1:
        print(f'{username} - Not Available')
    if response['code'] == 2:
        print(f'{username} - Censored')
    if response['code'] == 0 and response['message'] == 'Token Validation Failed':
        print('\n\n\n\n\nAdd a new X-Csrf-Token!!!!\n\n\n\n\n')
    

def SendPayload(Payload, username):
    request = requests.post('https://auth.roblox.com/v1/usernames/validate', Payload,headers={"referer": "https://www.roblox.com/", "X-Csrf-Token": Token})
    response = json.loads(request.text)
    VerifyResponse(response, username)

def MakePayload(username):
    SendablePayload = Payload
    SendablePayload['username'] = username
    SendPayload(Payload, username)

with open('Ulist.json', 'r') as file:
    data = json.load(file)
    maximum = len(data['Usernames'])

for i in range(maximum):
    MakePayload(usernameList[str(i)])

print(AvailableUsers)
with open('AUsers.json', 'r') as file:
    data = json.load(file)
with open('AUsers.json', 'w') as file:
    data['Available'] = AvailableUsers
    file = json.dump(data,file,indent=4)