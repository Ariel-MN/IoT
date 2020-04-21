# IoT
Dustbin IoT Database Filler

- Data Format: json
- File Format: plain text
- Requeriments: python, psycopg2
- In filler.py find 'con.autocommit' and set it equal to True

The command for launch the db filler composition is: <br>
`[ interpreter ] [ script file ] [ text file ]`
Example: `python filler.py data.txt`
