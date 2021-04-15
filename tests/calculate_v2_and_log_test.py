from calculate_v2_and_log import CalculateV2AndLog
import pytest


@pytest.fixture
def calculate_v2_and_log(mocker):

    s3_logging_mock = mocker.patch('calculate_v2_and_log.S3Logging')
    s3_logging_mock.return_value.info.return_value = True

    return CalculateV2AndLog()


class TestCalculateV2(object):

    def test_add(self, calculate_v2_and_log):

        add = calculate_v2_and_log.add(1, 2)

        assert 3 == add

    def test_substract(self, calculate_v2_and_log):

        sub = calculate_v2_and_log.substract(10, 2)

        assert 8 == sub

    def test_multiply(self, calculate_v2_and_log):

        mul = calculate_v2_and_log.multiply(10, 9)

        assert 90 == mul

    def test_divide(self, calculate_v2_and_log):

        div = calculate_v2_and_log.divide(6, 2)

        assert 3 == div
