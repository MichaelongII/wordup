import click

def generate_password():
    pass

def validate_name(ctx, param, value):
    if not value.isalnum():
        raise click.BadParameter('names must be alphanumeric')
    else:
        return value