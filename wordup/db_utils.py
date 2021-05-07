from pysqlite3 import dbapi2 as sqleet
import click


def create_db(key):
    con = sqleet.connect('wordup.db')
    cur = con.cursor()
    cur.execute("PRAGMA key=':key'", {"key": key})
    cur.execute("create table pass (name, password)")
    con.commit()
    con.close()

    click.echo("database initialized succesfully")


def add_pw_to_db(key, password, name):
    con = sqleet.connect('wordup.db')
    cur = con.cursor()
    cur.execute("PRAGMA key=':key'", {"key": key})

    cur.execute("""SELECT name FROM pass WHERE name=:name""", {"name": name})
    if cur.fetchone():
        con.commit()
        con.close()
        raise DuplicateNameAdd

    else:
        cur.execute("insert into pass values (?, ?)", (name, password))
        con.commit()
        con.close()

def delete_pw_from_db(key, name, username=None):
    con = sqleet.connect('wordup.db')
    cur = con.cursor()
    cur.execute("PRAGMA key=':key'", {"key": key})

    cur.execute("""SELECT name FROM pass WHERE name=:name""", {"name": name})
    if cur.fetchone():
        con.commit()
        con.close()
        raise DeleteNonExistentRecord

    else:
        cur.execute("DELETE FROM pass WHERE name=:name""", {"name": name})
        con.commit()
        con.close()

def get_pw_from_db_by_name(key, name):
    con = sqleet.connect('wordup.db')
    cur = con.cursor()
    cur.execute("PRAGMA key=':key'", {"key": key})

    cur.execute("""SELECT password FROM pass WHERE name=:name""", {"name": name})
    result = cur.fetchone()
    if result:
        con.commit()
        con.close()
        return result[0]
    else:
        raise GetNonExistentRecord


class DuplicateNameAdd(Exception):
    """Raised when the input value is too small"""
    pass

class DeleteNonExistentRecord(Exception):
    """Raised when the input value is too small"""
    pass

class GetNonExistentRecord(Exception):
    """Raised when the input value is too small"""
    pass
