class Language:
    id_counter = 1

    def __init__(self, name):
        self.language_id = Language.id_counter
        Language.id_counter += 1
        self.name = name

    def __str__(self):
        return f"{self.name + ' ' if self.name else ''}"
