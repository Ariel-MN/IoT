# IoT
Dustbin IoT Database Filler

- Data Format: json
- File Format: plain text
- Requeriments: python, psycopg2
- In filler.py find _'con.autocommit = False'_ and set it equal to _'True'_

The command for launch the db filler composition is: <br>
`[ interpreter ] [ script file ] [ text file ]`

Example: `$ python filler.py data.txt`
