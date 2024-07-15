from custom_errors import *
from abc import ABC, abstractmethod
from runner import Runner
from typing import List, Union
import math

class Race(ABC):
    """Abstract base class for different types of races."""

    def __init__(self, distance, runners: Union[List, None] = None):
        """Initializes a Race object with a given distance and an optional list of runners."""

        # validation of runners
        if runners == None:
            self.runners = []
        elif runners != None:
            if type(runners) != list:
                raise CustomTypeError(f"Incorrect input type for runners. Expeced list, got {type(runners)} instead.")
            self.runners = runners

        #validation of distance
        if type(distance) != float:
            raise CustomTypeError(f"Incorrect input type for distance. Expeced float, got {type(distance)} instead.")
        if distance <= 0:
            raise CustomValueError("Incorrect input value for distance. Expeced float more than 0.")
        self.distance = distance

        self.maximum_participants = 16
    
    def add_runner(self, runner: Runner):
        """Adds a runner to the race."""

        #validation of runner
        if type(runner) != Runner:
            raise CustomTypeError(f"Incorrect input type for runner. Expected Runner, got {type(runner)} instead.")
        if len(self.runners) >= self.maximum_participants:
            raise RaceIsFullError("Error. The number of participants is above the maximum.")
        if runner in self.runners:
            raise RunnerAlreadyExistsError("Error. The runner already exists. Cannot add repeatedly.")
        self.runners.append(runner)
    
    def remove_runner(self, runner: Runner):
        """Remova a runner from the race."""

        #validation of runner
        if type(runner) != Runner:
            raise CustomTypeError(f"Incorrect input type for runner. Expeced Runner, got {type(runners)} instead.")
        if runner not in self.runners:
            raise RunnerDoesntExistError("Error. The runner does NOT exists.")
        self.runners.remove(runner)
    
    @abstractmethod
    def conduct_race(self):
        """Abstract method to conduct the race. Must be implemented by subclasses."""
        pass

class ShortRace(Race):
    """Class representing a short race."""

    def __init__(self, distance, runners = None):
        """Initializes a ShortRace object with a given distance and an optional list of runners."""
        super().__init__(distance, runners)
        self.race_type = "short"
        self.maximum_participants = 8
        self.time_multiplier = 1.2
    
    def conduct_race(self) -> list:
        """Conducts the short race and returns the results."""
        result = []
        for i, runner in enumerate(self.runners):
            time_taken = runner.run_race("short", self.distance) * 1.2
            result.append((runner, time_taken))
        return result


class MarathonRace(Race):
    """Class representing a marathon race."""
    def __init__(self, distance, runners = []):
        """Initializes a ShortRace object with a given distance and an optional list of runners."""
        super().__init__(distance, runners)
        self.race_type = "long"
        self.energy_per_km = 100
        self.maximum_participants = 16
    
    def conduct_race(self) -> list:
        """Conducts the short race and returns the results."""
        result = []
        for i, runner in enumerate(self.runners):
            time_taken = 0
            for km in range(math.ceil(self.distance)):
                if runner.energy > 0:
                    time_taken += runner.run_race("long", self.distance)
                    runner.drain_energy(100)
                else:
                    time_taken = 'DNF'
                    break
            result.append((runner, time_taken))
        return result
        
if __name__ == '__main__':
    short_race = ShortRace(0.5)
    long_race = MarathonRace(5.0)

    # Add a Runner
    eli = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
    rup = Runner('Rupert', 23, 'Australia', 2.3, 1.9)

    long_race.add_runner(eli)
    long_race.add_runner(rup)

    result = long_race.conduct_race()
    print(result)
