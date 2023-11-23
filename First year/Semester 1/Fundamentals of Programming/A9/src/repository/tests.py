from src.repository.board_repo import RepoBoards
import unittest
from src.service.move_service import MoveService
from src.domain.errors import ServiceError


class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self._board = RepoBoards()
        self._service = MoveService(self._board)

    def test_board(self):
        # test place planes
        self._board.place_planes_repo('player', 2, 0, 'left')
        player_board = self._board.get_player_board()
        self.assertEqual(player_board[2][0], '$')
        self.assertEqual(player_board[2][1], 'X')
        # test hit part of a plane
        self._board.move_repo('computer', 2, 1)
        self.assertEqual(player_board[2][1], '0')
        # test hit the air
        self._board.move_repo('computer', 3, 0)
        self.assertEqual(player_board[3][0], ' ')
        # test hit a cabin
        self._board.move_repo('computer', 2, 0)
        self.assertEqual(player_board[2][0], '0')
        # test delete a plane
        self._board.place_planes_repo('player', 9, 2, 'down')
        player_planes = self._board.get_planes('player')
        self.assertEqual(player_planes, [(9,2,'down')])
        self._board.delete_plane('computer',9,2)
        player_planes = self._board.get_planes('player')
        self.assertEqual(player_planes, [])

    def test_game(self):
        # test place planes
        with self.assertRaises(ServiceError) as error:
            self._service.place_planes_service('player','A79', 'up')
        self.assertEqual(str(error.exception), 'Enter a valid location')
        with self.assertRaises(ServiceError) as error:
            self._service.place_planes_service('player','AA', 'up')
        self.assertEqual(str(error.exception), 'The location of the plane head is not valid')
        with self.assertRaises(ServiceError) as error:
            self._service.place_planes_service('player','A7', 'uup')
        self.assertEqual(str(error.exception), 'The direction of the plane is not valid')



