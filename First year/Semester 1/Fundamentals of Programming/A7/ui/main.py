from src.domain.validators import MovieValidator
from src.domain.validators import ClientValidator, RentalValidator
from src.repository.repo import MovieRepo, ClientRepo, RentalRepo
from src.services.service import MovieService, ClientService, RentalService, Statistics
from src.ui.ui import UI
from src.services.undo import UndoRedo


def main():
    validation_movie = MovieValidator()
    validation_client = ClientValidator()
    validation_rental = RentalValidator()
    movie_repo = MovieRepo()
    movie_service = MovieService(movie_repo, validation_movie)
    client_repo = ClientRepo()
    client_service = ClientService(client_repo, validation_client)
    rental_repo = RentalRepo()
    rental_service = RentalService(rental_repo, validation_rental, movie_repo, client_repo, movie_service, client_service)
    statistics_service = Statistics(rental_repo, movie_service, client_service, rental_service)
    undo_redo = UndoRedo(movie_service, client_service, rental_service)
    ui = UI(movie_service, client_service, rental_service, statistics_service, undo_redo)
    ui.generate_movies()
    ui.generate_clients()
    ui.generate_rentals()
    ui.print_menu()


main()
