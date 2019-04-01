from dotenv import load_dotenv
load_dotenv()

from src.server import app

from src.routes import download
from src.errors import internal_error, invalid_parameters, not_found

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')