from pysqlite3 import dbapi2 as sqleet
import click
import pathlib


def create_db(key):
    '''
    Creates an encrypted sqleet database and adds the pw table

    Parameter - key: string, key to encrypted db
    '''
    con = sqleet.connect(str(pathlib.Path(__file__).parent.absolute()) + '/wordup.db')
    cur = con.cursor()
    cur.execute("PRAGMA key=':key'", {"key": key})
    cur.execute("create table pw (name, password)")
    con.commit()
    con.close()
    click.echo("database initialized succesfully")


def add_pw_to_db(key, password, name):
    '''
    Adds a password to the database.

    Parameters
        - key: string, key to encrypted db
        - password: string, the password to add
        - name: string, the name to add
    '''
    con = sqleet.connect('wordup.db')
    cur = con.cursor()
    cur.execute("PRAGMA key=':key'", {"key": key})

    cur.execute("""SELECT name FROM pw WHERE name=:name""", {"name": name})
    if cur.fetchone():
        con.commit()
        con.close()
        raise DuplicateNameAdd

    else:
        cur.execute("insert into pw values (?, ?)", (name, password))
        con.commit()
        con.close()

def delete_pw_from_db(key, name):
    '''
    Deletes a password from the database.

    Parameters
        - key: string, key to encrypted db
        - name: string, the name to delete
    '''
    con = sqleet.connect('wordup.db')
    cur = con.cursor()
    cur.execute("PRAGMA key=':key'", {"key": key})

    cur.execute("""SELECT name FROM pw WHERE name=:name""", {"name": name})
    if cur.fetchone():
        con.commit()
        con.close()
        raise DeleteNonExistentRecord

    else:
        cur.execute("DELETE FROM pw WHERE name=:name""", {"name": name})
        con.commit()
        con.close()

def get_pw_from_db_by_name(key, name):
    '''
    Fetches a password from the database.

    Parameters
        - key: string, key to encrypted db
        - name: string, the name to fetch
    '''
    con = sqleet.connect('wordup.db')
    cur = con.cursor()
    cur.execute("PRAGMA key=':key'", {"key": key})

    cur.execute("""SELECT password FROM pw WHERE name=:name""", {"name": name})
    result = cur.fetchone()
    if result:
        con.commit()
        con.close()
        return result[0]
    else:
        raise GetNonExistentRecord


# Custom exceptions
class DuplicateNameAdd(Exception):
    pass

class DeleteNonExistentRecord(Exception):
    pass

class GetNonExistentRecord(Exception):
    pass
