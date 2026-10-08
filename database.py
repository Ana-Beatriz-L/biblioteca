"""Conexão com o PostgreSQL. Usada por todos os models."""
import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()  # lê o arquivo .env (que NÃO vai pro GitHub)


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "biblioteca"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", ""),
    )
