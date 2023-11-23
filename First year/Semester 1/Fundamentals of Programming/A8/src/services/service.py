from datetime import date
from src.domain.movie import Movie
from src.domain.errors import ServiceError
from src.domain.client import Client
from src.domain.rental import Rental
from datetime import timedelta


class MovieService:
    def __init__(self, movie_repo, validation_movie):
        self._movie_repo = movie_repo
        self._validation_movie = validation_movie

    def add_movie_service(self, movie_id, title, description, genre):
        if self.find_movie_by_id(movie_id):
            raise ServiceError("The movie id already exists")
        movie = Movie(movie_id, title, description, genre)
        self._validation_movie.validate(movie)
        self._movie_repo.add_movie_repo(movie)

    def remove_movie_service(self, movie_id):
        if not self.find_movie_by_id(movie_id):
            raise ServiceError("The movie id does not exist")
        movie = self.find_movie_by_id(movie_id)
        self._movie_repo.remove_movie_repo(movie)

    def get_all_movies_service(self):
        return self._movie_repo.get_all_movies_repo()

    def find_movie_by_id(self, movie_id_to_search_for):
        movies = self._movie_repo.get_all_movies_repo()
        for movie in movies:
            if movie.movie_id == movie_id_to_search_for:
                return movie
        return False

    def update_movie_service(self, movie_id, title, description, genre):
        updated_movie = Movie(movie_id, title, description, genre)
        self._validation_movie.validate(updated_movie)
        self._movie_repo.update_movie_repo(updated_movie, movie_id)

    def search_movie_service(self, search_input):
        search_results = []
        movies = self._movie_repo.get_all_movies_repo()
        search_input = search_input.lower()
        for movie in movies:
            if search_input in movie.movie_id:
                search_results.append(movie)
            elif search_input in movie.title.lower():
                search_results.append(movie)
            elif search_input in movie.description.lower():
                search_results.append(movie)
            elif search_input in movie.genre.lower():
                search_results.append(movie)
        return search_results


class ClientService:
    def __init__(self, client_repo, validation_client):
        self._client_repo = client_repo
        self._validation_client = validation_client

    def add_client_service(self, client_id, client_name):
        if self.find_client_by_id(client_id):
            raise ServiceError('Client id already exists')
        client = Client(client_id, client_name)
        self._validation_client.validate(client)
        self._client_repo.add_client_repo(client)

    def find_client_by_id(self, client_id):
        clients = self._client_repo.get_all_clients_repo()
        for client in clients:
            if client.client_id == client_id:
                return client
        return False

    def get_all_clients_service(self):
        return self._client_repo.get_all_clients_repo()

    def remove_client_service(self, client_id):
        if not self.find_client_by_id(client_id):
            raise ServiceError('The client id does not exist')
        client = self.find_client_by_id(client_id)
        self._client_repo.remove_client_repo(client)

    def update_client_service(self, client_id, new_name):
        client = Client(client_id, new_name)
        self._validation_client.validate(client)
        self._client_repo.update_client_repo(client, client_id)

    def search_client_service(self, search_input):
        search_results = []
        clients = self._client_repo.get_all_clients_repo()
        search_input = search_input.lower()
        for client in clients:
            if search_input in client.client_id:
                search_results.append(client)
            elif search_input in client.name.lower():
                search_results.append(client)
        return search_results


