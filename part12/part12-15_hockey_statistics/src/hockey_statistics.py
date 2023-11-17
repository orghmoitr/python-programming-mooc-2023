# Write your solution here

import json


class HockeyPlayer:

    def __init__(self, name: str, nationality: str, assists: int,
                 goals: int, penalties: int, team: str, games: int):
        self.__name = name
        self.__nationality = nationality
        self.__assists = assists
        self.__goals = goals
        self.__penalties = penalties
        self.__team = team
        self.__games = games

    def name(self):
        return self.__name

    def nationality(self):
        return self.__nationality

    def goals(self):
        return self.__goals

    def assists(self):
        return self.__assists

    def team(self):
        return self.__team

    def games(self):
        return self.__games


class HockeyStatistics:

    def __init__(self):
        self.__hockeyplayers = []

    def add_statistics(self, name: str, nationality: str, assists: int,
                       goals: int, penalties: int, team: str, games: int):
        hockeyplayer = HockeyPlayer(name, nationality, assists,
                                    goals, penalties, team, games)
        self.__hockeyplayers.append(hockeyplayer)

    def hockeyplayers(self):
        return self.__hockeyplayers


class HockeyStatisticsApplication:

    def __init__(self):
        self.__hockeystatistics = HockeyStatistics()
        self.__filehandler = FileHandler()

    def read_from_file(self):
        filename = input("file name: ")
        for item in self.__filehandler.load_file(filename):
            self.__hockeystatistics.add_statistics(item["name"], item["nationality"],
                                                   item["assists"], item["goals"],
                                                   item["penalties"], item["team"],
                                                   item["games"])
        print(f"read the data of {len(self.__filehandler.load_file(filename))} players")

    def help(self):
        print()
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def search_for_player(self):
        name = input("name: ")
        for hockeyplayer in self.__hockeystatistics.hockeyplayers():
            if name == hockeyplayer.name():
                print()
                print((f"{hockeyplayer.name():21}{hockeyplayer.team():3}"
                       f"{hockeyplayer.goals():4} + {hockeyplayer.assists():2} = {hockeyplayer.assists()+hockeyplayer.goals():3}"))
        print("123456789012345678901234567890123456789")

    def teams(self):
        teams = []
        for hockeyplayer in self.__hockeystatistics.hockeyplayers():
            if hockeyplayer.team() not in teams:
                teams.append(hockeyplayer.team())
        for team in sorted(teams):
            print(team)

    def countries(self):
        countries = []
        for hockeyplayer in self.__hockeystatistics.hockeyplayers():
            if hockeyplayer.nationality() not in countries:
                countries.append(hockeyplayer.nationality())
        for country in sorted(countries):
            print(country)

    def by_points_scored(self, hockeyplayer: HockeyPlayer):
        return hockeyplayer.goals() + hockeyplayer.assists()
    
    def players_in_team(self):
        team = input("team: ")
        hockeyplayers = []
        for hockeyplayer in self.__hockeystatistics.hockeyplayers():
            if hockeyplayer.team() == team:
                hockeyplayers.append(hockeyplayer)
        hockeyplayers = sorted(hockeyplayers, key=self.by_points_scored, reverse=True)
        for hockeyplayer in hockeyplayers:
            print((f"{hockeyplayer.name():21}{hockeyplayer.team():3}"
                   f"{hockeyplayer.goals():4} + {hockeyplayer.assists():2} = {hockeyplayer.assists()+hockeyplayer.goals():3}"))

    def players_from_country(self):
        country = input("country: ")
        hockeyplayers = []
        for hockeyplayer in self.__hockeystatistics.hockeyplayers():
            if hockeyplayer.nationality() == country:
                hockeyplayers.append(hockeyplayer)
        hockeyplayers = sorted(hockeyplayers, key=self.by_points_scored, reverse=True)
        for hockeyplayer in hockeyplayers:
            print((f"{hockeyplayer.name():21}{hockeyplayer.team():3}"
                   f"{hockeyplayer.goals():4} + {hockeyplayer.assists():2} = {hockeyplayer.assists()+hockeyplayer.goals():3}"))

    def most_points(self):
        how_many = int(input("how many: "))
        hockeyplayers = []
        for hockeyplayer in self.__hockeystatistics.hockeyplayers():
            hockeyplayers.append(hockeyplayer)
        hockeyplayers = sorted(hockeyplayers, key=self.by_points_scored, reverse=True)
        count = 0
        for hockeyplayer in hockeyplayers:
            if count == how_many:
                break
            print((f"{hockeyplayer.name():21}{hockeyplayer.team():3}"
                   f"{hockeyplayer.goals():4} + {hockeyplayer.assists():2} = {hockeyplayer.assists()+hockeyplayer.goals():3}"))
            count += 1

    def by_goals_scored(self, hockeyplayer: HockeyPlayer):
        return hockeyplayer.goals(), hockeyplayer.games()*-1
            
    def most_goals(self):
        how_many = int(input("how many: "))
        hockeyplayers = []
        for hockeyplayer in self.__hockeystatistics.hockeyplayers():
            hockeyplayers.append(hockeyplayer)
        hockeyplayers = sorted(hockeyplayers, key=self.by_goals_scored, reverse=True)
        count = 0
        for hockeyplayer in hockeyplayers:
            if count == how_many:
                break
            print((f"{hockeyplayer.name():21}{hockeyplayer.team():3}"
                   f"{hockeyplayer.goals():4} + {hockeyplayer.assists():2} = {hockeyplayer.assists()+hockeyplayer.goals():3}"))
            count += 1
            
    def execute(self):
        self.read_from_file()
        self.help()
        while True:
            print()
            command = int(input("command: "))
            if command == 0:
                break
            elif command == 1:
                self.search_for_player()
            elif command == 2:
                self.teams()
            elif command == 3:
                self.countries()
            elif command == 4:
                self.players_in_team()
            elif command == 5:
                self.players_from_country()
            elif command == 6:
                self.most_points()
            elif command == 7:
                self.most_goals()


class FileHandler:

    def __init__(self):
        self.__filename = ""

    def load_file(self, filename):
        self.__filename = filename
        hockeystatistics = []
        with open(self.__filename) as f:
            data = f.read()
        hockeystatistics = json.loads(data)
        return hockeystatistics


application = HockeyStatisticsApplication()
application.execute()
