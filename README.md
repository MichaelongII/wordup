## wordup - a cli password manager

#### Setup:
- create a virtual env and activate: ```virtualenv venv --python=python3 && source venv/bin/activate```
- install dependecies: ```pip install -r requirements.txt```
- complie encrypted SQLite db: ```./setup.sh```
- create local encrypted db: ```./src/wordup.py init```

```
$ ./src/wordup.py     
Usage: wordup.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add     [NAME] - Adds a password to the db with a corresponding NAME.
  check   [PASSWORD] - Checks if a PASSWORD was in a data breach.
  clear   Clears the contents of the clipboard.
  delete  [NAME] - Deletes a password from the db with a corresponding NAME.
  get     [NAME] - Places the password with NAME into the clipboard.
  ```


#### Commands:
1. ```add <name>```
- stores password in user's db with a given name
- checks if given password has been leaked in a data breach with the [HIBP API](https://haveibeenpwned.com/API/v3)

2. ```add <name>```
- stores password in user's db with a given name
- checks if given password has been leaked in a data breach with the [HIBP API](https://haveibeenpwned.com/API/v3)

3. ```<name>```
- gets the password with <name> from db and puts it in user's clipboard

4. ```clear```
- clears the user's clipboard

5. ```delete <name>```
- deletes the password from the db with corresponing name

6. ```gen <name>```
- generates, and if name is provided, adds a password to the db with a corresponing name
- generates a strong password
  
