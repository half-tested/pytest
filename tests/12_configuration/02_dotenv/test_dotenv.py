#
# pip3 install pytest-dotenv
#
# May be used by using default ".env" key=value property file placed in root
# or add pytest.ini line with property "env_files=.test.env"
# or pass argument "--envfile path/to/.env"


# pytest tests/12_configuration/02_dotenv
# pytest -c tests/12_configuration/02_dotenv/pytest.ini tests/12_configuration/02_dotenv/test_dotenv.py
def test_dotenv(user):
    user_username, user_password = user
    print(f"test using user_username='{user_username}', user_password='{user_password}'")