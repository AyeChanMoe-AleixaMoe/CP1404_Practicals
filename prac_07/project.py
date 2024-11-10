import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y').date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority: {self.priority}, cost: {self.cost_estimate: .2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage == 100

    def update(self, new_completion_percentage=None, new_priority=None):
        if new_completion_percentage is not None:
            self.completion_percentage = int(new_completion_percentage)
        if new_priority is not None:
            self.priority = int(new_priority)