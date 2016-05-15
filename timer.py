class timer:
    """ This is a timer that is used for the state system
    """
    from time import time

    def __init__(self):
        self.start_time = 0

    def start(self):
        self.start_time = self.time()

    def elapsed_time(self):
        return self.time() - self.start_time
