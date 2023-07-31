from dotenv import load_dotenv
import os
from pymongo import MongoClient
from datetime import datetime
from datetime import timedelta
import streamlit as st

load_dotenv() 
mongo_uri = os.getenv("MONGO_URI")

db_name = os.getenv("DB_NAME")
db_collection_name = os.getenv("COLLECTION_NAME")

#connect to the MongoDB Atlas cluster
client = MongoClient(mongo_uri)

#access the db
db = client[db_name]
collection = db[db_collection_name]

add_new_questions = False

def add_to_db(add_new_questions):
    if add_new_questions:
        question_file = open("questions_to_add.txt", "r") 
        questions = [line.strip() for line in question_file]
        
        for question in questions:
            document = {
                "text": question,
                "next_review_time": datetime.utcnow(),
                "difficulty": None,
                "interval_days": 1,
            }
            collection.insert_one(document)      

def delete_db():
    collection.delete_many({})
    
def get_next_question_document():
    current_time = datetime.utcnow()
    
    cursor = collection.find({"next_review_time": {"$lte": current_time}}).sort("next_review_time", 1).limit(1)
    # Try to get the next document from the cursor.
    try:
        question = next(cursor)
    except StopIteration:
        # If there's no document, handle it appropriately (e.g., return None).
        return None
    return question

def update_next_review_time_based_on_difficulty(question_id, difficulty):
    #get current time
    current_time = datetime.utcnow()
    
    #get the entire question document
    question = collection.find_one({"_id": question_id})

    if difficulty == "easy":
        next_review_time = timedelta(days=question["interval_days"]*2) 
        # update interval_days for the next review
        question["interval_days"] *= 2
    elif difficulty == "medium":
        next_review_time = timedelta(minutes=10)
        question["interval_days"] = 1
    elif difficulty == "hard":
        next_review_time = timedelta(minutes=1)
        question["interval_days"] = 1
    
    # Set the fields to be updated
    update_fields = {
        "next_review_time": current_time + next_review_time,
        "difficulty": difficulty,
        "interval_days": question["interval_days"]
    }
    
    collection.update_one(
        {"_id": question_id},
        {
            "$set": update_fields
        }
    )
    

        
    
    
    
             

             
             
         
         
            
