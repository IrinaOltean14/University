from src.domain.errors import StoreExceptions, ServiceError, UndoRedoException
from datetime import date


class UI:
    def __init__(self, movie_service, client_service, rental_service, statistics_service, undo_redo):
        self._movie_service = movie_service
        self._client_service = client_service
        self._rental_service = rental_service
        self._statistics_service = statistics_service
        self._undo_redo = undo_redo

    def print_menu(self):
        while True:
            print("Pick your option:")
            print("1.Manage clients and movies")
            print("2.Rent or return a movie")
            print("3.Search for clients or movies (using any of their fields)")
            print("4.Create statistics")
            print("5. Undo")
            print("6. Redo")
            print("7. End program")
            option = input("Enter your option: ")
            manage_clients_and_movies = '1'
            if option == manage_clients_and_movies:
                print("Do you want to work with movies or with clients?")
                print("1. Movies")
                print("2. Clients")
                user_pick = input("Enter your option: ")
                if user_pick == '1':
                    print("What do you want to do?")
                    print('1. Add a movie')
                    print('2. Remove a movie')
                    print('3. Update a movie')
                    print('4. Display movies')
                    user_pick_service = input('Enter your option: ')
                    if user_pick_service == '1':
                        self.add_movie_ui()
                    elif user_pick_service == '2':
                        self.remove_movie_ui()
                    elif user_pick_service == '3':
                        self.update_movie_ui()
                    elif user_pick_service == '4':
                        self.display_movies()
                    else:
                        print('Invalid command')
                elif user_pick == '2':
                    print("What do you want to do?")
                    print('1. Add a client')
                    print('2. Remove a client')
                    print('3. Update a client')
                    print('4. Display clients')
                    user_pick_service = input('Enter your option: ')
                    if user_pick_service == '1':
                        self.add_client_ui()
                    if user_pick_service == '2':
                        self.remove_client_ui()
                    if user_pick_service == '3':
                        self.update_client_ui()
                    elif user_pick_service == '4':
                        self.display_clients()
                else:
                    print('Invalid command')
            elif option == '2':
                print('What do you want to do?')
                print('1. Rent a movie')
                print('2. Return a movie')
                print('3. Display rentals')
                user_pick_service = input('Enter your option: ')
                if user_pick_service == '1':
                    self.rent_a_movie_ui()
                elif user_pick_service == '2':
                    self.return_a_movie_ui()
                elif user_pick_service == '3':
                    self.display_rentals_ui()
                else:
                    print('Invalid command')
            elif option == '3':
                print('What do you want to search?')
                print('1. Movies')
                print('2. Clients')
                user_pick_service = input('Enter your option: ')
                if user_pick_service == '1':
                    self.search_movie_ui()
                elif user_pick_service == '2':
                    self.search_client_ui()
                else:
                    print('Invalid command')
            elif option == '4':
                print('Choose statistic')
                print('1. Most rented movies')
                print('2. Most active clients')
                print('3. Late rentals')
                user_pick = input('Enter your option: ')
                if user_pick == '1':
                    self.most_rented_movies_ui()
                elif user_pick == '2':
                    self.most_active_clients_ui()
                elif user_pick == '3':
                    self.late_rentals_ui()
            elif option == '5':
                try:
                    self._undo_redo.undo_operation()
                    print('Undo operation successful')
                except UndoRedoException as error:
                    print('ERROR: ' + str(error))
            elif option == '6':
                try:
                    self._undo_redo.redo_operation()
                    print('Redo operation successful')
                except UndoRedoException as error:
                    print('ERROR: ' + str(error))
            elif option == '7':
                break
            else:
                print('Invalid command')

    def generate_movies(self):
        self._movie_service.add_movie_service('1', 'Iron Man', 'Marvel movie', 'Action')
        self._movie_service.add_movie_service('2', 'Batman', 'DC movie', 'Action')
        self._movie_service.add_movie_service('3', 'Thor', 'Marvel movie', 'Action')
        self._movie_service.add_movie_service('4', 'Black Panther', 'Marvel movie', 'Action')
        self._movie_service.add_movie_service('5', 'Black Widow', 'Marvel movie', 'Action')
        self._movie_service.add_movie_service('6', 'Spiderman', 'Marvel movie', 'Action')
        self._movie_service.add_movie_service('7', 'Captain America', 'Marvel movie', 'Action')
        self._movie_service.add_movie_service('8', 'Avatar 2', 'new movie', 'Sci-Fi')
        self._movie_service.add_movie_service('9', 'Hulk', 'Marvel movie', 'Action')
        self._movie_service.add_movie_service('10', 'Iron Man 2', 'Marvel movie', 'Action')

    def generate_clients(self):
        self._client_service.add_client_service('1', 'Andre Moldovan')
        self._client_service.add_client_service('2', 'Marius Ciupe')
        self._client_service.add_client_service('3', 'Andrada Puscas')
        self._client_service.add_client_service('4', 'Mihai Ardelean')
        self._client_service.add_client_service('5', 'Paul Noje')
        self._client_service.add_client_service('6', 'Maria Pop')
        self._client_service.add_client_service('7', 'Dan Pripon')
        self._client_service.add_client_service('8', 'Miruna Petre')
        self._client_service.add_client_service('9', 'Anda Moga')
        self._client_service.add_client_service('10', 'Ana Popa')

    def add_movie_ui(self):
        movie_id = input("Enter the movie id: ")
        title = input("Enter the movie title: ")
        description = input("Enter the movie description: ")
        genre = input("Enter the movie genre: ")
        try:
            self._movie_service.add_movie_service(movie_id, title, description, genre)
            print("Movie added successfully")
            self._undo_redo.register_operation_undo('add movie', (movie_id, title, description, genre))
        except StoreExceptions as errors:
            print("ERROR: " + str(errors))
        except ServiceError as errors:
            print("ERROR: " + str(errors))

    def remove_movie_ui(self):
        movie_id = input("Enter the movie id (that you want to delete): ")
        try:
            movie = self._movie_service.find_movie_by_id(movie_id)
            self._movie_service.remove_movie_service(movie_id)
            print("Movie deleted successfully")
            self._undo_redo.register_operation_undo('remove movie', (movie_id, movie.title, movie.description, movie.genre))
        except ServiceError as error:
            print("ERROR: " + str(error))

    def update_movie_ui(self):
        movie_id = input("Enter the movie id that you want to update: ")
        if not self._movie_service.find_movie_by_id(movie_id):
            print("The movie id does not exist")
        else:
            new_title = input("Enter the updated title: ")
            new_description = input("Enter the updated description: ")
            new_genre = input("Enter the updated genre: ")
            try:
                movie = self._movie_service.find_movie_by_id(movie_id)
                self._movie_service.update_movie_service(movie_id, new_title, new_description, new_genre)
                self._undo_redo.register_operation_undo('update movie', (movie_id, movie.title, movie.description, movie.genre, new_title, new_description, new_genre))
                print("Movie updated successfully")
            except StoreExceptions as error:
                print("ERROR: " + str(error))

    def display_movies(self):
        movies = self._movie_service.get_all_movies_service()
        for movie in movies:
            print(movie)

    def add_client_ui(self):
        client_id = input("Enter client id: ")
        client_name = input("Enter client name: ")
        try:
            self._client_service.add_client_service(client_id, client_name)
            self._undo_redo.register_operation_undo('add client', (client_id, client_name))
            print("Client added successfully")
        except ServiceError as error:
            print("ERROR: " + str(error))

    def display_clients(self):
        clients = self._client_service.get_all_clients_service()
        for client in clients:
            print(client)

    def remove_client_ui(self):
        client_id = input('Enter the client id (that you want to remove): ')
        try:
            client = self._client_service.find_client_by_id(client_id)
            self._client_service.remove_client_service(client_id)
            self._undo_redo.register_operation_undo('remove client', (client_id, client.name))
            print("Client removed successfully")
        except ServiceError as error:
            print('ERROR: ' + str(error))

    def update_client_ui(self):
        client_id = input('Enter the client id (that you want to update): ')
        if not self._client_service.find_client_by_id(client_id):
            print('The client id does not exist')
        else:
            new_name = input('Enter the updated name: ')
            try:
                client = self._client_service.find_client_by_id(client_id)
                self._client_service.update_client_service(client_id, new_name)
                print('Client updated successfully')
                self._undo_redo.register_operation_undo('update client', (client_id, client.name, new_name))
            except StoreExceptions as error:
                print('ERROR: ' + str(error))

    def generate_rentals(self):
        self._rental_service.rent_a_movie_service('1', '1', '6', date(2022, 12, 16))
        self._rental_service.rent_a_movie_service('2','1', '2', date(2022, 12, 15))
        self._rental_service.rent_a_movie_service('3', '1', '4', date(2022, 12, 7))
        self._rental_service.rent_a_movie_service('4', '2', '1', date(2022, 12, 15))
        self._rental_service.rent_a_movie_service('5', '4', '3', date(2022, 12, 17))
        self._rental_service.rent_a_movie_service('6', '7', '5', date(2022, 12, 14))
        self._rental_service.rent_a_movie_service('7', '3', '10', date(2022, 12, 5))

    def rent_a_movie_ui(self):
        rental_id = input('Please give the rental id: ')
        client_id = input('Please give the client id: ')
        movie_id = input('Please give the movie id: ')
        ok = True
        if not self._movie_service.find_movie_by_id(movie_id):
            ok = False
            print('The movie id does not exist')
        if not self._client_service.find_client_by_id(client_id):
            ok = False
            print('The client id does not exist')
        if ok:
            print('Do you want to specify the rental date? (if not, the rental date is today)')
            print('1. Yes')
            print('2. No')
            option = input('Enter your option: ')

            if option == '1':
                ok = True
                try:
                    day = int(input('Enter the day: '))
                except ValueError:
                    print('Not a valid day')
                    ok = False
                try:
                    month = int(input('Enter a month: '))
                except ValueError:
                    print('Not a valid month')
                    ok = False
                try:
                    year = int(input('Enter a year: '))
                except ValueError:
                    print('Not a valid year')
                    ok = False
                if ok:
                    if day < 0 or day > 29 or month < 0 or month > 12 or year > 2022 or year < 2000:
                        ok = False
                        print('Invalid date')
                if ok:
                    rental_date = date(year, month, day)
                    try:
                        self._rental_service.rent_a_movie_service(rental_id, client_id, movie_id, rental_date)
                        self._undo_redo.register_operation_undo('rent a movie', (rental_id, client_id, movie_id, rental_date))
                        print('Rental added successfully')
                    except ServiceError as error:
                        print('ERROR: ' + str(error))
            elif option == '2':
                rental_date = date.today()
                try:
                    self._rental_service.rent_a_movie_service(rental_id, client_id, movie_id, rental_date)
                    self._undo_redo.register_operation_undo('rent a movie', (rental_id, client_id, movie_id, rental_date))
                    print('Rental added successfully')
                except ServiceError as error:
                    print('ERROR: ' + str(error))
            else:
                print('Invalid command')

    def display_rentals_ui(self):
        rentals = self._rental_service.get_all_rentals_service()
        for rental in rentals:
            print(rental)

    def return_a_movie_ui(self):
        rental_id = input('Please enter the rental id: ')
        ok = self._rental_service.search_rental_by_rental_id(rental_id)
        if not ok:
            print('The rental id does not exist')
        else:
            print('Do you want to specify the return date? (if not, the return date is today)')
            print('1. Yes')
            print('2. No')
            option = input('Enter your option: ')

            if option == '1':
                ok = True
                try:
                    day = int(input('Enter the day: '))
                except ValueError:
                    print('Not a valid day')
                    ok = False
                try:
                    month = int(input('Enter a month: '))
                except ValueError:
                    print('Not a valid month')
                    ok = False
                try:
                    year = int(input('Enter a year: '))
                except ValueError:
                    print('Not a valid year')
                    ok = False
                if ok:
                    if day < 0 or day > 29 or month < 0 or month > 12 or year > 2022 or year < 2000:
                        ok = False
                        print('Invalid date')
                if ok:
                    return_date = date(year, month, day)
                    try:
                        self._rental_service.return_a_movie_service(rental_id, return_date)
                        print('Movie returned successfully')
                        self._undo_redo.register_operation_undo('return a movie', (rental_id, return_date))
                    except ServiceError as error:
                        print('ERROR: ' + str(error))
            elif option == '2':
                return_date = date.today()
                try:
                    self._rental_service.return_a_movie_service(rental_id, return_date)
                    print('Movie returned successfully')
                    self._undo_redo.register_operation_undo('return a movie', (rental_id, return_date))
                except ServiceError as error:
                    print('ERROR: ' + str(error))
            else:
                print('Invalid command')

    def search_movie_ui(self):
        search_input = input('Enter what you search for: ')
        search_results = self._movie_service.search_movie_service(search_input)
        for movie in search_results:
            print(movie)
        if len(search_results) == 0:
            print('No results')

    def search_client_ui(self):
        search_input = input('Enter what you search for: ')
        search_results = self._client_service.search_client_service(search_input)
        for client in search_results:
            print(client)
        if len(search_results) == 0:
            print('No results')

    def most_rented_movies_ui(self):
        most_rented_movies_list = self._statistics_service.most_rented_movies_service()
        for movie in most_rented_movies_list:
            print(movie)

    def most_active_clients_ui(self):
        most_active_clients_list = self._statistics_service.most_active_clients_service()
        for client in most_active_clients_list:
            print(client)

    def late_rentals_ui(self):
        late_rentals_list = self._statistics_service.late_rentals_service()
        for rental in late_rentals_list:
            print(rental)