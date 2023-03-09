# class Teacher:
#     school_name = "Global"
#
#
# def __init__(self, age):
#     self.age = age
#
#
# tear = Teacher("John")
# tear.age = 50
# tear.school_name = "SRM"
#
# print(tear.age, Teacher.school_name)

# a=10
# b="a"
# print(a+b)


class Father:
          def __init__(self):
                    self.f_age = 65


class Son(Father):
    def __init__(self, f_age):
        super().__init__()
        self.s_age = 20


s = Son(70)
print(s.f_age)
