class Client:
    def __init__(self, client_id, name):
        self._client_id = client_id
        self._name = name

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        self._client_id = client_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return f'{self.client_id} -> {self.name}'


def test_client():
    client = Client('12e', 'Andreea Chis')
    assert client.client_id == '12e'
    assert client.name == 'Andreea Chis'

    client.name = 'Maria Chis'
    assert client.name == 'Maria Chis'

    assert str(client) == '12e -> Maria Chis'


if __name__ == '__main__':
    test_client()