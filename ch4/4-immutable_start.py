# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass
from datetime import date


@dataclass()  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0


obj = ImmutableClass()
print(obj.value1)


# TODO: attempting to change the value of an immutable class throws an exception


# TODO: even functions within the class can't change anything


@dataclass(frozen=True)
class Citizen:
    nid: int
    fname: str
    lname: str
    gender: str
    dob: date

    def __post_init__(self):
        if self.gender not in ["F", "M"]:
            raise ValueError("Gender must be 'F' or 'M'")

    def to_json(self):
        return {
            "national_id": self.nid,
            "fname": self.fname,
            "lname": self.lname,
            "gender": self.gender,
            "dob": self.dob,
        }


john = Citizen(100939312, "john", "james", "F", date.today())
# leon = Citizen(100939312, "john", "james", "W")
print(john)

print(john.fname)
print(john.nid)
print(john.lname)
print(john.gender)
# john.name = "Jony"  # dataclasses.FrozenInstanceError: cannot assign to field 'name'


print(john.to_json())