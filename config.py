from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 5036
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://fullstack_780b_user:IgRxS2vctOMgCFeGXwlsM5exdwyxPslM@dpg-d3j4ua2dbo4c73861e4g-a.oregon-postgres.render.com/fullstack_780b"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

porta = app.config['PORT']
host = app.config['HOST']

if host == "0.0.0.0":
    host = "localhost"

url = f"http://{host}:{porta}"

# url = "https://trajettoexpressfullstack.onrender.com"

db = SQLAlchemy(app)
