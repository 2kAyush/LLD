from __future__ import annotations

class Student:
    def __init__(self):
        self.name : str = None
        self.age = None
        self.height = None
        self.weight = None

class StudentBuilder:
    def __init__(self):
        self.student = Student()

    def set_name(self, name) -> StudentBuilder:
        self.student.name = name
        return self

    def set_age(self, age) -> StudentBuilder:
        self.student.age = age
        return self

    def set_height(self, height) -> StudentBuilder:
        self.student.height = height
        return self

    def set_weight(self, weight) -> StudentBuilder:
        self.student.weight = weight
        return self

    def validate_and_build(self) -> Student:
        # do some validation here first
        if self.student.name.startswith("0"):
            print("Name can't start with 0")
        return self.student

if __name__ == "__main__":
    print("started")
    student = (
        StudentBuilder().set_name("Ayush").
        set_age(24).
        set_height(178).
        set_weight(70).
        validate_and_build()
    )
    print(student)
    print("end")