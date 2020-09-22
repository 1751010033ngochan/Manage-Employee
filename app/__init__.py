from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Kết nối với cơ sở dữ liệu bằng SQLALCHEMY

app.secret_key = "12345678"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost/db_test?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# Database conected with MySQL
db = SQLAlchemy(app=app)
