import os
from typing import List
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

# LLM initialization
load_dotenv() # load API key
llm = GoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Prompting
prompt_template = PromptTemplate(
    input_variables=["gender", "age", "symptoms"],
    template="""
You are a medical assistant. Based on the following patient information, suggest the most relevant hospital department.

Gender: {gender}
Age: {age}
Symptoms: {symptoms}

Only output the department name, such as "Neurology", "Cardiology", "Orthopedics", etc, without additional text.
"""
)

# Define the structure of request and response data
class Patient(BaseModel):
    gender: str
    age: int
    symptoms: List[str]

class DepartmentRecommendation(BaseModel):
    recommended_department: str

# Defines POST endpoint
@app.post("/recommend", response_model=DepartmentRecommendation)
async def recommend_department(patient: Patient):
    try:
        prompt = prompt_template.format(
            gender=patient.gender,
            age=patient.age,
            symptoms=patient.symptoms
        )
        response = llm.invoke(prompt).strip()
        
        return {"recommended_department": response}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) # Internal Server Error