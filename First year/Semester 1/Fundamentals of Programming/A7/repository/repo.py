
class MovieRepo:
    def __init__(self):
        self._movies = []

    def add_movie_repo(self, movie_to_be_added):
        self._movies.append(movie_to_be_added)

    def get_all_movies_repo(self):
        return self._movies

    def remove_movie_repo(self, movie_to_delete):
        self._movies.remove(movie_to_delete)

    def update_movie_repo(self, updated_movie, movie_id):
        for index in range(0, len(self._movies)):
            if self._movies[index].movie_id == movie_id:
                self._movies[index] = updated_movie


class ClientRepo:
    def __init__(self):
        self._clients = []

    def add_client_repo(self, client):
        self._clients.append(client)

    def get_all_clients_repo(self):
        return self._clients

    def remove_client_repo(self, client):
        self._clients.remove(client)

    def update_client_repo(self, updated_client, client_id):
        for index in range(0, len(self._clients)):
            if self._clients[index].client_id == client_id:
                self._clients[index] = updated_client


class RentalRepo:
    def __init__(self):
        self._rentals = []

    def rent_a_movie_repo(self, rental):
        self._rentals.append(rental)

    def get_all_rentals_repo(self):
        return self._rentals

    def return_a_movie_repo(self, rental_id, returned_date):
        for rental in self._rentals:
            if rental.rental_id == rental_id:
                rental.returned_date = returned_date

    def delete_rental_repo(self, rental):
        self._rentals.remove(rental)

    def delete_a_return_repo(self, rental_id):
        for rental in self._rentals:
            if rental.rental_id == rental_id:
                rental.returned_date = None

