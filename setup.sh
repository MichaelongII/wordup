#!/usr/bin/env bash

cd env

# compile pysqlite3 with sqleet source code
git clone https://github.com/coleifer/pysqlite3
cd pysqlite3

curl -L -o sqleet-v0.27.1-amalgamation.tar.gz https://github.com/resilar/sqleet/releases/download/v0.27.1/sqleet-v0.27.1-amalgamation.tar.gz
tar -xvzf sqleet-v0.27.1-amalgamation.tar.gz

mv sqleet-v0.27.1/sqleet.c sqlite3.c
mv sqleet-v0.27.1/sqleet.h sqlite3.h

python3 setup.py build_static
python3 setup.py install
