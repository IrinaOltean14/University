from src.domain.errors import ServiceError, RepoError


class MoveService:
    def __init__(self, repo):
        self._repo = repo

    def validate_place_planes_service(self, row, column, direction):
        if direction == 'up' and (row > 6 or column < 2 or column > 7):
            return False
        if direction == 'down' and (row < 3 or column < 2 or column > 7):
            return False
        if direction == 'right' and (column < 3 or row < 2 or row > 7):
            return False
        if direction == 'left' and (column > 6 or row < 2 or row > 7):
            return False
        return True

    def place_planes_service(self, who_moves, plane_head, plane_direction):
        if len(plane_head) != 2:
            raise ServiceError('Enter a valid location')
        if plane_head[0] < 'A' or plane_head[0] > 'J' or plane_head[1] > '9' or plane_head[1] < '0':
            raise ServiceError('The location of the plane head is not valid')
        if plane_direction not in ['up', 'down', 'right','left']:
            raise ServiceError('The direction of the plane is not valid')
        column = int(plane_head[1])
        row = ord(plane_head[0]) - 65
        if not self.validate_place_planes_service(row, column, plane_direction):
            raise ServiceError('The plane does not fit on the table (pick another location)')
        if who_moves == 'player':
            try:
                self._repo.place_planes_repo('player',row, column, plane_direction)
            except RepoError as error:
                raise ServiceError(str(error))
        elif who_moves == 'computer':
            try:
                self._repo.place_planes_repo('computer',row, column, plane_direction)
            except RepoError as error:
                raise ServiceError(str(error))

    def move_service(self, who_plays, move):
        if move[0] < 'A' or move[0] > 'J' or move[1] > '9' or move[1] < '0':
            raise ServiceError('The move is not valid')
        column = int(move[1])
        row = ord(move[0]) - 65
        return self._repo.move_repo(who_plays, row, column)

    def get_player_board_service(self):
        return self._repo.get_player_board()

    def get_computer_board_service(self):
        return self._repo.get_computer_board()

    def check_winner_status_service(self,who_moves):
        return self._repo.check_winner_status_repo(who_moves)

