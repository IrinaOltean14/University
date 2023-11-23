from src.domain import As
class MemoryRepo:
    def __init__(self):
        self._assign_list = []

    def display_assign(self):
        return self._assign_list

    def add_assign(self, assign):
        self._assign_list.append(assign)


class TextFileRepo(MemoryRepo):
    def __init__(self, file_path=str('assignments.txt')):
        super().__init__()
        self._file_path = file_path
        #self._write_data_to_file()

    def _write_data_to_file(self):
        with open(self._file_path, "wt") as file:
            for assign in super().display_assign():
                file.write(str(assign)+'\n')
        file.close()

    def _read_data_from_file(self):
        self._assign_list = []
        with open(self._file_path, "rt") as file:
            lines = file.readlines()
            for line in lines:
                if line != "":
                    parts = line.split(',')
                    id = parts[0].strip()
                    name = parts[1].strip()
                    solution = parts[2].strip()
                    assign =As(id, name, solution)
                    super().add_assign(assign)
        file.close()

    def display_assign(self):
        self._read_data_from_file()
        assign = super().display_assign()
        self._write_data_to_file()
        return assign

    def add_assign(self, assign):
        self._read_data_from_file()
        super().add_assign(assign)
        self._write_data_to_file()