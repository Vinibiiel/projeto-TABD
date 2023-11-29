from connect import Connection
from models import Prereq, TimeSlot, Advisor, Takes, Student, Teaches, Section, Instructor, Course, Department, ClassRoom
import json

model_map = {
    'prereq': Prereq('prereq'),
    'time_slot': TimeSlot('time_slot'),
    'advisor': Advisor('advisor'),
    'takes': Takes('takes'),
    'student': Student('student'),
    'teaches': Teaches('teaches'),
    'section': Section('section'),
    'instructor': Instructor('instructor'),
    'course': Course('course'),
    'department': Department('departament'),
    'classroom': ClassRoom('classroom')
}

if __name__ == "__main__":
    new_connection = Connection()
    db = new_connection.connect_to_mongo()

    with open('./data/data.json', 'r') as file:
        data_list = json.load(file)
        for data in data_list:
            model = model_map.get(data.get('table_name'))
            if not model:
                continue
            try:
                model.create(db, data.get('data'))
            except: 
                pass           
    new_connection.close_connection()