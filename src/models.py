class ClassRoom:
    def __init__(self, table_name):
        self.collection_name = table_name

    def create(self, db, data):
        collection = db[self.collection_name]
        building, room_number, capacity = data

        json_obj = {
            'building': building,
            'room_number': int(room_number),
            'capacity': int(capacity)
        }
        result = collection.find_one({'building': building, 'room_number': int(room_number)})
        if not result:
            collection.insert_one(json_obj)

class Department:
    def __init__(self, table_name):
        self.collection_name = table_name

    def create(self, db, data):
        collection = db[self.collection_name]
        dept_name, building, budget = data

        json_obj = {
            'dept_name': dept_name,
            'building': building,
            'budget': float(budget)
        }
        result = collection.find_one({'dept_name': dept_name})
        if not result and float(budget) > 0:
            collection.insert_one(json_obj)

class Course:
    def __init__(self, table_name):
        self.collection_name = table_name

    def create(self, db, data):
        collection = db[self.collection_name]
        course_id, title, dept_name, credits = data

        json_obj = {
            'course_id': course_id,
            'title': title,
            'dept_name': dept_name,
            'credits': int(credits)
        }
        result = collection.find_one({'course_id': course_id})
        if not result:
            collection.insert_one(json_obj)

class Instructor:
    def __init__(self, table_name):
        self.collection_name = table_name

    def create(self, db, data):
        collection = db[self.collection_name]
        id, name, dept_name, salary = data

        json_obj = {
            'id': id,
            'name': name,
            'dept_name': dept_name,
            'salary': float(salary)
        }
        result = collection.find_one({'id': id})
        if not result and float(salary) > 29000:
            collection.insert_one(json_obj)

class Section:
    def __init__(self, table_name):
        self.collection_name = table_name

    def create(self, db, data):
        collection = db[self.collection_name]
        (
            course_id, sec_id, semester, year,
            building, room_number, time_slot_id
        ) = data

        json_obj = {
            'course_id': course_id,
            'sec_id': sec_id,
            'semester': semester,
            'year': int(year),
            'building': building,
            'room_number': room_number,
            'time_slot_id': time_slot_id
        }
        map_station = ['Fall', 'Winter', 'Spring', 'Summer']
        result = collection.find_one({
            'course_id': course_id, 'sec_id': sec_id,
            'semester': semester, 'year': int(year)
        })
        if not result and int(year) > 1701 and int(year) < 2100 and semester in map_station:
            collection.insert_one(json_obj)

class Teaches:
    def __init__(self, table_name):
        self.collection_name = table_name

    def create(self, db, data):
        collection = db[self.collection_name]
        (
            id, course_id, sec_id, semester, year
        ) = data

        json_obj = {
            'id': id,
            'course_id': course_id,
            'sec_id': sec_id,
            'semester': semester,
            'year': int(year)
        }
        result = collection.find_one({
            'id': id, 'course_id': course_id,
            'sec_id': sec_id, 'semester': semester,
            'year': int(year)
        })
        # Essa verificação de ano não estava no SQL mas coloquei
        if not result and int(year) > 1701 and int(year) < 2100:
            collection.insert_one(json_obj)

class Student:
    def __init__(self, table_name):
        self.collection_name = table_name

    def create(self, db, data):
        collection = db[self.collection_name]
        id, name, dept_name, tot_cred = data

        json_obj = {
            'id': id,
            'name': name,
            'dept_name': dept_name,
            'tot_cred': int(tot_cred)
        }
        result = collection.find_one({'id': id})
        if not result and int(tot_cred) >= 0 and name:
            collection.insert_one(json_obj)

class Takes:
    def __init__(self, table_name):
        self.collection_name = table_name

    def create(self, db, data):
        collection = db[self.collection_name]
        (
            id, course_id, sec_id, semester, year, grade
        ) = data

        json_obj = {
            'id': id,
            'course_id': course_id,
            'sec_id': sec_id,
            'semester': semester,
            'year': int(year),
            'grade': grade
        }
        result = collection.find_one({
            'id': id, 'course_id': course_id,
            'sec_id': sec_id, 'semester': semester,
            'year': int(year)
        })
        # Essa verificação de ano não estava no SQL mas coloquei
        if not result and int(year) > 1701 and int(year) < 2100:
            collection.insert_one(json_obj)

class Advisor:
    def __init__(self, table_name):
        self.collection_name = table_name

    def create(self, db, data):
        collection = db[self.collection_name]
        s_id, i_id = data

        json_obj = {
            's_id': s_id,
            'i_id': i_id
        }
        result = collection.find_one({'s_id': s_id, 'i_id': i_id})
        if not result:
            collection.insert_one(json_obj)

class TimeSlot:
    def __init__(self, table_name):
        self.collection_name = table_name

    def create(self, db, data):
        collection = db[self.collection_name]
        time_slot_id, day, start_hr, start_min, end_hr, end_min = data

        json_obj = {
            'time_slot_id': time_slot_id,
            'day': day,
            'start_hr': int(start_hr),
            'start_min': int(start_min),
            'end_hr': int(end_hr),
            'end_min': int(end_min)
        }
        result = collection.find_one({
            'time_slot_id': time_slot_id, 'day': day,
            'start_hr': int(start_hr), 'start_min': int(start_min),
            'end_hr': int(end_hr), 'end_min': int(end_min)
        })
        if not result \
            and int(start_hr) > 0 and int(start_hr) < 24 and \
            int(start_min) > 0 and int(start_min) < 60 and \
            int(end_hr) > 0 and int(end_hr) < 24 and \
            int(end_min) > 0 and int(end_min) < 60:
            collection.insert_one(json_obj)

class Prereq:
    def __init__(self, table_name):
        self.collection_name = table_name

    def create(self, db, data):
        collection = db[self.collection_name]
        course_id, prereq_id = data

        json_obj = {
            'course_id': course_id,
            'prereq_id': prereq_id
        }
        result = collection.find_one({
            'course_id': course_id, 'prereq_id': prereq_id
        })
        if not result:
            collection.insert_one(json_obj)
