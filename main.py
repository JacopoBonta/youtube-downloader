from dotenv import load_dotenv
load_dotenv()
import os

from src.server import app

from src.routes import download
from src.errors import internal_error, invalid_parameters, not_found

ADDRESS = os.getenv('SERVER_ADDRESS')
PORT    = os.getenv('SERVER_PORT')

if __name__ == '__main__':
  app.run(debug=True, host=ADDRESS, port=PORT)