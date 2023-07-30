from dotenv import load_dotenv
import os
from pymongo import MongoClient
from datetime import datetime
from datetime import timedelta

mongo_uri = os.getenv("MONGO_URI")

db_name = "studygptdb"
db_collection_name = "questions"

#connect to the MongoDB Atlas cluster
client = MongoClient(mongo_uri)

#access the db
db = client[db_name]
collection = db[db_collection_name]

def setup_db(collection):
    if collection.count_documents({}) == 0:
         question_file = open("all_questions.txt", "r") 
         questions = [line.strip() for line in question_file]
         
         for question in questions:
             document = {
                 "text": question,
                 "answer": None,
                 "next_review_time": datetime.utcnow(),
                 "difficulty": None,
                 "interval_days": 1,
             }
             collection.insert_one(document)
             
             
def get_next_question(): 
    question = collection.find().sort("next_review_time", 1).limit(1)
    return question
    
def update_next_review_time_based_on_difficulty(question_id,difficulty):
    #get current time
    current_time = datetime.utcnow()
    
    #get the entire question document
    question = collection.find_one({"id": question_id})

    if difficulty == "easy":
        next_review_time = timedelta(days=question["interval_days"]*2) 
    elif difficulty == "medium":
        next_review_time = timedelta(minutes=10)
    elif difficulty == "hard":
        next_review_time = timedelta(minutes=1)
    
    collection.update_one(
        {"_id": question_id},
        {
            "$set": {
                "next_review_time": current_time + next_review_time,
                "difficulty": difficulty,
                "interval_days": question["interval_days"]*2
            }
        }
    )
    
        
    
    
    
             

             
             
         
         
            
