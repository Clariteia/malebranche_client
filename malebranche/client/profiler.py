import cProfile, pstats


class Profiler:
    def __init__(self):
        self.profiler = cProfile.Profile()

    def start(self):
        self.profiler.enable()

    def stop(self):
        self.profiler.disable()

    def print_results(self):
        stats = pstats.Stats(self.profiler)
        stats.print_stats()
