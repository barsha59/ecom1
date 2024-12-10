from flask import Flask

app = Flask(__name__)
@app.route('/')
def main():
    return "<h1>hi</h1>"

@app.route('about/<name>')
def home(name):
    return f"Hello, my nam is {name}"

if __name__ == '__main__':
    app.run(debug=True)
