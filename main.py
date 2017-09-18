from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Triggered from VSTS!'

@app.route('/branch')
def view_branch():
  return 'Found branch!'

if __name__ == '__main__':
  app.run()
