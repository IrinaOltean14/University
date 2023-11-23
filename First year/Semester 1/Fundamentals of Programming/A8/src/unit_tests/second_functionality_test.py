import unittest
from datetime import date
from src.repository.repo import RentalRepo, MovieRepo, ClientRepo
from src.services.service import MovieService, ClientService, RentalService
from src.domain.validators import MovieValidator, ClientValidator, RentalValidator
from src.domain.errors import ServiceError


class RentalServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._rental_repo = RentalRepo()
        self._movie_service = MovieService(MovieRepo(), MovieValidator())
        self._client_service = ClientService(ClientRepo(), ClientValidator())
        self._client_service = ClientService
        self._rental_service = RentalService(self._rental_repo, RentalValidator, MovieRepo(), ClientRepo(), self._movie_service, self._client_service)

    def tearDown(self) -> None:
        pass

    def test_rent_a_movie_service1(self):
        rental_date = date(2022, 12, 18)
        self._rental_service.rent_a_movie_service('1', '1', rental_date)
        self.assertEqual(len(self._rental_service.get_all_rentals_service()), 1)

    def test_rent_a_movie_service2(self): #try to rent a rented movie
        rental_date = date(2022, 12, 16)
        self._rental_service.rent_a_movie_service('1', '1', rental_date)
        rental_date = date(2022, 12, 18)
        with self.assertRaises(ServiceError) as error:
            self._rental_service.rent_a_movie_service('2', '1', rental_date)
        self.assertEqual(str(error.exception), 'This movie is not available right now. Try again later')

    def test_rent_a_movie_service3(self): #client that can not rent movies currently tries to rent
        rental_date = date(2022, 12, 6)
        self._rental_service.rent_a_movie_service('1', '1', rental_date)
        rental_date = date(2022, 12, 18)
        with self.assertRaises(ServiceError) as error:
            self._rental_service.rent_a_movie_service('1', '2', rental_date)
        self.assertEqual(str(error.exception), 'You can not borrow movies now. Please return the movies that passed their due dates')

    def test_return_a_movie_service1(self):
        rental_date = date(2022, 12, 6)
        self._rental_service.rent_a_movie_service('1', '1', rental_date)
        returned_date = date(2022, 12, 18)
        self._rental_service.return_a_movie_service('1', returned_date)
        rentals = self._rental_service.get_all_rentals_service()
        rental = rentals[0]
        self.assertEqual(rental.returned_date, returned_date)

    def test_return_a_movie_service2(self):
        # return a rental that does not exist
        returned_date = (2022, 12, 16)
        with self.assertRaises(ServiceError) as error:
            self._rental_service.return_a_movie_service('1', returned_date)
        self.assertEqual(str(error.exception), 'The rental does not exist')

    def test_return_a_movie_service3(self):
        # returned_date < rental_date
        rental_date = date(2022, 12, 6)
        self._rental_service.rent_a_movie_service('1', '1', rental_date)
        returned_date = date(2022, 12, 4)
        with self.assertRaises(ServiceError) as error:
            self._rental_service.return_a_movie_service('1', returned_date)
        self.assertEqual(str(error.exception), 'Invalid return date')

    def test_return_a_movie3(self):
        # return a rental that has been returned
        rental_date = date(2022, 12, 6)
        self._rental_service.rent_a_movie_service('1', '1', rental_date)
        returned_date = date(2022, 12, 18)
        self._rental_service.return_a_movie_service('1', returned_date)
        returned_date = date(2022, 12, 19)
        with self.assertRaises(ServiceError) as error:
            self._rental_service.return_a_movie_service('1', returned_date)
        self.assertEqual(str(error.exception), 'The movie has already been returned')



