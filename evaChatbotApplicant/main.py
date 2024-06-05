from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='test', userName='chenming')

@app.route('/hello')
def hello():
    name = "Hello world!"
    return name

if __name__ == "__main__":
    app.run()