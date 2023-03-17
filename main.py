from app import created_app
from config import config

enviroment = config.get('development')
app = created_app(enviroment)

if __name__ == "__main__":
    app.run()
