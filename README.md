# Dustbin IoT Database Filler

### A lightweight program to send the data from the dustbin sensors to the web app database.

<br>

**Input file with data:**
- Data Format: json
- File Format: plain text


**Settup:**
- Install Heroku CLI | https://devcenter.heroku.com/articles/heroku-cli
- Install Python 3.8.2 | https://www.python.org/downloads/
- Install PostgreSQL | `$ pip install psycopg2`

The command composition for launch the database filler is: <br>
`[ python interpreter ] [ script file ] [ text file ]`

Command example: `$ python path/filler.py path/data.txt`
> Note that no path is need if both files are in the same directory.

<br>

Required login to heroku (only first time)
