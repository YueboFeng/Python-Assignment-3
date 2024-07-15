from custom_errors import *
from runner import *
from competition import *

def create_runner(runner_name, runner_age, runner_country, sprint_speed, endurance_speed):
    """Creates a Runner object."""
    return Runner(runner_name, runner_age, runner_country, sprint_speed, endurance_speed)

def create_competition(runners, rounds, distances_short, distances_long):
    """Creates a Competition object."""
    return Competition(runners, rounds, distances_short, distances_long)

def main():
    """Main function to manage the creation of runners and competition and then conduct the competition."""
    # Ask the user to create runners (until they decide to add no more)
    runners = []
    print("Please add runner.")

    # TODO: Take input for several runners until the user choses to quit
    while True:
        runner_info = input("FORMAT: name/age/country/sprint speed/marathon speed (blank line stops): ")

        if runner_info != "":
            runner_info_list = runner_info.strip().split("/")

            if len(runner_info_list) != 5:
                print("Error. Expected 5 fields.")
                continue

            try:
                name = runner_info_list[0]
                age = int(runner_info_list[1])
                country = runner_info_list[2]
                sprint_speed = float(runner_info_list[3])
                marathon_speed = float(runner_info_list[4])
            except ValueError:
                print("Error. Expected: age as an int, sprint speed as a float, endurance speed as a float.")
        
            runners.append(create_runner(name, age, country, sprint_speed, marathon_speed))

        else:
            break

    print("Done creating runners!\n")
    
    print(runners)

    # Ask the user to create a competition
    distances_short = []
    distances_long = []

    print("Please create competition.")

    while True:
        comp_info = input("FORMAT: rounds/sprint distances/marathon distances: ")

        comp_info_list = comp_info.strip().split("/")

        if len(comp_info_list) != 3:
            print("Error. Expected 3 fields.")
            continue
        else:
            try:
                rounds = int(comp_info_list[0])
                distances_short = [float(i) for i in comp_info_list[1].strip().split(",")]
                distances_long = [float(i) for i in comp_info_list[2].strip().split(",")]
            except ValueError:
                print("Error. Expected: ** 3 fields ** with rounds as an int, distances split with ','.")

            if len(distances_short) != rounds or len(distances_short) != rounds:
                print("Error. number of both sprint distances and marathon distances should be the same as rounds.")
                continue
            else:
                break

    comp = create_competition(runners, rounds, distances_short, distances_long)

    print("Done creating competition!\n")

    # Conduct the competition
    comp.conduct_competition()

    # Reveal the results!
    comp.print_leaderboard()

if __name__ == '__main__':
    main()

