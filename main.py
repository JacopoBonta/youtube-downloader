from dotenv import load_dotenv
load_dotenv()
import os

from src.store import Store
store = Store()

from src.server import app

import src.routes
import src.errors

ADDRESS = os.getenv('SERVER_ADDRESS')
PORT    = os.getenv('SERVER_PORT')

if __name__ == '__main__':
  app.run(debug=True, host=ADDRESS, port=PORT)