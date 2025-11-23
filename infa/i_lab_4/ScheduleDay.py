class ScheduleDay():

    def __init__(self, name: str):
        self.name = name
        self.classes = []
        self.other = {}

    def add_subject(self, subject):
        self.classes.append(subject)    

