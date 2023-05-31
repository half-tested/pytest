# pytest tests/05_fixtures_scope/test_fixtures_function.py --setup-plan
# pytest tests/05_fixtures_scope --setup-plan

def test_one_function_fixtures_scope(
        fixture_module_level,
        # class level fixture is for class
        # but if use then it will work as
        # module fixture but executes after
        # fixture_class_level,
        fixture_package_level,
        fixture_function_level,
        fixture_session_level
):
    print("Executing test test_one_function_fixtures_scope")


def test_two_function_fixtures_scope(
        fixture_module_level,
        fixture_package_level,
        fixture_function_level,
        fixture_session_level
):
    print("Executing test test_two_function_fixtures_scope")
