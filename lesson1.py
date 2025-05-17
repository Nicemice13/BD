from connect_sqlalchemy import get_db
from sqlalchemy import text


def get_users():
    db = get_db()
    categories = db.execute(text("SELECT * FROM categories")).fetchall()
    for category in categories:
        print(category)

def get_user_id(id):
    db = get_db()
    # Используем параметризованный запрос для безопасности
    category = db.execute(text("SELECT * FROM categories WHERE id = :id"), {"id": id}).fetchone()
    print(*category)

# Вызываем функции
get_users()
print("\nПоиск по ID:")
get_user_id(2)


## ДЗ
1) Получить письма в интервале(id1, id2)
2) Получить письма в которых есть слово "письма"
3) Отсортировать вывод писем по id по убыванию
4) Отсортировать вывод писем по алфавиту темы
5) Добавить новую строчку в таблицу categories
