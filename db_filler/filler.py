# -*- coding: utf-8 -*-
"""
todo: Documentation

    Project name: Python
    File name: filler
    
    Date created: 21/04/2020
    Date last modified: 21/04/2020
    Status: Development

    Python version: 3.8
    Modules required: psycopg2
"""
__author__ = 'Ariel Montes Nogueira'
__website__ = 'http://www.montes.ml'
__email__ = 'arielmontes1989@gmail.com'

__copyright__ = 'Copyright © 2020-present Ariel Montes Nogueira'
__credits__ = []
__license__ = '''
                Licensed under the Apache License, Version 2.0 (the "License");
                you may not use this file except in compliance with the License.
                You may obtain a copy of the License at
                
                    http://www.apache.org/licenses/LICENSE-2.0
                
                Unless required by applicable law or agreed to in writing, software
                distributed under the License is distributed on an "AS IS" BASIS,
                WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
                See the License for the specific language governing permissions and
                limitations under the License.'''
__recovery__ = ''
__version__ = '0.1'

import psycopg2
from sys import argv, exit as exits
from json import loads
from os import popen

# Get database url (Must be authenticated in Heroku)
DATABASE_URL = popen('heroku config:get DATABASE_URL -a dustbin-iot').read()[:-1]
con = None

# Take json list from shell with command: '$ python filler.py ../data.txt'
file = open(argv[1]).read()
sensors = loads(file)

"""
    JSON FILE EXAMPLE

[
  {
    "id": null,
    "capacity": 40,
    "battery": 50,
    "ip": "192.168.1.1",
    "location": "Central Park Avenue - NY"
  },
  {
    "id": 1,
    "capacity": 30,
    "battery": 80,
    "ip": "192.168.1.2",
    "location": "Central Park Avenue - NY"
  }
]

"""

try:
    con = psycopg2.connect(DATABASE_URL)
    con.autocommit = True  # todo: 'TRUE' FOR WRITE IN DB
    cur = con.cursor()
    print('Writing:', con.autocommit)

    def exist(sensor):
        cur.execute('select exists (select 1 from web_sensor where id = %(id)s)', sensor)
        return cur.fetchone()[0]

    count_add = 0
    count_upd = 0
    for i in sensors:
        # Create new sensors if id is None
        if i['id'] is None:
            cur.execute("INSERT INTO web_sensor (capacity, battery, ip, location) "
                        "VALUES(%(capacity)s, %(battery)s, %(ip)s, %(location)s)", i)
            count_add += 1
        else:
            # Create new sensors with a specified id
            if not exist(i):
                cur.execute("INSERT INTO web_sensor (capacity, battery, ip, location, id) "
                            "VALUES(%(capacity)s, %(battery)s, %(ip)s, %(location)s, %(id)s)", i)
                count_add += 1

    # Update sensors (find sensor by id)
    cur.executemany("UPDATE web_sensor SET capacity=%(capacity)s, battery=%(battery)s, ip=%(ip)s, location=%(location)s"
                    " WHERE id=%(id)s", sensors)

    print(f'Number of sensors added: {count_add}')
    print(f'Number of sensors updated: {cur.rowcount - count_add}')

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    exits(1)

finally:

    if con:
        con.close()
