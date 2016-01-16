# Andrew Erlichson
# MongoDB, Inc. 
# M101P - Copyright 2015, All Rights Reserved


import pymongo
import datetime
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")


def remove_student(hw_type):
    db = connection.students
    grades = db.grades

    try:
        result = grades.find({'type': hw_type}).sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])

        previous_id = None
        student_id = None
        deleted = 0

        for doc in result:
            student_id = doc['student_id']
            if student_id != previous_id:
                previous_id = student_id
                print "Removing", doc
                grades.remove({'_id': doc['_id']})
                deleted+=1
                print "num removed: ", deleted
    except Exception as e:
        print "Exception: ", type(e), e


remove_student('homework')
