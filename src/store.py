import sqlite3
import datetime

class Store():
  
  def __init__(self, db_file='yd.db'):

    self.db_file  = db_file

    self._init_downloads_table()
    self._init_logs_table()
  
  def __del__(self):
    self.conn.close()
  
  def _init_logs_table(self):
    self.query('''CREATE TABLE IF NOT EXISTS logs (
      id integer PRIMARY KEY AUTOINCREMENT,
      date text NOT NULL,
      level text NOT NULL,
      message text NOT NULL
    )''')
  
  def _init_downloads_table(self):
    self.query('''CREATE TABLE IF NOT EXISTS downloads (
      id integer PRIMARY KEY AUTOINCREMENT,
      date text NOT NULL,
      url text NOT NULL,
      status text NOT NULL,
      time text
    )''')
  
  def query(self, str, values=()):
    
    self.conn = sqlite3.connect(self.db_file)
    self.c    = self.conn.cursor()
    
    res = self.c.execute(str, values)
    
    self.conn.commit()

    return res
  
  def insert_log(self, level, message):
    
    timestamp = datetime.datetime.now().timestamp()
    
    r = self.query('''INSERT INTO logs (date, level, message) VALUES (?,?,?)''', (str(timestamp), level, message))

    return r.lastrowid
  
  def insert_download(self, url, status, time=None):
    
    timestamp = datetime.datetime.now().timestamp()
    
    r = self.query('''INSERT INTO downloads (date, url, status, time) VALUES (?,?,?,?)''', (str(timestamp), url, status, time))

    return r.lastrowid