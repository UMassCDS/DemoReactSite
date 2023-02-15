from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
import os
from pymongo import MongoClient

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)


MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI, 27017)
db = client["roost_db"]
img_files = db["img_files"] # Create collection for image files
bounding_boxes = db["bounding_boxes"] # Create collection for bounding boxes


@app.get("/")
async def root():
    return {"detail": "Roost Backend is Running!"}

@app.get("/test_db_entry")
def get_test_db_entry():
    file_name: str = "testfile.png"
    test_file_name = img_files.find_one({"file_name": file_name}, {"_id": 0})
    return test_file_name

@app.get("/add_db_entry")
def add_test_db_entry():
    file_name: str = "testfile.png"
    img_files.insert_one({"file_name": file_name, "file_metadata": "foo"})
    return {"detail": "Success! Test Entry Created!"}