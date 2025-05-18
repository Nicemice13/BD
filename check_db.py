from connect_sqlalchemy import get_db, engine
from sqlalchemy import inspect, text

# Получаем инспектор для базы данных
inspector = inspect(engine)

# Получаем список всех таблиц
tables = inspector.get_table_names()
print("Таблицы в базе данных:")
for table in tables:
    print(f"- {table}")
    # Получаем список столбцов для каждой таблицы
    columns = inspector.get_columns(table)
    print("  Столбцы:")
    for column in columns:
        print(f"    - {column['name']} ({column['type']})")
    print()

# Пример запроса к таблице categories
db = get_db()
try:
    result = db.execute(text("SELECT * FROM categories LIMIT 3")).fetchall()
    print("\nПример данных из таблицы categories:")
    for row in result:
        print(row)
except Exception as e:
    print(f"Ошибка при запросе к таблице categories: {e}")