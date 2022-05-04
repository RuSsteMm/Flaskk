from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/menu')
def login():
    data = [
        'Онлайн энциклопедия по игре Geometry Dash',
        'Игра Geometry Dash вышла в далеком августе 2013 года, но не смотря на это до сих пор имеет абширное сообщество. В игре есть 22 официальных уровней разных сложностей. Также в игре есть редактор уровней где тысячи пользователей создают и выкладывают их.',
        'После просмотра уже имеющих сайтов стало логичным создание хорошой энциклопедии, потому что уже имеющие либо криво переведены на русский, либо ограничены количеством информации, либо сёрфинг по ним оставляет желать лучшего. Я решил взять дело в свои руки...'
    ]
    return render_template('menu.html', param=data)


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
