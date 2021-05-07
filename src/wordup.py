#!/usr/bin/env python3
import click
import clipboard
import os.path
from db_utils import *
from utils import generate_password, validate_name, print_general_error
from hibp_api import check_pw_hibp

@click.command()
@click.option('--key', prompt="wordup password", hide_input=True)
@click.option('-p', '--password', 'password', prompt="password to set",
                hide_input=True, confirmation_prompt=True)
@click.argument('name', callback=validate_name)
def add(key, password, name):
    '''
    [NAME] - Adds a password to the db with a corresponding NAME.

    Password is checked against the HIBP pwned passwords API and will
    only be added if it is not present in their list of leaked passwords.

    Parameters:
        - key: string, key to encrypted db
        - password: string, new password to add
        - name: string, name of password to be added
    '''
    try:
        if not check_pw_hibp(password):
            msg = ('\nThe password you entered has been leaked in a data breach '
                    'and therefore is insecure, please enter a different '
                    'password.\nFor more information see '
                    'https://haveibeenpwned.com/Passwords')
            click.echo(click.style(msg, fg='red'))
            return
        add_pw_to_db(key, password, name)
        click.echo("\nPassword '{}' successfully added".format(name))

    except DuplicateNameAdd:
        msg = ('That name has already been added, please add this password'
                'under a different name.')
        click.echo(click.style(msg, fg='red'))

    # except Exception as e:
    #     print_general_error()
    #     print(e)

@click.command()
@click.option('--key', prompt="wordup password", hide_input=True)
@click.argument('name', callback=validate_name)
def get(key, name):
    '''
    [NAME] - Places the password with NAME into the clipboard.

    Parameters:
        - key: string, key to encrypted db
        - name: string, name of password to be added
    '''
    try:
        password = get_pw_from_db_by_name(key, name)
        clipboard.copy(password)
        click.echo("\nPassword '{}' copied to clipboard".format(name))

    except GetNonExistentRecord:
        msg = ("\nThere's no password stored under that name")
        click.echo(click.style(msg, fg='red'))

    # except Exception:
    #     print_general_error()


@click.command()
@click.option('--key', prompt="wordup password", hide_input=True)
@click.argument('name', callback=validate_name)
def delete(key, name):
    '''
    [NAME] - Deletes a password from the db with a corresponding NAME.

    Parameters:
        - key: string, key to encrypted db
        - name: string, name of password to be added
    '''
    try:
        delete_pw_from_db(key, name)
        click.echo('\nPassword for {} deleted'.format(name))

    except DeleteNonExistentRecord:
        msg = ("\nThere's no password stored under that name")
        click.echo(click.style(msg, fg='red'))

    # except Exception:
    #     print_general_error()


@click.command()
@click.option('-p', '--password', 'password', prompt="password to set",
                hide_input=True, confirmation_prompt=True)
def check(password):
    '''
    [PASSWORD] - Checks if a PASSWORD was in a data breach.

    Parameters:
        - key: string, key to encrypted db
        - name: string, name of password to be added
    '''
    click.echo('\nChecking if password has been comprimised...')
    if check_pw_hibp(password):
        click.echo("\nPassword has not been pwned!")

    else:
        msg = ("\nPassword is the haveibeenpwned pwned passwords database! "
                    "Don't use that password!")
        click.echo(click.style(msg, fg='red'))


@click.command()
def clear():
    '''
    Clears the contents of the clipboard.
    '''
    clipboard.copy("")
    click.echo('Clipboard cleared')


@click.command()
@click.option('--key', prompt="set your wordup password", hide_input=True,
                confirmation_prompt=True)
def init(key):
    '''
    Creates an encrypted database for your passwords.
    '''
    create_db(key)
    click.echo("\nwordup password set")

@click.group()
def first_run():
    pass


@click.group()
def cli():
    pass


cli.add_command(add)
cli.add_command(get)
cli.add_command(delete)
cli.add_command(check)
cli.add_command(clear)
first_run.add_command(init)


if __name__ == '__main__':
    if os.path.exists('wordup.db'):
        cli()
    else:
        first_run()
