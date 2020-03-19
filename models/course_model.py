from typing import Dict

from utils.db import db


class CourseModel(db.Model):
    __tablename__ = "Courses"

    _id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String, nullable=False)
    code = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    section_type = db.Column(db.String, nullable=False)
    section_name = db.Column(db.String, nullable=False)
    meeting_time = db.Column(db.String, nullable=False)
    instructor = db.Column(db.String, nullable=False)
    building = db.Column(db.String, nullable=False)

    def json(self) -> Dict:
        if self.meeting_time != "TBA":
            days, time = self.meeting_time.split()
        else:
            days, time = "TBA", "TBA"

        return {
            "_id": self._id,
            "term": self.term,
            "code": self.code,
            "title": self.title,
            "section_type": self.section_type,
            "section_name": self.section_name,
            "days": days,
            "time": time,
            "instructor": self.instructor,
            "building": self.building,
        }
