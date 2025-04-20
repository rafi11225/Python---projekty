import bcrypt
import sqlite3
DB_NAME = 'users_v2.db'
#Pobieranie bazy danych

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn
def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS user(
    id_usera INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    hashed_pass BLOB)
    ''')
    cur.execute('''CREATE TABLE IF NOT EXISTS password(
        id_usera INTEGER,
        page TEXT,
        page_pass TEXT
        )''')

    
    conn.commit()
    conn.close()
def validate_pass(passwd):
    if len(passwd) < 8:
        return False
    else:
        return True
def hash_pass (password):
    salt = bcrypt.gensalt()
    pass_hash = bcrypt.hashpw(password.encode("UTF-8"), salt)
    return pass_hash        
def register():
        username = str(input("Podaj nazwę użytkownika: "))
        password = str(input("Wprowadź hasło: "))
        while validate_pass(password) == False:
            password = str(input("Wprowadź dłuższe hasło: "))
        print("Zarejestrowano pomyślnie")
        hashed_password = hash_pass(password)
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO user (username, hashed_pass) VALUES(?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
def login(username, password):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT hashed_pass FROM user WHERE username = ?",(username,)) ##sprawdzenie czy jest to w bazie danych
    u = cur.fetchone()
    if u and bcrypt.checkpw(password.encode('UTF-8'), u['hashed_pass']):
            return True
    else:
            return False
def get_user_id(username):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id_usera FROM user WHERE username = ?",(username,))
    u = cur.fetchone()
    conn.close()
    if u:
        return u['id_usera']
    else:
        return None
def add_pass(user, password):
    if login(user, password) == True:
        id_usera = get_user_id(user)
        page = str(input("Podaj stronę: "))
        page_pass = str(input("Podaj hasło do strony: "))
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO password (id_usera, page, page_pass) VALUES(?, ?, ?)", (id_usera, page, page_pass))
        conn.commit()
        conn.close()
def show_pass(user, password):
    if login(user, password) == True:
        user_id = get_user_id(user)
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT page, page_pass FROM password WHERE id_usera = ?",(user_id,))
        id_u = cur.fetchall()
        for row in id_u:
            print(f"Strona: {row['page']} | Hasło: {row['page_pass']}")
        conn.close()
while True:        
    init_db()
    print("*"*100)
    print("Witaj, co chcesz zrobić?")
    print("1. Dodaj nową bazę haseł \n 2. Odczytaj swoją bazę haseł \n 3. Dodaj nowe hasło do bazy danych \n")
    switch = int(input("Wprowadź numer opcji, którym jesteś zainteresowany: "))
    match(switch):
        case 1:
            print("*"*100)
            register()
        case 2:
            print('*'*100)
            usr = str(input("Podaj nazwę użytkownika: "))
            passwd = str(input("Podaj hasło: "))
            login(usr, passwd)
            while login(usr, passwd)==False:
                usr = str(input("Podaj nazwę użytkownika: "))
                passwd = str(input("Podaj hasło: "))
                login(usr, passwd)
            show_pass(usr,passwd)
        case 3:
            print("*"*100)
            usr = str(input("Podaj nazwę użytkownika: "))
            passwd = str(input("Podaj hasło: "))
            login(usr, passwd)
            while login(usr, passwd)==False:
                usr = str(input("Podaj nazwę użytkownika: "))
                passwd = str(input("Podaj hasło: "))
                login(usr, passwd)
            add_pass(usr, passwd)          

           
