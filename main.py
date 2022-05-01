from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Job
from flask import url_for, request, render_template, redirect
from data.forms import *


def check_user(name, password):
    user = db_sess.query(User).filter(name == User.email).first()
    if user and user.hashed_password == password:
        return True
    return False


def get_info():
    global db_sess
    images_dick = {'large-pool': ['large-pool.png', 'Большой бассейн']}
    days = {'monday': 'Понедельник'}
    image, russian_name = './static/images/' + images_dick[place][0], images_dick[place][1]
    print(place, day, time)
    jobs = db_sess.query(Job).filter(place == Job.place).all()
    for job in jobs:
        if job.time == time.split(':')[0] and job.day == day:
            break
    count_already = job.already
    count_max = job.max
    can_write = 1 if count_already < count_max else 0
    return render_template('info.html', title='Большой бассейн', can_write=can_write, day_of_the_week=days[day], name=russian_name, time=time, day=day, place=place, image=image, count_already=count_already, count_max=count_max)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'her_vam_a_ne_kluch'
db_sess = 0
place = 'large-pool'
day = 'monday'
time = '7:00'


@app.route('/')
def start():
    return render_template('test.html', title='Главная страница')

@app.route('/write')
def write():
    return render_template('write.html', title='Вы записаны')
########################################################################################################################
def shedule():
    dick = {'large-pool': 'Большой бассейн', 'ice': 'Ледовая арена'}
    image_path = f"./static/images/shedule_{place.replace('-', '_')}.png"
    return render_template('shedule.html', title=dick[place], image=image_path)

@app.route('/large-pool')
def place1():
    global place
    place = 'large-pool'
    return shedule()


@app.route('/ice')
def place2():
    global place
    place = 'ice'
    return shedule()


@app.route('/monday')
def day1():
    global day
    day = 'monday'
    return render_template('choose-time.html', title='Время записи')


@app.route('/tuesday')
def day2():
    global day
    day = 'tuesday'
    return render_template('choose-time.html', title='Время записи')


@app.route('/wednesday')
def day3():
    global day
    day = 'wednesday'
    return render_template('choose-time.html', title='Время записи')


@app.route('/thursday')
def day4():
    global day
    day = 'thursday'
    return render_template('choose-time.html', title='Время записи')


@app.route('/friday')
def day5():
    global day
    day = 'friday'
    return render_template('choose-time.html', title='Время записи')


@app.route('/saturday')
def day6():
    global day
    day = 'saturday'
    return render_template('choose-time.html', title='Время записи')


@app.route('/sunday')
def day7():
    global day
    day = 'sunday'
    return render_template('choose-time.html', title='Время записи')

@app.route('/8')
def time8():
    global time
    time = '8:00'
    return get_info()

@app.route('/9')
def time9():
    global time
    time = '9:00'
    return get_info()


########################################################################################################################

@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           username=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    check = ''
    form = LoginForm()
    if form.validate_on_submit():
        name, password = request.form['username'], request.form['password']
        if check_user(name, password):
            return redirect('/success')
        else:
            check = 'Неправильный логин или пароль'
    return render_template('login.html', title='Авторизация', form=form, check=check)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name, password = request.form['username'], request.form['password']
        if check_user(name, password):
            return redirect('/success')
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/success')
def success():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Пfff!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                  </body>
                </html>"""

##########################################################################################
@app.route('/form_sample', methods=['POST', 'GET'])
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
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">В каком вы классе</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>7</option>
                                          <option>8</option>
                                          <option>9</option>
                                          <option>10</option>
                                          <option>11</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
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
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"

@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
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
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1>Загрузим файл</h1>
                            <form method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        print(f.read())
        return "Форма отправлена"

@app.route('/sample_page')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                  </body>
                </html>"""

@app.route('/greeting/<username>')
def greeting(username):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Привет, {username}</title>
                  </head>
                  <body>
                    <h1>Привет, {username}!</h1>
                  </body>
                </html>'''
##########################################################################################
def find_similar():
    pass

def main():
    global db_sess
    db_session.global_init("db/users.db")
    db_sess = db_session.create_session()
    app.run(port=8080, host='127.0.0.1')

    for user in db_sess.query(User).all():
        print(user.name)

    '''
    for i in ['ice', 'large-pool', 'gym', 'universal']:
        for k in [8, 9, 10, 11, 12, 20, 21]:
            for j in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                job = Job()
                job.place, job.day, job.time, job.already, job.max = i, j, k, 0, 12
                db_sess.add(job)
                
                user = User()
                user.email = "aue2005@mars.org"
                user.hashed_password = "1234"
                db_sess.add(user)
                
    db_sess.commit()
    '''
    '''
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    db_sess.add(job)
    user = User()
    user.email = "aue2005@mars.org"
    user.hashed_password = "1234"
    db_sess.add(user)

    db_sess.commit()
    '''

if __name__ == '__main__':
    main()