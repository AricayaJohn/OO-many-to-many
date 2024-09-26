# import ipdb
from lib.visit import Visit
class Museum:
    def __init__(self, name):
        self.name = name
    #create a relationship to visit
    def visits(self):
        return [visit for visit in Visit.all if visit.museum == self]

    #create a relationship to visitor
    def visitors(self):
        return [visit.visitor for visit in self.visits()]

    def check_in(self, visitor, date):
        return Visit(self, visitor, date)
        uniq_visitors = []
        for visit in self.visits():
            if not visit.visitor in uniq_visitors:
                uniq_visitors.append(visit.visitor)

        return uniq_visitors

    def __repr__(self):
        return f'<Museum name="{self.name}">'

# m1 = Museum("Botanical")
# m2 = Museum("The Met")

# ipdb.set_trace()