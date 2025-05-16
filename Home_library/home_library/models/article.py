from models.material import Material


class Article(Material):


    def __init__(self, title, author, year, journal, volume=None, issue=None, pages=None):
        super().__init__(title, author, year)
        self.journal = journal
        self.volume = volume
        self.issue = issue
        self.pages = pages

    def get_type(self):
        return "Стаття"

    def __str__(self):
        base_info = super().__str__()
        additional_info = [f"Журнал: {self.journal}"]

        if self.volume:
            additional_info.append(f"Том: {self.volume}")
        if self.issue:
            additional_info.append(f"Випуск: {self.issue}")
        if self.pages:
            additional_info.append(f"Сторінки: {self.pages}")

        return f"{base_info}\n    " + "\n    ".join(additional_info)

    def matches(self, query):
        base_match = super().matches(query)
        query = query.lower()

        additional_match = (
                (self.journal and query in self.journal.lower()) or
                (self.volume and query in self.volume.lower()) or
                (self.issue and query in self.issue.lower()) or
                (self.pages and query in self.pages.lower())
        )

        return base_match or additional_match