import click

def validate_name(ctx, param, value):
    if not value.isalnum():
        raise click.BadParameter('names must be alphanumeric')
    else:
        return value

def print_general_error():
    msg = ('Could not add password, please ensure you entered your wordup '
            'password correctly.')
    click.echo(click.style(msg, fg='red'))
