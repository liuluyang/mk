# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/5 14:12


class Company:

    def __init__(self):
        self.name = 'mk'
        self.staff_list = []

    def append_staff(self, staff):

        self.staff_list.append(staff)
        staff.company = self
        pass


class Staff:

    def __init__(self):
        self.name = None
        self.company = None

c1 = Company()
s1 = Staff()
c1.append_staff(s1)

# print(c1.staff_list[0].company)