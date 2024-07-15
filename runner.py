from custom_errors import *

class Runner:
    
    """" Represents a runner with atrributes and methods for managing energy and running races. """

    max_energy = 1000 # maximun energy a runner has

    def __init__(self,
                 name: str,
                 age: int,
                 country: str,
                 sprint_speed: float,
                 endurance_speed: float) -> None:
        
        """ Initilizes a Runner object. """

        #Name validation
        if type(name) != str:
            raise CustomTypeError(f"Incorrect input type for name. Expected str, got {type(name)} instead.")
        if type(name) == str:
            for char in name:
                if not (char.isalnum() or char.isspace()):
                    raise CustomValueError("Incorrect input value for name. Expected alphabets, numbers and spaces, got others contained.")
        self.name = name
        
        #Age validation
        if type(age) != int:
            raise CustomTypeError(f"Incorrect input type for age. Expected int, got {type(age)} instead.")
        if age < 5 or age > 120:
            raise CustomValueError("Incorrect input value for age. Expeced number valued between 5 and 120, got number out of range.")
        self.age = age

        #Country validation
        if type(country) != str:
            raise CustomTypeError(f"Incorrect input type for country. Expected str, got {type(country)} instead.")
        countries = []
        with open ("countries.csv") as f:
            header = f.readline().strip().split(',')[1:]
            for line in f:
                field = line.strip().split(",")[3]
                countries.append(field)
        if country not in countries:
            raise CustomValueError("Incorrect input value for country. Expected those in countries.csv, got out of range instead.")
        self.country = country

        #Sprint speed validation
        if type(sprint_speed) != float:
            raise CustomTypeError(f"Incorrect input type for sprint_speed. Expected float, got {type(sprint_speed)} instead.")
        if sprint_speed < 2.2 or sprint_speed > 6.8:
            raise CustomValueError("Incorrect input value for sprint_speed. Expected float valued between 2.2 and 6.8, got float out of range.")
        self.sprint_speed = sprint_speed

        #Endurance speed validation
        if type(endurance_speed) != float:
            raise CustomTypeError(f"Incorrect input type for endurance_speed. Expeced float, got {type(endurance_speed)} instead.")
        if endurance_speed < 1.8 or endurance_speed > 5.4:
            raise CustomValueError("Incorrect input value for endurance_speed. Expeced float valued between 1.8 and 5.4, got float out of range.")
        self.endurance_speed = endurance_speed

        self.energy = Runner.max_energy
    
    def drain_energy(self, drain_points: int) -> None:
        """Drains the specified amount of energy from the runner."""
        if type(drain_points) != int:
            raise CustomTypeError(f"Incorrect input type for drain_energy. Expected int, got {type(drain_points)} instead.")
        if drain_points < 0 or drain_points > Runner.max_energy:
            raise CustomValueError("Incorrect input value for endurance_speed. Expeced int valued between 0 and 1000, got number out of range.")
        if self.energy < drain_points:
            self.energy = 0
        else:
            self.energy -= drain_points
    
    def recover_energy(self, recovery_amount: int) -> None:
        """Recovers the specified amount of energy for the runner."""
        if type(recovery_amount) != int:
            raise CustomTypeError(f"Incorrect input type for recover_energy. Expected int, got {type(recovery_amount)} instead.")
        if recovery_amount > Runner.max_energy:
            raise CustomValueError("Incorrect input value for recover_energy. Expeced number more than max_energy, got less than instead.")
        if self.energy < Runner.max_energy:
            self.energy += recovery_amount
        else:
            self.energy = Runner.max_energy
    
    def run_race(self,
                 race_type: str,
                 distance: float) -> float:
        """Calculates the time taken to run a race of the given type and distance."""
        if type(distance) != float:
            raise CustomTypeError(f"Incorrect input type for distance. Expected float, got {type(distance)} instead.")
        if distance <= 0:
            raise CustomValueError("Incorrect input value for distance. Expected number greater than 0.")
        if type(race_type) != str:
            raise CustomTypeError(f"Incorrect input type for run_type. Expected str, got {type(race_type)} instead.")
        if race_type == "short":
            return round(distance * 1000 / self.sprint_speed, 2)
        elif race_type == "long":
            return round(distance * 1000 / self.endurance_speed, 2)
        else:
            raise CustomValueError("Incorrect input value for race_type. Expected only 'long' or 'short'.")
    
    def __str__(self):
        return f"Name: {self.name} Age: {self.age} Country: {self.country}"

if __name__ == '__main__':
    """Returns a string representation of the runner."""

    runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
    
    # running a short race
    time_taken = runner.run_race('short', 2.0)
    print(f"Runner {runner.name} took {time_taken} seconds to run 2km!")
    


