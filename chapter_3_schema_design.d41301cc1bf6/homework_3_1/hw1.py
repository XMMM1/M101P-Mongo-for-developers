import pymongo
import datetime
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")


def RemoveLowest(score1):
    UnScore = score1
    homework_scores = [score for score in score1 if score[u"type"] == u"homework"]
    lowScore = min(score[u'score'] for score in homework_scores)

    newScore = [score for score in score1 if
                score[u'type'] != 'homework' or (score[u"type"] == u"homework" and score[u"score"] != lowScore)]

    return newScore


# add a review date to a single record using update_one
def hw1():
    # get a handle to the school database
    db = connection.school
    scores = db.students

    try:
        # get the doc
        data = scores.find({'scores.type': 'homework'})

        for score in data:
            id = score['_id']
            score1 = score['scores']
            newScore = RemoveLowest(score1)
            # print newScore
            # print newScore
            scores.update({'_id': id}, {'$set': {'scores': newScore}})

    except Exception as e:
        raise


def getLowest(scores):
    if (scores[0] < scores[1]):
        return scores[0]
    else:
        return scores[1]


hw1()
