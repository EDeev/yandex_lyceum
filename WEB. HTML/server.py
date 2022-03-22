from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def gimn():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promo():
    return '</br>'.join(['Человечество вырастает из детства.',
                         'Человечеству мала одна планета.',
                         'Мы сделаем обитаемыми безжизненные пока планеты.',
                         'И начнем с Марса!', 'Присоединяйся!'])


@app.route('/image_mars')
def img():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/planet.jpg')}"></br>
                        <a>Вот она какая, красная планета.</a>
                      </body>
                    </html>"""


@app.route('/promotion_image')
def promo_img():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1 class="red" >Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/planet.jpg')}"></br>
                        <div class="font black"><b>Человечество вырастает из детства.</b></div></br>
                        <div class="font green"><b>Человечеству мала одна планета.</b></div></br>
                        <div class="font gray"><b>Мы сделаем обитаемыми безжизненные пока планеты.</b></div></br>
                        <div class="font yellow"><b>И начнем с Марса!</b></div></br>
                        <div class="font red"><b>Присоединяйся!</b></div>
                      </body>
                    </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 style="text-align:center">Анкета претендента</h1>
                            <h2 style="text-align:center">на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="text" placeholder="Введите фамилию" name="text1">
                                    <input type="text" class="form-control" id="text" placeholder="Введите имя" name="text2"></br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее оконченное</option>
                                          <option>Среднее неоконченное</option>
                                          <option>Высшее оконченное</option>
                                          <option>Высшее неоконченное</option>
                                        </select>
                                     </div></br>
                                    <label for="classSelect">Какие у Вас есть профессии?</label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept1">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label></br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept2">
                                        <label class="form-check-label" for="acceptRules">Инженер-строитель</label></br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept3">
                                        <label class="form-check-label" for="acceptRules">Пилот</label></br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept4">
                                        <label class="form-check-label" for="acceptRules">Метеоролог</label></br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept5">
                                        <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label></br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept6">
                                        <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label></br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept7">
                                        <label class="form-check-label" for="acceptRules">Врач</label></br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept8">
                                        <label class="form-check-label" for="acceptRules">Экзобиолог</label></br>
                                    </div></br>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male">
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div></br>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div></br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label></br>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div></br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div></br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print("Фамилия -", request.form.get('text1'))
        print("Имя -", request.form.get('text2'))
        print("Почта -", request.form.get('email'))
        print("Образование -", request.form.get('class'))
        prof = []
        typis = {'accept1': "Инженер-исследователь", 'accept2': "Инженер-строитель", 'accept3': "Пилот",
                 'accept4': "Метеоролог", 'accept5': 'Инженер по жизнеобеспечению',
                 'accept6': 'Инженер по радиационной защите', 'accept7': "Врач", 'accept8': "Экзобиолог"}
        for i in typis:
            a = request.form.get(i)
            if a:
                prof.append(typis[i])
        print("Профкссия(-и):", ", ".join(prof))
        print("Пол -", request.form.get('sex'))
        print("Причины участия -", request.form.get('about'))
        print("Фото -", request.form.get('file'))
        if request.form.get('accept'):
            print("Подписан на программу")
        else:
            print("Отказался от программы")
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1 class="font">Моё предложение: {planet_name}</h1>
                        <h1>Эта планета близка к Земле;</h1>
                        <div class="font green"><b>На ней много необходимых ресурсов;</b></div></br>
                        <div class="font gray"><b>На ней есть вода и атмосфера;</b></div></br>
                        <div class="font yellow"><b>На ней есть небольшое магнитное поле;</b></div></br>
                        <div class="font red"><b>Наконец, она просто красива!</b></div></br>
                      </body>
                    </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1 class="font">Результаты отбора</h1>
                        <h1>Претендента на участие в миссии {nickname}:</h1>
                        <div class="font green"><b>Поздравляем! Ваш рейтинг после {level} этапа отбора</b></div>
                        <h1>составляет {rating}!</h1>
                        <div class="font yellow"><b>Желаем удачи!</b></div></br>
                      </body>
                    </html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 style="text-align:center">Загрузка фотографии</h1>
                            <h2 style="text-align:center">для участия в миссии</h2>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label></br>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div></br>
                                    <img class="width" src="{url_for('static', filename='img/img.png')}"></br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        if f:
            with open("static/img/img.png", "wb") as file:
                file.write(f.read())
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 style="text-align:center">Загрузка фотографии</h1>
                            <h2 style="text-align:center">для участия в миссии</h2>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label></br>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div></br>
                                    <img class="width" src="{url_for('static', filename='img/img.png')}"></br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
