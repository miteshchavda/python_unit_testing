from s3_logging import S3Logging

class CalculateV2AndLog(object):

    def __init__(self):

        self.logging = S3Logging()

    def add(self, a, b):

        self.logging.info(f'Calculating {a} + {b}')

        return a + b

    def substract(self, a, b):

        self.logging.info(f'Calculating {a} - {b}')

        return a - b

    def multiply(self, a,b):

        self.logging.info(f'Calculating {a} * {b}')

        return a * b

    def divide(self, a, b):

        self.logging.info(f'Calculating {a} / {b}')

        return a / b
