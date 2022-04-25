

def parkruns():
    return [
        ParkRun('kirkwall', 100)
    ]


class ParkRun:
    def __init__(self, name, first_race):
        self.name = name
        self.first_race = first_race