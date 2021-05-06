import hashlib
import requests
import re
import click

def check_pw_hibp(password):
    '''
    Checks if a given password is in the haveibeenpwned pwned password database.

    Parameter - password: string, password to be checked
    '''
    hashed_pw = hashlib.sha1(bytes(password, 'utf-8')).hexdigest().upper()
    hash_prefix = hashed_pw[:5]

    url = "https://api.pwnedpasswords.com/range/{}".format(hash_prefix)
    res = requests.get(url)

    if res.status_code == 200:
        for line in res.text.split('\n'):
            line = re.sub(':.*$', '', line)
            if hashed_pw == hash_prefix + line:
                return False
        return True
        
    else:
        msg = ("warning: wordup was unable to check this password against the "
                "haveibeenpwned API.\nPlease ensure this is a strong password, "
                "or run 'wordup gen' to generate one.")
        click.echo(click.style(msg, fg='yellow'))
        return True
