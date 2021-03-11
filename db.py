
from configparser import ConfigParser
import psycopg2
from model.user import User


def get_config(file_name="config.ini", section="postgresql"):
    config = ConfigParser()
    config.read(file_name)
    db_config = {}
    for key, value in config.items(section):
        db_config[key] = value

    return db_config

def db_connect():
    params = get_config()
    conn = psycopg2.connect(**params)
    return conn

def add_user(user_id, first_name, last_name, contact):
    conn = db_connect()
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO employee 
        (user_id, first_name, last_name, contact)
        VALUES 
        (%s, %s, %s, %s)
        """, (user_id, first_name, last_name, contact))
        conn.commit()

def authenticate(username, password):
    conn = db_connect()
    with conn.cursor() as cur:
        cur.execute("""
        SELECT user_id, first_name, last_name, contact, username, password FROM employee
        WHERE username=%s and password=%s
        """, (username, password))
        result = cur.fetchone()
        if result:
            user = User(*result)
            return user
