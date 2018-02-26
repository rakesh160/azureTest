from flask import Flask
app = Flask(__name__)

@app.route('/default')
def hello_world():
  return 'Hello, World!'

@app.route('/fellows')
def hello_world():
  return 'Hello, World! fellows'

if __name__ == '__main__':
  app.run()
