class icc(object):
    def __init__(self, name, teamCount):
        self.teams = teamCount
        self.name = name

    def noOfTeams(self):
        print("Total no. of participated teams in " + str(self.name) + \
        " is: " + str(self.teams))

    def noOfJeams(self):
        print("Total no. of participated teams in " + str(self.name) + \
        " is: " + str(self.teams))

ct = icc('Champions Trophy', 8)
wc = icc('World Cup', 10)

ct.noOfTeams()
wc.noOfTeams()

# print(type(ct))