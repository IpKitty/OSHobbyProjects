import time
import random
import json
import os

# this checks the directory of the script and turns it into an absolute path before changing it
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

numbers_wanted = int(input('Input amount of IDS to generate:\n'))



# this gets the time.time() and turns it into an integer
def getTimeInt():
  a = str(time.time())
  a = a.split('.')
  a = int(a[0] + a[1])
  return a

# this list will be used for storing the numbers
NumberList = []

count = 0
print('')
while count < numbers_wanted:
  count += 1

  # this runs getTimeInt() but adds a delay to make sure it isnt the same the next time this loop continues
  time.sleep(random.randint(100, 135) / 10000)
  BaseNumber = str(getTimeInt())  
  BaseNumber = [*BaseNumber]
  # this creates the number to multiply by, using the last 2 integers of the basenumber
  Multiplier = int(BaseNumber[-1] + BaseNumber[-2])
  
  BaseNumber = int(''.join(BaseNumber))

  ResultNumber = BaseNumber * Multiplier

  # this appends the result to the list outside of the loop
  NumberList.append(ResultNumber)
  print(ResultNumber)

  # this checks for duplicates, sets cannot contain a duplicate
  # if the length of a list and a set arent alike, theres a duplicate
  if len(NumberList) != len(set(NumberList)):
    break

# debug print statement
if len(NumberList) != len(set(NumberList)):
  print(f'There was a duplicate!!!!!!!\n{NumberList[-1]}')

# this opens the IDS.json file to be able to copy its contents
with open('IDS.json', 'r') as file:
  data = json.load(file)

# this makes data the numberlist created
data['IDS'] = NumberList

# this writes the data variable into the json file with an indent of 4 so it doesnt bunch up on 1 line
with open('IDS.json', 'w') as file:
  json.dump(data, file, indent=4)


