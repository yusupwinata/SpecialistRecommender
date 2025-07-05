# SpecialistRecommender
 This is a simple FastAPI-based API that uses Google's Gemini language model (via LangChain) to recommend the most relevant specialist department for a patient based on gender, age, and symptoms.

## 🚀 Features
- Uses Gemini 2.0 Flash model via LangChain
- Accepts POST requests with patient data
- Returns only the recommended hospital department

## 🔑 Prerequisite
You must have a Google API key, then add your Google API key to the `.env` file. Example:
```text
GOOGLE_API_KEY=your_google_api_key_here
```

## 📁 Project Structure
```text
SpecialistRecommender/
├── main.py                  # FastAPI app with /recommend endpoint
├── run_recommendation.py    # Python script to test API
├── requirements.txt         # Required packages
├── .env                     # Contains your GOOGLE_API_KEY (empty)
└── README.md                # This tutorial
```

---

## 📦 A. Setup Instructions
Open a terminal and follow these steps:
### 1. Clone the repository
```bash
git clone https://github.com/yusupwinata/SpecialistRecommender.git
cd SpecialistRecommender
```

### 2. Create and activate virtual environment
In this tutorial I use **conda** to create a virtual environment named `specialist_env`.
```bash
conda create -n specialist_env python=3.11 -y
conda activate specialist_env
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🏃‍♂️ B. Run the API and Make Request Instructions
Open a new terminal in SpecialistRecommender folder and follow these steps:
### 1. Running the API
```bash
fastapi dev main.py
```
The API will be available at:
http://127.0.0.1:8000

### 2. Making Requests
You can test the /recommend endpoint in two different ways:

#### Option 1: Using curl
Make sure the API is running, then execute this command in your new terminal:
```bash
curl -X POST "http://127.0.0.1:8000/recommend" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"gender\": \"female\", \"age\": 62, \"symptoms\": [\"pusing\", \"mual\", \"sulit berjalan\"]}"
```
**Note**: You can modify patient's info (gender, age, and symptoms) in the command.

#### Option 2: Using run_recommendation.py
Make sure the API is running, then execute `run_recommendation.py` your new terminal:
```base
python run_recommendation.py
```
**Note**: You can modify patient's info (gender, age, and symptoms) in the code.

---

**Example Request Format:**
```json
{
  "gender": "female",
  "age": 62,
  "symptoms": ["pusing", "mual", "sulit berjalan"]
}
```

**Example output:**
```json
{
  "recommended_department": "Neurology"
}
```
