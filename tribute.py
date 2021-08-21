#* tribute.py

class Tribute:
    # Constructor
    def __init__(self, Name, Gender, Age, District, Strengths, Weaknesses, Health=100, PTS="UNEVALUATED", *Inventory):
        '''"Constructs" an instance of this class with the provided parameters'''
        self.name = Name
        self.gender = Gender
        self.age = (Age if type(Age) is int else int(Age))
        self.district = (District if type(District) is int else int(District))
        self.strengths = (Strengths if Strengths is not None else [])
        self.weaknesses = (Weaknesses if Weaknesses is not None else [])
        self.health = Health
        self._training_score = PTS
        self._grey_scale_skills = []
        self.inventory = (Inventory if Inventory is not None else [])
            
    # Training Score Methods
    @property   # GETTER
    def private_training_score(self):
        return self._training_score
    @private_training_score.setter  # SETTER
    def private_training_score(self, Score):
        self._training_score = Score
    @private_training_score.deleter # DELETER
    def private_training_score(self):
        self._training_score = "UNEVALUATED"
        
    # Grey-Scale-Skills Methods
    @property   # GETTER
    def arena_skills(self):
        return self._grey_scale_skills
    @arena_skills.setter  # SETTER
    def arena_skills(self, *Skills):
        if isinstance(Skills, list) or isinstance(Skills, tuple):
            for skill in Skills:
                self._grey_scale_skills.append(skill)
        else:
            self._grey_scale_skills = Skills
    @arena_skills.deleter # DELETER
    def arena_skills(self):
        self._grey_scale_skills = []
    
    def print_dict(self):
        """Returns The __dict__ of the object."""
        print("\n\n", self.__dict__, "\n\n")

"""This Module Is For The Tribute Class & Its Functionality."""
# Fetches User Input
def ask_for_character(Default: bool=False):
    """Fetches Serializable Tribute Data."""
    if Default:
        tmp_name = 'Placeholder Name'
        tmp_gender = 'Male'
        tmp_age = 12
        tmp_district = 1
        tmp_strengths = 's_one, s_two, s_three'
        tmp_weaknesses = 'w_one, w_two, w_three'
    else:
        tmp_name = input("Please Enter Your Name.\n")
        tmp_gender = input("Please Enter Your Gender.\n")
        tmp_age = int(input("Please Enter Your Age. \n(Numerical Values Only)\n"))
        tmp_district = input("Please Enter Your District.\n")
        tmp_strengths = input("Please Enter Your Strengths. \n(Separated By Commas)\n")
        tmp_weaknesses = input("Please Enter Your Weaknesses. \n(Separated By Commas)\n")
    return tmp_name, tmp_gender, tmp_age, tmp_district, tmp_strengths, tmp_weaknesses



def main():
    sample_name, sample_gender, sample_age, sample_district, sample_strengths, sample_weaknesses = ask_for_character(True)
    sampleTribute = Tribute(sample_name, sample_gender, sample_age, sample_district, sample_strengths.split(", "), sample_weaknesses.split(", "))
    sampleTribute.print_dict()
    sampleTribute.private_training_score(11)
    print(f"The Private Training Score For {sampleTribute.name} is {sampleTribute.private_training_score}.")

if __name__ == "__main__":
    print("\n\n")
    main()
    print("\n\n")
else:
    print(f"{__name__} has been successfully imported.\n")
