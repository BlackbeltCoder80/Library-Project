class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def __str__(self):
        return f"{self.name} - {self.biography}"