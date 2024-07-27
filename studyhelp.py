import pickle
from datetime import datetime


class StudySession:
    def __init__(self, subject, topic, hours, date):

        self.subject = subject
        self.topic = topic
        self.hours = hours
        self.date = date
