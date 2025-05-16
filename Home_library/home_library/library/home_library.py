from models.book import Book
from models.article import Article
from models.magazine import Magazine


class HomeLibrary:

    def __init__(self):
        self.materials = []

    def add_material(self, material):
        if not self._is_unique(material):
            raise ValueError(
                f"Матеріал з назвою '{material.title}' та автором '{material.author}' вже існує в бібліотеці")

        self.materials.append(material)
        return True

    def _is_unique(self, material):
        for existing_material in self.materials:
            if (existing_material.title.lower() == material.title.lower() and
                    existing_material.author.lower() == material.author.lower()):
                return False
        return True

    def remove_material(self, index):
        if index < 0 or index >= len(self.materials):
            raise IndexError("Індекс виходить за межі списку матеріалів")

        return self.materials.pop(index)

    def get_all_materials(self):
        return self.materials

    def find_materials(self, query):
        if not query:
            return []

        return [material for material in self.materials if material.matches(query)]

    def sort_materials(self, key='title', reverse=False):
        if key not in ['title', 'author', 'year']:
            raise ValueError("Неприпустимий ключ сортування. Використовуйте 'title', 'author' або 'year'")

        sorted_materials = sorted(self.materials, key=lambda x: getattr(x, key), reverse=reverse)
        return sorted_materials

    def get_by_type(self, material_type):
        type_mapping = {
            'book': Book,
            'article': Article,
            'magazine': Magazine
        }

        if material_type.lower() not in type_mapping:
            raise ValueError("Неприпустимий тип матеріалу. Використовуйте 'book', 'article' або 'magazine'")

        return [material for material in self.materials
                if isinstance(material, type_mapping[material_type.lower()])]