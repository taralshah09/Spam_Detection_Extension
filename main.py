from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import time
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Spam Detection API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model at startup
try:
    with open('spam_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

class MessageRequest(BaseModel):
    message: str

class MessageResponse(BaseModel):
    is_spam: bool
    confidence: float
    category: str
    processing_time_ms: float

@app.get("/")
async def root():
    return {"message": "Spam Detection API is running"}

@app.post("/classify", response_model=MessageResponse)
async def classify_message(request: MessageRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    start_time = time.time()
    
    try:
        # Get prediction
        prediction = model.predict([request.message])[0]
        probabilities = model.predict_proba([request.message])[0]
        confidence = float(probabilities[prediction])
        
        processing_time = (time.time() - start_time) * 1000  # Convert to ms
        
        return MessageResponse(
            is_spam=bool(prediction),
            confidence=confidence,
            category="Spam" if prediction else "Ham",
            processing_time_ms=round(processing_time, 2)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }