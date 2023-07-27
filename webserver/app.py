from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def respond():
    # connect to DB
    try:
        connection = psycopg2.connect(host=app.db_hostname, user=app.db_username, password=app.db_password, dbname=app.db_database)
    except Exception as e:
        return "cannot connect to DB "+app.db_database+", error line: <br> "+str(e)
        
    # get data from DB
    try:    
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sales")
        sales = cursor.fetchall()
    except Exception as e:
        connection.close()
        return "cannot pull data from DB "+app.db_hostname+", error line: <br> "+str(e)

    # parse the DB data & respond
    ret = "<h1>Sales:</h1>"
    for sale in sales:
        ret += "<br><h2>"+str(sale[0])+": "+sale[1]+"</h2><br>"
        images = sale[2][1:-1].split("\",\"")
        for image in images:
            ret += "<img src="+image.replace("\"","")+" >"

        connection.close()
    return ret
    

if __name__ == '__main__':
    app.db_hostname = 'db'
    app.db_username = 'username_test'
    app.db_password = 'password_test'
    app.db_database = 'SREALITY'

    app.run(host='0.0.0.0', port=80)