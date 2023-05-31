import datetime

from assertpy import assert_that


def test_assert_dates():
    today = datetime.datetime.today()
    yesterday = today - datetime.timedelta(days=1)

    assert_that(yesterday).is_before(today)
    assert_that(today).is_after(yesterday)

    middle = today - datetime.timedelta(hours=12)
    assert_that(middle).is_between(yesterday, today)


def test_assert_truncated_datetime():
    today = datetime.datetime.today()
    today_0us = today - datetime.timedelta(microseconds=today.microsecond)
    today_0s = today - datetime.timedelta(seconds=today.second)
    today_0h = today - datetime.timedelta(hours=today.hour)

    assert_that(today).is_equal_to_ignoring_milliseconds(today_0us)
    assert_that(today).is_equal_to_ignoring_seconds(today_0s)
    assert_that(today).is_equal_to_ignoring_time(today_0h)
    assert_that(today).is_equal_to(today)


def test_assert_datetime_units():
    # 1980-01-02 03:04:05.000006
    x = datetime.datetime(1980, 1, 2, 3, 4, 5, 6)

    assert_that(x).has_year(1980)
    assert_that(x).has_month(1)
    assert_that(x).has_day(2)
    assert_that(x).has_hour(3)
    assert_that(x).has_minute(4)
    assert_that(x).has_second(5)
    assert_that(x).has_microsecond(6)

    