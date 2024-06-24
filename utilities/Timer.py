import time

class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            raise Exception("Timer has not been started")
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        return elapsed_time

    def show_time(self):
         elapsed_time = self.stop()
         print(f"Elapsed time: {elapsed_time} seconds")
         