import os
import sys
from models.book import Book
from models.article import Article
from models.magazine import Magazine
from library.home_library import HomeLibrary


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title):
    print(f"\n{'=' * 50}")
    print(f"{title.center(50)}")
    print(f"{'=' * 50}\n")


def display_materials(materials, start_index=0):
    if not materials:
        print("Список порожній.")
        return

    print(f"Всього матеріалів: {len(materials)}")
    for i, material in enumerate(materials, start=start_index):
        print(f"[{i}] {material}")
        print("-" * 50)


def get_safe_input(prompt, convert_type=str, default=None):
    while True:
        try:
            user_input = input(prompt)
            if user_input.strip() == "" and default is not None:
                return default
            return convert_type(user_input)
        except ValueError:
            print(f"Помилка: введіть правильне значення типу {convert_type.__name__}")
        except KeyboardInterrupt:
            print("\nОперацію скасовано.")
            return default


def add_book(library):
    print_header("Додавання нової книги")

    try:
        title = get_safe_input("Назва книги: ")
        author = get_safe_input("Автор: ")
        year = get_safe_input("Рік видання: ", int)
        publisher = get_safe_input("Видавництво: ")
        isbn = get_safe_input("ISBN (необов'язково): ", default="")
        pages = get_safe_input("Кількість сторінок (необов'язково): ", int, default=None)

        book = Book(title, author, year, publisher, isbn, pages)
        library.add_material(book)
        print("Книгу успішно додано до бібліотеки!")

    except ValueError as e:
        print(f"Помилка: {e}")
    except KeyboardInterrupt:
        print("\nОперацію скасовано.")


def add_article(library):
    print_header("Додавання нової статті")

    try:
        title = get_safe_input("Назва статті: ")
        author = get_safe_input("Автор: ")
        year = get_safe_input("Рік публікації: ", int)
        journal = get_safe_input("Назва журналу: ")
        volume = get_safe_input("Том (необов'язково): ", default="")
        issue = get_safe_input("Випуск (необов'язково): ", default="")
        pages = get_safe_input("Сторінки (необов'язково): ", default="")

        article = Article(title, author, year, journal, volume, issue, pages)
        library.add_material(article)
        print("Статтю успішно додано до бібліотеки!")

    except ValueError as e:
        print(f"Помилка: {e}")
    except KeyboardInterrupt:
        print("\nОперацію скасовано.")


def add_magazine(library):
    print_header("Додавання нового журналу")

    try:
        title = get_safe_input("Назва журналу: ")
        publisher = get_safe_input("Видавець: ")
        year = get_safe_input("Рік видання: ", int)
        issue = get_safe_input("Номер випуску: ")
        frequency = get_safe_input("Періодичність (необов'язково): ", default="")
        category = get_safe_input("Категорія (необов'язково): ", default="")

        magazine = Magazine(title, publisher, year, issue, frequency, category)
        library.add_material(magazine)
        print("Журнал успішно додано до бібліотеки!")

    except ValueError as e:
        print(f"Помилка: {e}")
    except KeyboardInterrupt:
        print("\nОперацію скасовано.")


def remove_material(library):
    print_header("Видалення матеріалу")

    materials = library.get_all_materials()
    if not materials:
        print("Бібліотека порожня.")
        return

    display_materials(materials)

    try:
        index = get_safe_input("Введіть індекс матеріалу для видалення (або 'q' для скасування): ")
        if index == 'q':
            print("Операцію скасовано.")
            return

        index = int(index)
        material = library.remove_material(index)
        print(f"Матеріал видалено: {material}")

    except (ValueError, IndexError) as e:
        print(f"Помилка: {e}")
    except KeyboardInterrupt:
        print("\nОперацію скасовано.")


def search_materials(library):
    print_header("Пошук матеріалів")

    query = get_safe_input("Введіть пошуковий запит: ")
    if not query:
        print("Пошуковий запит не може бути порожнім.")
        return

    results = library.find_materials(query)

    print_header(f"Результати пошуку за запитом '{query}'")
    display_materials(results)


