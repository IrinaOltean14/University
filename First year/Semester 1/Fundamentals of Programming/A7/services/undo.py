from src.domain.errors import UndoRedoException


class UndoRedo:
    def __init__(self, movie_service, client_service, rental_service):
        self._undo_operation = []
        self._undo_iterator = 0
        self._movie_service = movie_service
        self._client_service = client_service
        self._rental_service = rental_service
        self._redo_operation = []
        self._redo_iterator = 0

    def register_operation_undo(self, type_operation, arguments):
        self._undo_operation.append((type_operation, arguments))
        self._undo_iterator += 1

    def register_operation_redo(self, type_operation, arguments):
        self._redo_operation.append((type_operation, arguments))
        self._redo_iterator += 1

    def redo_is_possible(self):
        if self._redo_iterator <= 0:
            return False
        return True

    def undo_is_possible(self):
        if self._undo_iterator <= 0:
            return False
        return True

    def remove_movie(self, arguments):
        # undo for add movie
        movie_id = arguments[0]
        self._movie_service.remove_movie_service(movie_id)

    def add_movie(self, arguments):
        # undo for remove movie
        movie_id = arguments[0]
        movie_title = arguments[1]
        movie_description = arguments[2]
        movie_genre = arguments[3]
        self._movie_service.add_movie_service(movie_id, movie_title, movie_description, movie_genre)

    def update_movie(self, arguments):
        # undo for update movie
        movie_id = arguments[0]
        movie_title = arguments[1]
        movie_description = arguments[2]
        movie_genre = arguments[3]
        self._movie_service.update_movie_service(movie_id, movie_title, movie_description, movie_genre)

    def update_movie_redo(self, arguments):
        movie_id = arguments[0]
        movie_title = arguments[4]
        movie_description = arguments[5]
        movie_genre = arguments[6]
        self._movie_service.update_movie_service(movie_id, movie_title, movie_description, movie_genre)

    def remove_client(self, arguments):
        # undo for add client
        client_id = arguments[0]
        self._client_service.remove_client_service(client_id)

    def add_client(self, arguments):
        # undo for remove client
        client_id = arguments[0]
        client_name = arguments[1]
        self._client_service.add_client_service(client_id, client_name)

    def update_client(self, arguments):
        # undo for update client
        client_id = arguments[0]
        client_name = arguments[1]
        self._client_service.update_client_service(client_id, client_name)

    def update_client_redo(self, arguments):
        client_id = arguments[0]
        client_name = arguments[2]
        self._client_service.update_client_service(client_id, client_name)

    def delete_a_rental(self, arguments):
        # undo for rent a movie
        rental_id = arguments[0]
        self._rental_service.delete_rental_service(rental_id)

    def delete_a_return(self, arguments):
        # undo for return a movie
        self._rental_service.delete_a_return_service(arguments[0])

    def rent_a_movie(self, arguments):
        self._rental_service.rent_a_movie_service(arguments[0], arguments[1], arguments[2], arguments[3])

    def return_a_movie(self, arguments):
        self._rental_service.return_a_movie_service(arguments[0], arguments[1])

    def undo_operation(self):
        if self.undo_is_possible():
            last_operation = self._undo_operation[len(self._undo_operation)-1]
            type_operation = last_operation[0]
            arguments = last_operation[1]
            self._undo_iterator -= 1
            self._undo_operation.pop()
            self.register_operation_redo(type_operation, arguments)
            if type_operation == 'add movie':
                self.remove_movie(arguments)
            elif type_operation == 'remove movie':
                self.add_movie(arguments)
            elif type_operation == 'update movie':
                self.update_movie(arguments)
            elif type_operation == 'add client':
                self.remove_client(arguments)
            elif type_operation == 'remove client':
                self.add_client(arguments)
            elif type_operation == 'update client':
                self.update_client(arguments)
            elif type_operation == 'rent a movie':
                self.delete_a_rental(arguments)
            elif type_operation == 'return a movie':
                self.delete_a_return(arguments)
        else:
            raise UndoRedoException('You can not undo')

    def redo_operation(self):
        if self.redo_is_possible():
            last_operation = self._redo_operation.pop()
            self._redo_iterator -= 1
            type_operation = last_operation[0]
            arguments = last_operation[1]
            if type_operation == 'add movie':
                self.add_movie(arguments)
            elif type_operation == 'remove movie':
                self.remove_movie(arguments)
            elif type_operation == 'update movie':
                self.update_movie_redo(arguments)
            elif type_operation == 'add client':
                self.add_client(arguments)
            elif type_operation == 'remove client':
                self.remove_client(arguments)
            elif type_operation == 'update client':
                self.update_client_redo(arguments)
            elif type_operation == 'rent a movie':
                self.rent_a_movie(arguments)
            elif type_operation == 'return a movie':
                self.return_a_movie(arguments)

        else:
            raise UndoRedoException('You can not redo')