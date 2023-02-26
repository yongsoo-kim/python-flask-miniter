from sqlalchemy import create_engine, text

db = {
    'user': 'root',
    'password': 'sesame',
    'host': 'localhost',
    'port': 3306,
    'database': 'miniter'
}

db_url = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
db = create_engine(db_url, encoding='utf-8', max_overflow=0)