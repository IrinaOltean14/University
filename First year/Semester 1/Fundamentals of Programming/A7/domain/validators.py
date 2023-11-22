from datetime import date
from src.domain.errors import StoreExceptions


class MovieValidator:
    def __init__(self):
        pass

    @staticmethod
    def is_genre_valid(genre):
        if genre not in ["Action", "Comedy", "Drama", "Fantasy", "Horror", "Mystery", "Romance", "Sci-Fi", "Thriller", "Western"]:
            return False
        return True

    @staticmethod
    def validate(movie):
        errors = ""
        if not MovieValidator.is_genre_valid(movie.genre):
            errors += 'Invalid movie genre'
        if len(errors) > 0:
            raise StoreExceptions(errors)


class ClientValidator:
    def __init__(self):
        pass

    @staticmethod
    def is_name_valid(name):
        if any(char.isdigit() for char in name) or len(name) < 2:
            return False
        return True

    @staticmethod
    def validate(client):
        errors = ""
        if not ClientValidator.is_name_valid(client.name):
            errors += 'The name of the client is not valid'
        if len(errors) > 0:
            raise StoreExceptions(errors)


class RentalValidator:
    def __init__(self):
        pass

    @staticmethod
    def is_date(possible_date):
        if type(possible_date) != date:
            return False
        return True

    @staticmethod
    def validate(rental):
        errors = ""
        if not RentalValidator.is_date(rental.rental_date):
            errors += 'Invalid rental date '
        if not RentalValidator.is_date(rental.due_date):
            errors += 'Invalid due date'
        if len(errors) > 0:
            raise StoreExceptions(errors)
