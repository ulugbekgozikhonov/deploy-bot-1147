import sqlite3


def create_tables():
    con = sqlite3.connect("testuchun.db")
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR,
        phone_number VARCHAR,
        chat_id INTEGER
        )""")

  


def get_user_by_chat_id(chat_id):
    con = sqlite3.connect("testuchun.db")
    cur = con.cursor()
    try:
        user = cur.execute("SELECT * FROM users WHERE chat_id=?",(chat_id,)).fetchone()
        con.commit()
        con.close()
        return user
    except Exception as e:
        print(e)
        return False
        
    
    


def register_user(data:dict):
    con = sqlite3.connect("testuchun.db")
    cur = con.cursor()

    try:
        cur.execute("INSERT INTO users(full_name,phone_number,chat_id) VALUES(?,?,?)",
                    (data.get('full_name'),data.get('phone_number'),data.get('chat_id')))
        con.commit()
        return True
    except Exception as exp:
        print(exp)
        return False