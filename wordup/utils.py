import click
import os
from functools import update_wrapper

def generate_password():
    pass

def validate_name(ctx, param, value):
    if not value.isalnum():
        raise click.BadParameter('names must be alphanumeric')
    else:
        return value

def print_help_msg(command):
    with click.Context(command) as ctx:
        click.echo(command.get_help(ctx))

def print_general_error():
    msg = ('Could not add password, please ensure you entered your wordup '
            'password correctly.')
    click.echo(click.style(msg, fg='red'))

def init_required(f):
    @click.pass_context
    def new_func(ctx, *args, **kwargs):
        return ctx.invoke(f, ctx.obj, *args, **kwargs)
    if os.path.exists('wordup.db'):
        return update_wrapper(new_func, f)
    else:
        raise NoDbException


def is_db_missing():
    if not os.path.exists('wordup.db'):
        msg = ("Your password db is not set up yet, run 'wordup init'"
                'to set your wordup password.')
        click.echo(click.style(msg, fg='red'))

class NoDbException(Exception):
    pass
