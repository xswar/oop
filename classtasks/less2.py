class Human:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.friends = 0

    def update_friends(self, friends_count):
        self.friends = friends_count

    def add_friend(self):
        self.friends += 1

    def good_bye_friend(self):
        if self.friends > 0:
            self.friends -= 1


friend = Human('adil', 20)
print(friend.__dict__)

friend.add_friend()
print(friend.__dict__)

friend.good_bye_friend()
print(friend.__dict__)
