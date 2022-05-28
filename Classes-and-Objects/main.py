class Student:

    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
        pass

    def change_name(self, new_name):
        self.name = new_name
        return new_name

    def change_age(self, new_age):
        self.age = int(new_age)
        return new_age

    def add_track(self, new_track):
        (self.tracks).append(new_track)
        return self.tracks

    def get_score(score):
        return score


Bob = Student("Bob", 26, ["FE", "BE"], 20.90)


# Expected methods
Bob.change_name("Peter")

Bob.change_age(34)

Bob.add_track("UI/UX")

Bob.get_score()
