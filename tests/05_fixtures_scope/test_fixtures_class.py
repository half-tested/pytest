# pytest tests/05_fixtures_scope/test_fixtures_class.py --setup-plan
# pytest tests/05_fixtures_scope --setup-plan

class TestFixturesScope:
    def test_one_class_fixtures_scope(
            self,
            fixture_module_level,
            fixture_class_level,
            fixture_package_level,
            fixture_function_level,
            fixture_session_level
    ):
        print("Executing test test_one_class_fixtures_scope")

    def test_two_class_fixtures_scope(
            self,
            fixture_module_level,
            fixture_class_level,
            fixture_package_level,
            fixture_function_level,
            fixture_session_level
    ):
        print("Executing test test_two_class_fixtures_scope")
