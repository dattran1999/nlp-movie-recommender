import psycopg2
import urllib.parse as urlparse
import os

url = urlparse.urlparse(os.environ['DATABASE_URL'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

def connect():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
            )
        conn.set_client_encoding('UTF8')
    except Exception as e:
        print("Unable to connect to the database")
    return conn

if __name__ == "__main__":
    conn = connect()
    
