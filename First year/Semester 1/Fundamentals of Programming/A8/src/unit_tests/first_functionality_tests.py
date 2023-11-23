import unittest
from src.domain.validators import MovieValidator, ClientValidator
from src.services.service import MovieService, ClientService
from src.repository.repo import MovieRepo, ClientRepo
from src.domain.errors import ServiceError, StoreExceptions


class MovieServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._movie_repo = MovieRepo()
        self._movie_service = MovieService(self._movie_repo, MovieValidator())

    def tearDown(self) -> None:
        pass

    def test_add_movie(self):
        self._movie_service.add_movie_service('1', 'Batman', 'DC movie', 'Action')
        self.assertEqual(len(self._movie_service.get_all_movies_service()), 1)

    def test_add_movie2(self):
        with self.assertRaises(StoreExceptions) as error:
            self._movie_service.add_movie_service('1', 'Batman', 'DC movie', 'ceva')
        self.assertEqual(str(error.exception), 'Invalid movie genre')

    def test_add_movie3(self):
        self._movie_service.add_movie_service('1', 'Batman', 'DC movie', 'Action')
        with self.assertRaises(ServiceError) as error:
            self._movie_service.add_movie_service('1', 'Batman', 'DC movie', 'Action')
        self.assertEqual(str(error.exception), 'The movie id already exists')

    def test_update_movie(self):
        self._movie_service.add_movie_service('1', 'Batman', 'DC movie', 'Action')
        self._movie_service.update_movie_service('1', 'Batman', 'DC movie', 'Sci-Fi')
        movies = self._movie_service.get_all_movies_service()
        movie = movies[0]
        self.assertEqual(movie.genre, 'Sci-Fi')

    def test_remove_movie(self):
        self._movie_service.add_movie_service('1', 'Batman', 'DC movie', 'Action')
        self._movie_service.remove_movie_service('1')
        self.assertEqual(len(self._movie_service.get_all_movies_service()), 0)

    def test_find_movie_by_id(self):
        self._movie_service.add_movie_service('1', 'Batman', 'DC movie', 'Action')
        movies = self._movie_service.get_all_movies_service()
        movie = movies[0]
        self.assertEqual(movie, self._movie_service.find_movie_by_id('1'))


class ClientServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._client_repo = ClientRepo()
        self._client_service = ClientService(self._client_repo, ClientValidator())

    def tearDown(self) -> None:
        pass

    def test_add_client(self):
        self._client_service.add_client_service('1', 'Maria Alexutan')
        self.assertEqual(len(self._client_service.get_all_clients_service()), 1)

    def test_remove_client(self):
        self._client_service.add_client_service('1', 'Maria Alexutan')
        self._client_service.remove_client_service('1')
        self.assertEqual(len(self._client_service.get_all_clients_service()), 0)

    def test_update_client(self):
        self._client_service.add_client_service('1', 'Maria Alexutan')
        self._client_service.update_client_service('1', 'Marius Alexutan')
        clients = self._client_service.get_all_clients_service()
        client = clients[0]
        self.assertEqual(client.name, 'Marius Alexutan')

    def test_find_client_by_id(self):
        self._client_service.add_client_service('1', 'Maria Alexutan')
        clients = self._client_service.get_all_clients_service()
        client = clients[0]
        self.assertEqual(client, self._client_service.find_client_by_id('1'))