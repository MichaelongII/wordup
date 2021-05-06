import hashlib
import requests
import re
import click


def check_pw_hibp(password):
    hashed_pw = hashlib.sha1(bytes(password, 'utf-8')).hexdigest().upper()
    hash_prefix = hashed_pw[:5]
    hash_suffix = hashed_pw[5:]

    url = "https://api.pwnedpasswords.com/range/{}".format(hash_prefix)

    res = requests.get(url)
    if res.status_code == 200:
        for line in res.text.split('\n'):
            line = re.sub(':.*$', '', line)
            if hashed_pw == hash_prefix + line:
                return False
        return True
    else:
        click.echo(click.style("warning: wordup was unable to check this password against the haveibeenpwned API.\nPlease ensure this is a strong password, or run 'wordup gen' to generate one.", fg='yellow'))
        return True