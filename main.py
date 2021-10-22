from flask import Flask, render_template
import util

app = Flask(__name__)

username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'


@app.route('/')
def index():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor, "SELECT * from basket_a;")
    col_names = [desc[0] for desc in cursor.description]
    log = record[:5]
    util.disconnect_from_db(connection,cursor)
    return render_template('index.html', sql_table = log, table_title=col_names)

@app.route('/api/update_basket_a')
def index2():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    result = util.run_and_commit_sql(cursor, connection, "INSERT INTO basket_a (a, fruit_a) VALUES(5, 'Cherry');")
    if result == 1:
        loght = 'Success!'
    else:
        loght = result
    util.disconnect_from_db(connection,cursor)
    return render_template('index.html', log_html = loght)

@app.route('/api/unique')
def index3():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor, "SELECT * FROM basket_a WHERE fruit_a NOT IN (SELECT fruit_b FROM basket_b) UNION (SELECT * FROM basket_b WHERE fruit_b NOT IN (SELECT fruit_a FROM basket_a))")
    if record != 1:
         loght = record
    col_names = [desc[0] for desc in cursor.description]
    log = record[:5]
    util.disconnect_from_db(connection,cursor)
    return render_template('index.html', sql_table = log, table_title=col_names)


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

