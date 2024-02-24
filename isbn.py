class ISBN:
    def __init__(self, isbn):
        self.isbn = self._clean_isbn(isbn)

    def _clean_isbn(self, isbn):
        # Remove any hyphens or spaces from the ISBN
        return isbn.replace("-", "").replace(" ", "")

    def validate(self):
        """
        Validates the ISBN.

        Returns:
            bool: True if the ISBN is valid, False otherwise.
        """
        if len(self.isbn) == 10:
            return self._validate_isbn10()
        elif len(self.isbn) == 13:
            return self._validate_isbn13()
        else:
            return False

    def _validate_isbn10(self):
        """
        Validates the ISBN-10.

        Returns:
            bool: True if the ISBN-10 is valid, False otherwise.
        """
        if not self.isbn[:-1].isdigit():
            return False

        total = sum(int(digit) * (i + 1) for i, digit in enumerate(self.isbn[:-1]))
        check_digit = self.isbn[-1]
        if check_digit == 'X':
            total += 10 * 10
        else:
            total += int(check_digit) * 10

        return total % 11 == 0

    def _validate_isbn13(self):
        """
        Validates the ISBN-13.

        Returns:
            bool: True if the ISBN-13 is valid, False otherwise.
        """
        if not self.isbn.isdigit():
            return False

        total = sum(int(digit) * (3 if i % 2 == 0 else 1) for i, digit in enumerate(self.isbn[:-1]))
        check_digit = self.isbn[-1]
        calculated_check_digit = (10 - (total % 10)) % 10

        return int(check_digit) == calculated_check_digit

    def __str__(self):
        return f"{self.isbn + ' ' if self.isbn else ''}"