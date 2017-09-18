from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, VSTS!'

@app.route('/branch')
def hello_world():
  return 'Found branch!'

if __name__ == '__main__':
  app.run()
