import sqlite3

DB_NAME = 'cookies.db'

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn
def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS cookies(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_page TEXT,
        cookie_session TEXT 
        )''')
    conn.commit()
    conn.close()
def insert_to_db(name, cookie):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO cookies (name_page, cookie_session) VALUES(?, ?)", (name, cookie))
    conn.commit()
    conn.close()
def show_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT name_page, cookie_session FROM cookies")
    show_me = cur.fetchall()
    for row in show_me:
        print(f"Page: {row['name_page']} Cookie session: {row['cookie_session']}")
    conn.close()