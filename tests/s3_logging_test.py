from s3_logging import S3Logging


class TestS3Logging(object):

    def test_info(self, mocker):

        print_mock = mocker.patch('builtins.print')

        s3_logging = S3Logging()

        s3_logging.info('Hello')

        assert print_mock.call_count == 1
        print_mock.assert_called_with('Info: Hello')

