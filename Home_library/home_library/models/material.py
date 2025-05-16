from abc import ABC, abstractmethod
from datetime import datetime
from utils.validators import validate_year, validate_text_length


class Material(ABC):

    def __init__(self, title, author, year):
        self.title = validate_text_length(title, "Назва", 100)
        self.author = validate_text_length(author, "Автор", 50)
        self.year = validate_year(year)

    @abstractmethod
    def get_type(self):
        pass

    def __str__(self):
        return f"{self.get_type()}: '{self.title}' ({self.author}, {self.year})"

    def matches(self, query):
        query = query.lower()
        return (query in self.title.lower() or
                query in self.author.lower() or
                query in str(self.year))