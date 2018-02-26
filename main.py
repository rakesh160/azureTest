from flask import Flask
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
   if(word != 'admin'):
      return redirect(url_for('hello_name', name=word))
   else:
      return redirect(url_for('hello_name_default'))

if __name__ == '__main__':
  app.run()
