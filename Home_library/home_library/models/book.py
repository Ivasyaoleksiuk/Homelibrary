# models/book.py
from models.material import Material


class Book(Material):
    """
    Клас, що представляє книгу у бібліотеці.
    Успадковується від базового класу Material.
    """

    def __init__(self, title, author, year, publisher, isbn=None, pages=None):
        """
        Ініціалізує нову книгу.

        Args:
            title (str): Назва книги
            author (str): Автор книги
            year (int): Рік видання
            publisher (str): Видавництво
            isbn (str, optional): ISBN книги
            pages (int, optional): Кількість сторінок
        """
        super().__init__(title, author, year)
        self.publisher = publisher
        self.isbn = isbn
        self.pages = pages

    def get_type(self):
        """
        Повертає тип матеріалу.

        Returns:
            str: "Книга"
        """
        return "Книга"

    def __str__(self):
        """
        Повертає рядкове представлення книги.

        Returns:
            str: Текстове представлення книги з додатковою інформацією
        """
        base_info = super().__str__()
        additional_info = []

        if self.publisher:
            additional_info.append(f"Видавництво: {self.publisher}")
        if self.isbn:
            additional_info.append(f"ISBN: {self.isbn}")
        if self.pages:
            additional_info.append(f"Сторінок: {self.pages}")

        if additional_info:
            return f"{base_info}\n    " + "\n    ".join(additional_info)
        return base_info

    def matches(self, query):
        """
        Перевіряє, чи відповідає книга пошуковому запиту.
        Перевіряє базові поля, видавництво, ISBN та кількість сторінок.

        Args:
            query (str): Пошуковий запит

        Returns:
            bool: True, якщо книга відповідає запиту, інакше False
        """
        base_match = super().matches(query)
        query = query.lower()

        additional_match = (
                (self.publisher and query in self.publisher.lower()) or
                (self.isbn and query in self.isbn.lower()) or
                (self.pages and query in str(self.pages))
        )

        return base_match or additional_match