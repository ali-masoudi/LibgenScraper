class Author:
    id_counter = 1

    def __init__(self, name):
        self.id = Author.id_counter
        Author.id_counter += 1
        self.title = None
        self.prefix = None
        self.first_name = None
        self.middle_names = []
        self.last_name = None
        self.suffix = None

        self.parse_name(name)

    def parse_name(self, name):
        parts = name.split('(')
        name_part = parts[0].strip()
        if len(parts) > 1:
            self.suffix = parts[1].split(')')[0].strip()

        name_parts = name_part.split(' ')
        for part in name_parts:
            if part.endswith('.'):
                self.title = part
            elif part.endswith(','):
                self.prefix = part[:-1]
            elif part.startswith('.'):
                self.suffix = part[1:]
            else:
                if self.first_name is None:
                    self.first_name = part
                elif self.last_name is None:
                    self.last_name = part
                else:
                    self.middle_names.append(part)

    def __str__(self):
        middle_names_str = " ".join(self.middle_names) if self.middle_names else ""
        return f"{self.title} {self.prefix} {self.first_name} {middle_names_str} {self.last_name} {self.suffix}"

# Prof. Robert D. M. Accola (auth.)
# Prof. Dr. Heinz Zemanek (auth.), Andrei P. Ershov, Donald E. Knuth (eds.)