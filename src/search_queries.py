from connect import Connection

def query1():
    return [
    {
        # Primeiro inner Student -> Advisor
        "$lookup": {
            "from": "advisor",
            "localField": "id",
            "foreignField": "s_id",
            "as": "advisor"
        }
    },
    {
        "$unwind": "$advisor"
    },
    {
        # Segundo inner Advisor -> Instructor
        "$lookup": {
            "from": "instructor",
            "localField": "advisor.i_id",
            "foreignField": "id",
            "as": "instructor"
        }
    },
    {
        "$unwind": "$instructor"
    },
    {
        # Terceiro inner Instructor -> Teaches
        "$lookup": {
            "from": "teaches",
            "localField": "instructor.id",
            "foreignField": "id",
            "as": "teaches"
        }
    },
    {
        "$unwind": "$teaches"
    },
    {
        # Quarto inner Teaches -> Takes
        "$lookup": {
            "from": "takes",
            "localField": "id",
            "foreignField": "id",
            "as": "takes"
        }
    },
    {
        "$unwind": "$takes"
    },
    {
        # Quarto inner Teaches(course_id) -> course(course_id)
        "$lookup": {
            "from": "course",
            "localField": "teaches.course_id",
            "foreignField": "course_id",
            "as": "course"
        }
    },
    {
        "$unwind": "$course"
    },
    {
        "$match": {
            "$expr": {
                "$eq": ["$course.course_id", "$takes.course_id"]
            }
        }
    },
    {
        "$limit": 50
    },
    {
        "$project": {
            "_id": 0,
            "Nome do estudante": "$name",
            "Nome do Professor": "$instructor.name",
            "Nome do Cursp": "$course.title"
        }
    }
]

def query2():
    return [
    {
        # Primeiro inner Section -> Teaches
        "$lookup": {
            "from": "teaches",
            "localField": "course_id",
            "foreignField": "course_id",
            "as": "teaches"
        }
    },
    {
        "$unwind": "$teaches"
    },
    {
        # Segundo inner Teaches -> Instructor
        "$lookup": {
            "from": "instructor",
            "localField": "teaches.id",
            "foreignField": "id",
            "as": "instructor"
        }
    },
    {
        "$unwind": "$instructor"
    },
    {
        "$limit": 50
    },
    {
        "$project": {
            "_id": 0,
            "ID do professor": "$teaches.id",
            "Prédio": "$building",
            "Numero da sala": "$room_number"
        }
    }
]

def query3():
    return [
    {
        # Primeiro inner
        "$lookup": {
            "from": "student",
            "localField": "dept_name",
            "foreignField": "dept_name",
            "as": "students"
        }
    },
    {
        "$unwind": "$students"
    },
    {
        # segundo inner
        "$lookup": {
            "from": "instructor",
            "localField": "dept_name",
            "foreignField": "dept_name",
            "as": "instructors"
        }
    },
    {
        "$unwind": "$instructors"
    },
    {
        # group by
        "$group": {
            "_id": "$dept_name",
            "budget": {"$first": "$budget"},
            "student_count": {"$sum": 1},
            "avg_salary": {"$avg": "$instructors.salary"}
        }
    },
    {
        "$limit": 50
    },
    {
        "$project": {
            "_id": 0,
            "Nome do Departamento": "$_id",
            "Budget": "$budget",
            "N° estudantes": "$student_count",
            "Salário Médio": {"$round": ["$avg_salary", 2]}
        }
    }
]

print_mapper = {
    '1': '''\n
QUERY:
SELECT s.name, i.name, c.title FROM student s 
INNER JOIN advisor adv ON adv.s_id = s.id
INNER JOIN instructor i ON adv.i_id = i.id
INNER JOIN teaches te ON i.id= te.id
INNER JOIN takes ta ON s.id = ta.id
INNER JOIN course c ON c.course_id = te.course_id
WHERE ta.course_id = te.course_id;
''',
    '2': '''\n
QUERY:
SELECT t.ID, s.building, s.room_number FROM section s
INNER JOIN teaches t on s.course_id = t.course_id
INNER JOIN instructor i on i.id = t.id
''',
    '3': '''\n
QUERY:
SELECT d.dept_name, d.budget, COUNT(s.id), AVG(i.salary) FROM department as d
INNER JOIN student s on d.dept_name = s.dept_name 
INNER JOIN instructor i on d.dept_name = i.dept_name 
GROUP BY d.dept_name 
'''
}

def main():
    new_connection = Connection()
    db = new_connection.connect_to_mongo()
    print('''\n
################################################ QUERY SEARCHER\n...
''')
    number = input('Digite o numero da query entre 1 e 3: ')
    if number not in print_mapper.keys():
        print("Numero inválido")
        return
    
    pipeline = result = []
    if number == '1':
        pipeline = query1()
        result = db.student.aggregate(pipeline)
    if number == '2':
        pipeline = query2()
        result = db.section.aggregate(pipeline)
    if number == '3':
        pipeline = query3()
        result = db.departament.aggregate(pipeline)   

    print(print_mapper.get(number))
    for data in result:
        print(data)

    print("\nTodas as queries estão com LIMIT = 50")
    new_connection.close_connection()
    return


if __name__ == "__main__":
    main()
