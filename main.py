from flask import render_template, Flask
from data.db_session import *
from data.users import *
from data.jobs import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    params = {}
    global_init("db/mars_explorer.db")
    with create_session() as db_sess:
        users = db_sess.query(User).all()
        jobs = db_sess.query(Jobs).all()
    params['users'] = users
    params['jobs'] = jobs
    return render_template('table.html', **params)




if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')