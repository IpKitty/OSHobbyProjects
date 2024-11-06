# How-To use

1. install the requirements.txt using: pip install -r (Path to the requirements.txt)

2. Open a browser with a logged out roblox signup page

3. Enter a random birthday

4. Open inspect element and traverse to the Network Tab

5. Enter a random username into the username box on the signup page

6. Search for the validate network request to https://auth.roblox.com/v1/usernames/validate

7. Scroll down the headers and find the X-Crsf-Token

8. Put the Token in main.py and execute!

- The Available usernames will be in AUsers.json

# How to generate users

1. install the requirements.txt using: pip install -r (Path to the requirements.txt)

2. Run the usermaker.py and follow the inputs

- The results should be in Ulist.json (no need to touch them)

# Disclaimer

- If you want to add your own usernames, I recommend using an LLM to index them in the format seen in Ulist.json.