from flask import Flask, redirect, url_for
from sqlalchemy import *

app = Flask(__name__)


@app.route('/hello/<name>')
def hello_name(name):
    hello_name_default()
    return 'Hello %s!' % name


@app.route('/hello')
def hello_name_default():
    return 'Hello default'


@app.route('/helloall/<word>')
def hello_all(word):
    if (word == 'admin'):
        return redirect(url_for('hello_name', name=word))
    else:
        return redirect(url_for('hello_name_default'))


@app.route('/select')
def select():
    engine = create_engine('mysql+pymysql://datavirt:D@t@Virt@usilapphad05/_Stage_GoogleAnalytics?charset=utf8')
    connection = engine.connect()
    result = connection.execute("select username from GA_KB_Activity")
    connection.close()
    return render_template('select.html', data=result)

if __name__ == '__main__':
    app.run()
