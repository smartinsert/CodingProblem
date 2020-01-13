class CallCenter:
    def __init__(self, respondents, managers, director):
        self.respondents = respondents
        self.managers = managers
        self.director = director
        self.respondents_queue = list()
        self.call_queue = list()
        for respondent in respondents:
            respondent.call_center = self
            if not respondent.call:
                self.respondents_queue.append(respondent)

    def route_respondent(self, respondent):
        if len(self.call_queue):
            respondent.take_call(self.call_queue.pop(0))
        else:
            self.respondents_queue.append(respondent)

    def route_call(self, call):
        if len(self.respondents_queue):
            self.respondents_queue.pop(0).take_call(call)
        else:
            self.call_queue.append(call)


class Call:
    def __init__(self, issue):
        self.issue = issue
        self.employee = None

    def resolve(self, handled):
        if handled:
            self.issue = None
        self.employee.finish_call(handled)

    def apologize_and_hangup(self):
        self.employee = None


class Employee:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager
        self.call = None

    def take_call(self, call):
        if self.call:
            self.escalate(call)
        else:
            self.call = call
            self.call.employee = self

    def escalate(self, call):
        if self.manager:
            self.manager.take_call(call)
        else:
            call.apologize_and_hangup()

    def finish_call(self, handled=True):
        if not handled:
            if self.manager:
                self.manager.take_call(self.call)
            else:
                self.call.apologize_and_hangup()
        self.call = None


class Respondent(Employee):
    def finish_call(self, handled=True):
        super(Respondent, self).finish_call(handled)
        self.call_center.route_respondent(self)


class Manager(Employee):
    def __init__(self, name):
        super(Manager, self).__init__(name, Director)


class Director(Employee):
    def __init__(self, name):
        super(Director, self).__init__(name, None)