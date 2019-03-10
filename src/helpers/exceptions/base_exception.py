


class BaseException(Exception):
    """docstring for BaseException."""
    def __init__(self):
        super(BaseException, self).__init__()

    @property
    def message(self):
        # str(e.orig) + ' - ' +  e.statement
        orig = str(e.orig)
        message = 'Sentence: {self.statement}, Orig: {orig}'
        logging.info('500 - {message}')
        return message
