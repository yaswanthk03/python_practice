import sqlite3

DATABASE_NAME = 'url_shortener'

def init_db():
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS urls(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     original_url TEXT NOT NULL,
                     short_code TEXT UNIQUE NOT NULL,
                     click_count INTEGER DEFAULT 0
                     )
        ''')

def insert_url(url, short_code):
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.execute('''
            INSERT INTO urls (original_url, short_code)
            VALUES (?, ?)                   
        ''', (url, short_code))
        

def get_url(short_code):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cur = conn.execute('''
                    SELECT original_url
                    FROM urls
                    WHERE short_code = ?
                ''', (short_code, ))
        return cur.fetchone()

def increment_visit_click_count(short_code):
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.execute('''
             UPDATE urls 
             SET click_count = click_count + 1
             WHERE short_code = ?           
        ''', (short_code, ))

def get_all_url():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cur = conn.execute('''
                        SELECT original_url, short_code, click_count
                        FROM urls
                        ORDER BY id DESC
                ''')
        return cur.fetchall()

def delete_url_by_short_code(short_code):
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.execute('''
                        DELETE 
                        FROM urls
                        WHERE short_code = ?
                ''', (short_code, ))
        