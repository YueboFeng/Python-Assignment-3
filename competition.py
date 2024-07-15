from race import *
from runner import Runner
from custom_errors import CustomTypeError

class Competition:
    """Represents a comptition."""
    MAX_ROUNDS = 3

    def __get_ordinal(self, n):
        """Helper function to return the ordinal string for a given integer."""
        suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
        if 11 <= n % 100 <= 13:
            suffix = 'th'
        else:
            suffix = suffixes.get(n % 10, 'th')
        return f"{n}{suffix}"

    # In your Competition class
    def __init__(self, runners, rounds, distances_short, distances_marathon):
        """Initializes a Competition object."""
        if runners == None:
            self.runners = []
        elif runners != None:
            if type(runners) != list:
                raise CustomTypeError(f"Incorrect input type for runners. Expeced list, got {type(runners)} instead.")
        self.runners = runners

        if type(rounds) != int:
            raise CustomTypeError(f"Incorrect input type for rounds. Expeced int, got {type(rounds)} instead.")
        if rounds <= 0 or rounds > self.MAX_ROUNDS:
            raise CustomValueError("Incorrect input value for rounds. Expeced positive.")
        self.rounds = rounds

        if type(distances_short) != list:
            raise CustomTypeError(f"Incorrect input type for distances_short. Expeced list, got {type(distances_short)} instead.")
        if len(distances_short) > self.MAX_ROUNDS:
            raise CustomValueError("Error. The length of distances_short should not exceed MAX_ROUNDS.")
        for distance in distances_short:
            if distance <= 0:
                raise CustomValueError("Incorrect input value for distances_short. Expeced float more than 0 inside the list.")
        self.distances_short = distances_short

        if type(distances_marathon) != list:
            raise CustomTypeError(f"Incorrect input type for distances_marathon. Expeced list, got {type(distances_marathon)} instead.")
        if len(distances_marathon) > self.MAX_ROUNDS:
            raise CustomValueError("Error. The length of distances_marathon should not exceed MAX_ROUNDS.")
        for distance in distances_marathon:
            if distance <= 0:
                raise CustomValueError("Incorrect input value for distances_marathon. Expeced float more than 0 inside the list.")
        self.distances_marathon = distances_marathon

        self.leaderboard = {}

        for i in range(1, len(self.runners) + 1):
            self.leaderboard[self.__get_ordinal(i)] = None
     
    def conduct_competition(self):
        """Conducts the competition and returns the final leaderboard."""
        current_round = 1
        i = 0
        while current_round <= self.rounds:
            if i >= len(self.distances_short):
                break 
            # Conduct the short race with all runners
            short_race = ShortRace(self.distances_short[i], runners = self.runners)
            short_race.runners = self.runners
            short_result = self.conduct_race(short_race)

            # Conduct the Marathon race with all runners
            marathon = MarathonRace(self.distances_marathon[i], runners = self.runners)
            marathon.runners = self.runners
            marathon_result = self.conduct_race(marathon)
            
            # Recover energy for all DNF runners
            for runner, time in marathon_result:
                if time == "DNF":
                    runner.recover_energy(runner.max_energy)
            current_round += 1
            
            i += 1
            self.update_leaderboard(short_result)
            self.update_leaderboard(marathon_result)
        return self.leaderboard

    def conduct_race(self, race):
        """Conducts a given race and returns the results."""
        return race.conduct_race()

    def update_leaderboard(self, results):
        """Updates the leaderboard based on the results of a race."""
        sorted_result = sorted(results, key=lambda x: x[1])
        leaderboard_keys = list(self.leaderboard.keys())
        if all(value is None for value in self.leaderboard.values()):
            for i, runner_time in enumerate(sorted_result):
                if "DNF" not in runner_time:
                    self.leaderboard[leaderboard_keys[i]] = (runner_time[0].name, len(results) - (i+1))
                else:
                    self.leaderboard[leaderboard_keys[i]] = (runner_time[0].name, 0)
        else:
            for i, runner_time in enumerate(sorted_result):
                point = len(results) - (i+1) if "DNF" not in runner_time else 0
                for key, value in self.leaderboard.items():
                    if runner_time[0] == value[0]:
                        self.leaderboard[key] = (runner_time[0], value[1] + point)
                        break
            sorted_values = sorted(self.leaderboard.values(), key=lambda x: -x[1])
            for i, runner_time in enumerate(sorted_values):
                self.leaderboard[leaderboard_keys[i]] = runner_time

        
    def print_leaderboard(self):
        """Prints the leaderboard."""
        print("Leaderboard\n\n")
        for key, value in self.leaderboard.items():
            print(f"{key} - {value[0]} ({value[1]})")


if __name__ == '__main__':
    # Example usage
    runners = [
        Runner("Elijah", 19, 'Australia', 6.4, 5.2),
        Runner("Rupert", 67, 'Botswana', 2.2, 1.8),
        Runner("Phoebe", 12, 'France', 3.4, 2.8),
        Runner("Lauren", 13, 'Iceland', 4.4, 5.1),
        Runner("Chloe", 21, 'Timor-Leste', 5.2, 1.9)
    ]

    competition = Competition(runners, 3, [0.5, 0.6, 1.2], [4.0, 11.0, 4.5])
    _ = (competition.conduct_competition())
    competition.print_leaderboard()
