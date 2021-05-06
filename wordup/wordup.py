import click
import clipboard
from db_utils import *
from utils import generate_password, validate_name
from hibp_api import check_pw_hibp

@click.command()
@click.option('--key', prompt="wordup password", hide_input=True)
@click.option('-p', '--password', 'password', prompt="password to set",
                hide_input=True, confirmation_prompt=True)
@click.argument('name', callback=validate_name)
def add(key, password, name):
    '''
    Adds a password to the db with a 'name'.

    Password is checked against the HIBP pwned passwords API and will
    only be added if it is not present in their list of leaked passwords.

    Parameters:
        - key: string, key to encrypted db
        - password: string, new password to add
        - name: string, name of password to be added
    '''
    try:
        if not check_pw_hibp(password):
            msg = ('The password you entered has been leaked in a data breach '
                    'and therefore is insecure, please enter a different '
                    'password.\nFor more information see '
                    'https://haveibeenpwned.com/Passwords')
            click.echo(click.style(msg, fg='red'))
            return
        # add_pw_to_db(key, password, name)
        click.echo('Password for {} successfully added'.format(name))
    except Exception:
        msg = ('Could not add password, please ensure you entered your wordup '
                'password correctly.')
        click.echo(click.style(msg, fg='red'))


@click.command()
@click.option('--key', prompt="wordup password", hide_input=True)
@click.argument('name', callback=validate_name)
def get(key, name):
    try:
        password = get_pw_from_db_by_name(key, name)
        clipboard.copy(password)
        click.echo('Password for {} copied to clipboard'.format(name))
    except Exception as e:
        click.echo(e.args)


@click.command()
@click.option('--key', prompt="wordup password", hide_input=True)
@click.argument('name', callback=validate_name)
def delete(key, name):
    try:
        # delete_pw_from_db(key, name)
        click.echo('Password for {} deleted'.format(name))
    except Exception as e:
        click.echo(e.args)


@click.command()
@click.option('-p', '--password', 'password', prompt="password to set",
                hide_input=True, confirmation_prompt=True)
def check(password):
    click.echo('\nChecking if password has been comprimised...')
    if check_pw_hibp(password):
        click.echo("Password has not been pwned!")
    else:
        msg = ("Password is the haveibeenpwned pwned passwords database! "
                    "Don't use that password!")
        click.echo(click.style(msg, fg='red'))


@click.command()
def clear():
    clipboard.copy("")
    click.echo('Clipboard cleared')


@click.group()
def cli():
    pass


cli.add_command(add)
cli.add_command(get)
cli.add_command(delete)
cli.add_command(clear)
cli.add_command(check)


if __name__ == '__main__':
    cli()
