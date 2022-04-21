from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/menu')
def login():
    return render_template('menu.html')


@app.route('/info')
def lol():
    return render_template('info.html')


@app.route('/katalog')
def kat():
    return render_template('kat.html')


@app.route('/gallereya')
def gal():
    return render_template('gallereya.html')


@app.route('/katalog/gameplay')
def kat_1():
    return render_template('katalog/gameplay.html')


@app.route('/katalog/rejim')
def kat_2():
    return render_template('katalog/rejim.html')


@app.route('/katalog/lavels')
def kat_3():
    return render_template('katalog/lavels.html')


@app.route('/katalog/secrets')
def kat_4():
    return render_template('katalog/secrets.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
