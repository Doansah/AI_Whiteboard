
import shutil
from fastapi import FastAPI, UploadFile, File
import os


app = FastAPI()

newFile = File()

@app.get("/")
def root():
    return {"message": "Hello World REALLY WOW!"}


@app.get("/analyze/")
def analyze():
    #analsis logic and stuffff!!!!!
    return {"recommendation": "Recommendation: "}

UPLOAD_FOLDER = './uploads'

@app.post("/photos/")
async def upload_photo(file: UploadFile = File(...)):

    # uploading a file nonsense
    try:
        file_location = os.path.join(UPLOAD_FOLDER, file.filename)

        #Save uploaded
        with open(file_location, 'rb') as buffer:
            shutil.copyfileobj(buffer, file)

        return {"filename": file.filename,
                "message" :" Uploaded Successfully!"}



