"""
    Athlos fixture maker by team Eight085
"""

def noOfRounds(teams):
    counter = 2
    while counter <= len(teams):
        counter = counter * 2
    return counter


def Halves(teams, matches):
    if len(teams) % 2 == 0:
        upperhalf = (matches + 1)/2
        lowerhalf = (matches + 1)/2
    else:
        upperhalf = ((matches + 1)/2) + 0.5
        lowerhalf = ((matches + 1)/2) + 0.5 
    return upperhalf, lowerhalf   


def byefunc(rounds, teams):
    byes = rounds - len(teams)
    return byes


def fixture():
    print(teams[0])
    print("|------")
    print(teams[1])
    print()
    print(teams[2])
    print("|------")
    print(teams[3])
    print()
    print(teams[4])
    print("|------")
    print(teams[5])
    print()
    print(teams[6])
    print("|------")
    print(teams[7])
    print("..............")
    print(teams[8])
    print("|------")
    print(teams[9])
    print()
    print(teams[10])
    print("|------")
    print(teams[11])
    print()
    print(teams[12])
    print("|------")
    print(teams[13])
    print()
    print(teams[14])
    print("|------")
    print(teams[15])
    print()


def byefixture():
    pass


def FFfunc():
    if __name__ == '__main__':
        # teams = input("Enter a list: ").split(",")
        teams = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        matches = len(teams) - 1
        rounds = noOfRounds(teams)
        if len(teams) % 2 == 0:
            print(f"The number of teams in upper and lower half, ", Halves(teams, matches))
            print(f"The number of total matches to be played, ", matches)
            print(f"Total number of teams/players, ", teams )
            fixture()
        else:
            print(f"Number of byes, ", byefunc(rounds, teams))
            print(f"The number of teams in upper and lower half, ", Halves(teams, matches))
            print(f"The number of total matches to be played, ", matches)
            print(f"Total number of teams/players, ", teams )
            byefixture()

FFfunc()