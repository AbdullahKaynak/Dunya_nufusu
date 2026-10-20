import os
from dotenv import load_dotenv
import sqlalchemy as sq

# .env dosyasındaki gizli değişkenleri projeye yükle
load_dotenv()

# Bilgileri güvenli bir şekilde değişkenlere alalım
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


def get_connection():
  # Bağlantı cümlesini güvenli değişkenlerle oluşturalım
  connection_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
  engine = sq.create_engine(connection_url)
  return engine