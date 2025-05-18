from connect_sqlalchemy import get_db
from sqlalchemy import text


# 1) Получить письма в интервале(id1, id2)
def get_letters_in_range(id1, id2):
    db = get_db()
    letters = db.execute(text("SELECT * FROM categories WHERE id BETWEEN :id1 AND :id2"), {"id1": id1, "id2": id2}).fetchall()
    if letters:
        print(f"Найдено записей в диапазоне от {id1} до {id2}:")
        for letter in letters:
            print(letter)
    else:
        print(f"Записей в диапазоне от {id1} до {id2} не найдено")

    return letters


# 2) Получить письма в которых есть слово "письма"
def get_users_letters():
    db = get_db()
    # Используем оператор LIKE для поиска подстроки в теле или названии письма
    # Сначала проверим, какие таблицы и столбцы есть в базе данных
    try:
        # Пробуем найти письма в таблице categories, предполагая, что там есть столбцы name и description
        letters = db.execute(text("""
            SELECT * FROM categories
            WHERE name LIKE :keyword
            OR description LIKE :keyword
        """), {"keyword": "%письма%"}).fetchall()

        if letters:
            print(f"Найдено записей: {len(letters)}")
            for letter in letters:
                print(letter)
        else:
            print("Записей с ключевым словом 'письма' не найдено")
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        # Выведем все записи из таблицы categories для анализа
        print("\nСодержимое таблицы categories:")
        all_categories = db.execute(text("SELECT * FROM categories")).fetchall()
        for cat in all_categories:
            print(cat)


# 3) Отсортировать вывод писем по id по убыванию
def get_letters_sorted_in_python():
    db = get_db()
    # Используем оператор ORDER BY для сортировки по убыванию id
    letters = db.execute(text("SELECT * FROM categories ORDER BY id DESC")).fetchall()
    sorted_leters = sorted(letters, key=lambda x: x[0], reverse=True)
    print("Отсортированные записи по убыванию id:")
    for letter in sorted_leters:
        print(letter)
    return sorted_leters


# 4) Отсортировать вывод писем по алфавиту темы
def get_letters_sorted_in_subject():
    db = get_db()
    letters = db.execute(text("SELECT * FROM categories ORDER BY name ASC")).fetchall()
    print("Отсортированные письма по алфавиту темы:")
    for letter in letters:
        print(letter)
    return letters


# 5) Добавить новую строчку в таблицу categories
def add_new_category():
    db = get_db()
    category_name = "Билеты"

    # Проверяем, существует ли уже такая категория
    existing = db.execute(text("SELECT * FROM categories WHERE name = :name"),
                         {"name": category_name}).fetchone()

    if existing:
        print(f"Категория '{category_name}' уже существует:")
        print(existing)
        return existing

    # Если категории нет, добавляем её
    try:
        db.execute(text("""
            INSERT INTO categories (name, description)
            VALUES (:name, :description)
        """), {"name": category_name, "description": "Билеты на мероприятия"})
        db.commit()
        print(f"Новая категория '{category_name}' добавлена в базу данных")

        # Получаем добавленную запись для проверки
        new_category = db.execute(text("SELECT * FROM categories WHERE name = :name"),
                                {"name": category_name}).fetchone()
        print("Добавленная запись:", new_category)

        return new_category
    except Exception as e:
        print(f"Ошибка при добавлении категории: {e}")
        return None


# Вызываем функции
get_letters_in_range(1, 2)
print(f"Поиск записей с ключевым словом 'письма':")
get_users_letters()
get_letters_sorted_in_python()
get_letters_sorted_in_subject()
add_new_category()