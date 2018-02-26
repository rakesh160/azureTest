import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



# put them all together as a string that shows SQLAlchemy where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://datavirt:D@t@Virt@usilapphad05/_Stage_GoogleAnalytics'


# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

# this route will test the database connection and nothing more
@app.route('/select')
def testdb():
    try:
        db.session.query("1").from_statement("SELECT 1").all()
        return '<h1>It works.</h1>'
    except Exception as ex:
        return ex

if __name__ == '__main__':
    app.run(debug=True)