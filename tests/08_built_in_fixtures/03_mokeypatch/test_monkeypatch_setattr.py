import pytest
import requests


@pytest.fixture()
def mock_api(monkeypatch):
    def mock_post(url, json):
        class MockResponse:
            def __init__(self, json_data):
                self.json_data = json_data

            def json(self):
                return self.json_data

        if url == 'https://example.com/endpoint1':
            return MockResponse({'message': 'Response from endpoint 1 (POST)'})
        elif url == 'https://example.com/endpoint2':
            return MockResponse({'message': 'Response from endpoint 2 (POST)'})
        else:
            return MockResponse({'message': 'Unknown endpoint (POST)'})

    # Mock the requests.get() method to return different responses based on the URL
    def mock_get(url):
        class MockResponse:
            def __init__(self, json_data):
                self.json_data = json_data

            def json(self):
                return self.json_data

        if url == 'https://example.com/endpoint3':
            return MockResponse({'message': 'Response from endpoint 3 (GET)'})
        elif url == 'https://example.com/endpoint4':
            return MockResponse({'message': 'Response from endpoint 4 (GET)'})
        else:
            return MockResponse({'message': 'Unknown endpoint (GET)'})

    monkeypatch.setattr(requests, 'post', mock_post)
    monkeypatch.setattr(requests, 'get', mock_get)


def test_mock_api(mock_api):
    data1 = {'key': 'value1'}
    url1 = 'https://example.com/endpoint1'
    result1 = requests.post(url1, json=data1).json()
    assert result1 == {'message': 'Response from endpoint 1 (POST)'}

    data2 = {'key': 'value2'}
    url2 = 'https://example.com/endpoint2'
    result2 = requests.post(url2, json=data2).json()
    assert result2 == {'message': 'Response from endpoint 2 (POST)'}

    url3 = 'https://example.com/endpoint3'
    result3 = requests.get(url3).json()
    assert result3 == {'message': 'Response from endpoint 3 (GET)'}

    url4 = 'https://example.com/endpoint4'
    result4 = requests.get(url4).json()
    assert result4 == {'message': 'Response from endpoint 4 (GET)'}