class RentalService:
    def __init__(self, rental_repo, validation_rental, movie_repo, client_repo, movie_service, client_service):
        self._rental_repo = rental_repo
        self._validation_rental = validation_rental
        self._movie_repo = movie_repo
        self._client_repo = client_repo
        self._movie_service = movie_service
        self._client_service = client_service

    def rent_a_movie_service(self,rental_id, client_id, movie_id, rental_date):
        self.check_rental_possibility(client_id, movie_id, rental_id)
        due_date = rental_date + timedelta(days=10)
        rental = Rental(rental_id, movie_id, client_id, rental_date, due_date)
        self._validation_rental.validate(rental)
        self._rental_repo.rent_a_movie_repo(rental)

    def check_rental_possibility(self, client_id, movie_id, rental_id):
        rentals = self._rental_repo.get_all_rentals_repo()
        for rental in rentals:
            if rental.client_id == client_id and rental.due_date < date.today():
                raise ServiceError('You can not borrow movies now. Please return the movies that passed their due dates')
        for rental in rentals:
            if rental.movie_id == movie_id and not rental.returned_date:
                raise ServiceError('This movie is not available right now. Try again later')
        for rental in rentals:
            if rental.rental_id == rental_id:
                raise ServiceError('Invalid rental id')

    def get_all_rentals_service(self):
        return self._rental_repo.get_all_rentals_repo()

    def search_rental_by_rental_id(self, rental_id):
        rentals = self._rental_repo.get_all_rentals_repo()
        for rental in rentals:
            if rental.rental_id == rental_id:
                return rental
        return False

    def delete_a_return_service(self, rental_id):
        self._rental_repo.delete_a_return_repo(rental_id)

    def return_a_movie_service(self, rental_id, returned_date):
        self.check_return_possibility(rental_id, returned_date)
        self._rental_repo.return_a_movie_repo(rental_id, returned_date)

    def check_return_possibility(self, rental_id, returned_date):
        rentals = self._rental_repo.get_all_rentals_repo()
        rental_exists = False
        for rental in rentals:
            if rental.rental_id == rental_id:
                if rental.returned_date:
                    raise ServiceError('The movie has already been returned')
                if rental.rental_date > returned_date:
                    raise ServiceError('Invalid return date')
                rental_exists = True
        if not rental_exists:
            raise ServiceError('The rental does not exist')

    def delete_rental_service(self, rental_id):
        rentals = self.get_all_rentals_service()
        for rental in rentals:
            if rental.rental_id == rental_id:
                self._rental_repo.delete_rental_repo(rental)
                break


class Statistics:
    def __init__(self, rental_repo, movie_service, client_service, rental_service):
        self._rental_repo = rental_repo
        self._movie_service = movie_service
        self._client_service = client_service
        self._rental_service = rental_service

    def most_rented_movies_service(self):
        rentals = self._rental_repo.get_all_rentals_repo()
        most_rented_movies_dict = {}
        for rental in rentals:
            movie_id = rental.movie_id
            if self._movie_service.find_movie_by_id(movie_id):
                if rental.returned_date:
                    delta = rental.returned_date - rental.rental_date
                else:
                    delta = date.today() - rental.rental_date
                current_days = 0
                if movie_id in most_rented_movies_dict.keys():
                    current_days = most_rented_movies_dict[movie_id]
                most_rented_movies_dict[movie_id] = current_days + delta.days
        sorted_most_rented_movies_tuple = sorted(most_rented_movies_dict.items(), key = lambda number: number[1])
        index = len(sorted_most_rented_movies_tuple) - 1
        sorted_most_rented_movies_list = []
        while index >= 0:
            movie = self._movie_service.find_movie_by_id(sorted_most_rented_movies_tuple[index][0])
            sorted_most_rented_movies_list.append(movie)
            index -= 1
        return sorted_most_rented_movies_list

    def most_active_clients_service(self):
        rentals = self._rental_repo.get_all_rentals_repo()
        most_active_clients_dict = {}
        for rental in rentals:
            movie_id = rental.movie_id
            client_id = rental.client_id
            if self._movie_service.find_movie_by_id(movie_id):
                if rental.returned_date:
                    delta = rental.returned_date - rental.rental_date
                else:
                    delta = date.today() - rental.rental_date
                current_days = 0
                if client_id in most_active_clients_dict.keys():
                    current_days = most_active_clients_dict[client_id]
                most_active_clients_dict[client_id] = delta.days + current_days
        sorted_most_active_clients_tuple = sorted(most_active_clients_dict.items(), key = lambda number: number[1])
        index = len(sorted_most_active_clients_tuple) - 1
        sorted_most_active_clients_list = []
        while index >= 0:
            client = self._client_service.find_client_by_id(sorted_most_active_clients_tuple[index][0])
            sorted_most_active_clients_list.append(client)
            index -= 1
        return sorted_most_active_clients_list

    def late_rentals_service(self):
        rentals = self._rental_repo.get_all_rentals_repo()
        late_rentals_dict = {}
        for rental in rentals:
            if not rental.returned_date and date.today() > rental.due_date:
                delta = date.today() - rental.due_date
                late_rentals_dict[rental.rental_id] = delta.days
        sorted_late_rentals_tuple = sorted(late_rentals_dict.items(), key=lambda number: number[1])
        index = len(sorted_late_rentals_tuple) - 1
        sorted_late_rentals_list = []
        while index >= 0:
            rental = self._rental_service.search_rental_by_rental_id(sorted_late_rentals_tuple[index][0])
            sorted_late_rentals_list.append(rental)
            index -= 1
        return sorted_late_rentals_list
