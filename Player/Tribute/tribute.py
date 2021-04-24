class Tribute:
    def __init__(self, Name, Age, District, Strengths, Weaknesses, Health=100, PTS=None, GSS=None, Inventory=None):
        self.name = Name
        self.age = Age
        self.district = District
        self.strengths = Strengths
        self.weaknesses = Weaknesses
        self.health = Health
        self.private_training_score = PTS
        self.grey_scale_skills = GSS
        self.inventory = Inventory
    
    def print_dict(self):
        """Returns The __dict__ of the object.
        """
        print("\n\n", self.__dict__, "\n\n")


def main():
    sampleTribute = Tribute("Sample Tribute", 12, 3, ["Climbing", "Swimming", "Archery"], ["Hiding", "Foraging", "Locating Water Sources"])
    sampleTribute.print_dict()

if __name__ == "__main__":
    main()
else:
    print(f"{__name__} has been imported.")