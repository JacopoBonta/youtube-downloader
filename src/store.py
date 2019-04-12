import sqlite3
import datetime

FILE_STATUSES = ['PENDING', 'READY', 'DOWNLOAD_ERROR']

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
    )''')
  
  def query(self, str, values=()):
    
    self.conn = sqlite3.connect(self.db_file)
    self.c    = self.conn.cursor()
    
    res = self.c.execute(str, values)
    
    self.conn.commit()

    return res
  
  def log(self, level, message):
    
    date = datetime.datetime.now()
    
    r = self.query('''INSERT INTO logs (date, level, message) VALUES (?,?,?)''', (str(date), level, message))

    return r.lastrowid
  
  def add_download(self, url):
    
    date = datetime.datetime.now()
    
    r = self.query('''INSERT INTO downloads (date, url, status, time) VALUES (?,?,?,?)''', (str(date), url, 'PENDING'))

    return r.lastrowid
  
  def set_status(self, download_id, status):

    if status not in FILE_STATUSES:
      raise Exception('Invalid status')
    
    r = self.query('''UPDATE downloads SET status = ? WHERE id = ?''', ('READY', download_id))

    return r.lastrowid