def sort_materials(library):
    print_header("Сортування матеріалів")

    if not library.get_all_materials():
        print("Бібліотека порожня.")
        return

    print("Варіанти сортування:")
    print("1. За назвою")
    print("2. За автором")
    print("3. За роком")

    try:
        choice = get_safe_input("Виберіть варіант сортування (1-3): ", int)
        if choice not in [1, 2, 3]:
            print("Невірний вибір.")
            return

        order = get_safe_input("Порядок сортування (1 - за зростанням, 2 - за спаданням): ", int)
        if order not in [1, 2]:
            print("Невірний вибір.")
            return

        key_mapping = {1: 'title', 2: 'author', 3: 'year'}
        reverse = (order == 2)

        sorted_materials = library.sort_materials(key_mapping[choice], reverse)

        order_text = "спаданням" if reverse else "зростанням"
        print_header(f"Матеріали відсортовані за {key_mapping[choice]} (за {order_text})")
        display_materials(sorted_materials)

    except ValueError as e:
        print(f"Помилка: {e}")
    except KeyboardInterrupt:
        print("\nОперацію скасовано.")


def display_by_type(library):
    print_header("Відображення матеріалів за типом")

    print("Типи матеріалів:")
    print("1. Книги")
    print("2. Статті")
    print("3. Журнали")

    try:
        choice = get_safe_input("Виберіть тип матеріалу (1-3): ", int)
        if choice not in [1, 2, 3]:
            print("Невірний вибір.")
            return

        type_mapping = {1: 'book', 2: 'article', 3: 'magazine'}
        materials = library.get_by_type(type_mapping[choice])

        type_names = {1: "Книги", 2: "Статті", 3: "Журнали"}
        print_header(type_names[choice])
        display_materials(materials)

    except ValueError as e:
        print(f"Помилка: {e}")
    except KeyboardInterrupt:
        print("\nОперацію скасовано.")


def main():
    library = HomeLibrary()

    try:
        library.add_material(Book("1984", "Джордж Орвелл", 1949, "Secker & Warburg", "978-0451524935", 328))
        library.add_material(Book("Майстер і Маргарита", "Михайло Булгаков", 1967, "YMCA Press", "978-0141180144", 384))
        library.add_material(
            Article("Штучний інтелект: сучасні підходи", "Петро Іваненко", 2023, "Наука і технології", "12", "3",
                    "45-67"))
        library.add_material(
            Magazine("National Geographic", "National Geographic Society", 2023, "6", "Щомісячно", "Наука"))
    except ValueError:
        pass

    while True:
        clear_screen()
        print_header("ДОМАШНЯ БІБЛІОТЕКА")

        print("1. Додати книгу")
        print("2. Додати статтю")
        print("3. Додати журнал")
        print("4. Видалити матеріал")
        print("5. Переглянути всі матеріали")
        print("6. Пошук за властивостями")
        print("7. Сортування матеріалів")
        print("8. Відображення за типом")
        print("0. Вихід")

        try:
            choice = get_safe_input("\nВаш вибір: ", int)

            if choice == 0:
                print("\nДякуємо за використання Домашньої бібліотеки!")
                break

            actions = {
                1: add_book,
                2: add_article,
                3: add_magazine,
                4: remove_material,
                5: lambda lib: display_materials(lib.get_all_materials()),
                6: search_materials,
                7: sort_materials,
                8: display_by_type
            }

            if choice in actions:
                actions[choice](library)
            else:
                print("Невірний вибір. Спробуйте ще раз.")

            input("\nНатисніть Enter, щоб продовжити...")

        except ValueError:
            print("Введіть числове значення.")
            input("\nНатисніть Enter, щоб продовжити...")
        except KeyboardInterrupt:
            print("\n\nПрограму завершено.")
            sys.exit(0)


if __name__ == "__main__":
    main()