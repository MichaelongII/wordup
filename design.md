### wordup high level design

#### Commands:
1. ```add <name>```
- Adds a password to the db with a corresponing name
- checks prefix of pw hash against [HIBP API](https://haveibeenpwned.com/API/v3)

2. ```name```
- places the passowrd stored with given name in the user's clipboard

3. ```clear```
- clears the user's clipboard

4. ```delete name```
- deletes the record from the db with name

5. ```gen <name>```
- Generates, and if name is provided, adds a password to the db with a corresponing name
- Generates a strong password
