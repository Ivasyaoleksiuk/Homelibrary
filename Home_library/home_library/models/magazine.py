from models.material import Material


class Magazine(Material):
    def __init__(self, title, publisher, year, issue, frequency=None, category=None):
        super().__init__(title, publisher, year)
        self.issue = issue
        self.frequency = frequency
        self.category = category

    def get_type(self):
        return "Журнал"

    def __str__(self):
        base_info = f"Журнал: '{self.title}' (Видавець: {self.author}, {self.year}, Випуск: {self.issue})"
        additional_info = []

        if self.frequency:
            additional_info.append(f"Періодичність: {self.frequency}")
        if self.category:
            additional_info.append(f"Категорія: {self.category}")

        if additional_info:
            return f"{base_info}\n    " + "\n    ".join(additional_info)
        return base_info

    def matches(self, query):
        base_match = super().matches(query)
        query = query.lower()

        additional_match = (
                (self.issue and query in self.issue.lower()) or
                (self.frequency and query in self.frequency.lower()) or
                (self.category and query in self.category.lower())
        )

        return base_match or additional_match