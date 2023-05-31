# Example explains monkeypatch usage
# but for reliable mock API purposes
# should use lib like responses
import requests


def test_monkeypatch_request(monkeypatch):

    # Mock the requests.get() method to return custom responses
    def mock_get(url):
        class MockResponse:
            @staticmethod
            def json():
                return {'message': f'Mocked response for {url}'}

            @property
            def text(self):
                return f'Mocked response text for {url}'

        return MockResponse()

    # Monkeypatch the requests.get method to use our mock_get function
    monkeypatch.setattr(requests, 'get', mock_get)

    response1 = requests.get('https://api.example.com/data1')
    response2 = requests.get('https://api.example.com/data2')
    # Assert that the method returns the mocked responses
    assert response1.text == 'Mocked response text for https://api.example.com/data1'
    assert response2.text == 'Mocked response text for https://api.example.com/data2'