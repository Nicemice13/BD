from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем подключение к базе данных SQLite
# Если у вас другая БД (PostgreSQL, MySQL и т.д.), измените строку подключения
DATABASE_URL = "sqlite:///email_database.db"

# Создаем движок SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Создаем базовый класс для моделей
Base = declarative_base()

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

# Пример использования
if __name__ == "__main__":
    # Получаем сессию
    db = get_db()
    
    # Получаем информацию о таблицах в базе данных
    inspector = inspect(engine)
    table_names = inspector.get_table_names()
    
    print("Таблицы в базе данных:")
    for table_name in table_names:
        print(f"- {table_name}")
        
    # Закрываем сессию
    db.close()