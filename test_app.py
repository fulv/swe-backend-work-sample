import pytest
import app
import json

PUBLIC_KEY = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDBhhgrB72tRuyulrOemCz6xuMa' \
             'R+pWqloDP2pKOISSxINa+bfnw+LIH26mz9E68d3JdXAhrKNSnum7ZCTV2hDmVVo9' \
             '43x6bqTkVL+a5HU1odzfRgpC6EzccrERBIzdKWJtCUU1GFtQYgnDWv4QLKlLIY4n' \
             'JI9iiEG4e9lyC2eONC2j/V81v7ZWI7wLFFFOiv5XdAxhRoNUB1RkyUj73kjKwUW5' \
             '0ZrefDxIrGOZ1mht8tJ9tYWG9+14n4VxCZ2tNe+L8D+36IwXuNvlipuwuX7G4VKb' \
             '/othVeO3ojRGXQpPjy6IciP++Jl8enHu0YkNqcgnqi1mGAzQCaeLtbdvaNkbziX5' \
             '81H0Gthrbivft5KcmBlDBKfdRoWVr5tgm0nYtN08grXyvIKL/GJe1h5JaZWgQpC/' \
             'IUjjxPWRbH40DnAKeNtAoxZQjZ1XT8/i0gePBWrL7drFR9CaDqOUuZOYBsyivi03' \
             'aWy0sNQ02Zxy0E2I/Z5zFuB4GuIzpIwWIUMo9tE= test'


@pytest.fixture
def client():
    app.app.config['TESTING'] = True

    with app.app.test_client() as client:
        yield client


def test_post(client):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    data = json.dumps({
      'username': 'test',
      'user_public_key': PUBLIC_KEY
    })
    response = client.post('/', data=data, headers=headers)

    response_data = json.loads(response.data)

    assert 'key' in response_data
    assert response_data['key'].startswith('ssh-rsa-cert-v01@openssh.com')
