from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/menu')
def login():
    return render_template('menu.html')


@app.route('/info')
def lol():
    return render_template('info.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
