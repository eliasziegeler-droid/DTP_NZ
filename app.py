from flask import Flask, g, render_template 
import sqlite3 


DATABASE = 'database.db'




#initialise app
app = Flask(__name__)


def get_db():
    db = getattr(g,'_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


# @app.route('/')
# def home():
#     #homepage
#     db = get_db()
#     cursor = db.cursor()
#     sql = "SELECT * FROM Motorbikes;"
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     return str(results)

@app.route('/')
def home():
#home page- just the ID, Maker, Model amnd Image URL
    sql= """ 
            SELECT Motorbikes.BikeID, Motorbikes.MakerID, Motorbikes.Model, Motorbikes.Cost, Motorbikes.Description,Motorbikes.`Acceleration 0-100 km/h`, Motorbikes.Topspeed, Motorbikes.ImageURL
            FROM Motorbikes 
            JOIN Makers ON Makers.MakerID=MOTORBIKES.MakerID;"""
    results = query_db(sql,(id,),True)
    return render_template("layout.html")


if __name__ == "__main__":
    app.run(debug=True)