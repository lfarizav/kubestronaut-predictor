from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from inference import predict_kubestronaut_result, batch_predict
from schemas import KubestronautPredictionRequest, PredictionResponse

# Initialize FastAPI app with metadata
app = FastAPI(
    title="Kubestronaut results Prediction API",
    description=(
        "An API for predicting kubestronaut results based on various features. "
        "This application was created by Gourav Shah and modified my Luis Felipe Ariza Vesga (lfarizav@gmail.com)."
    ),
    version="1.0.0",
    contact={
        "name": "delaparlaalcluster",
        "url": "https://delaparlaalcluster.org",
        "email": "lfarizav@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health", response_model=dict)
async def health_check():
    return {"status": "healthy", "model_loaded": True}

# Prediction endpoint
@app.post("/predict", response_model=PredictionResponse)
async def predict(request: KubestronautPredictionRequest):
    return predict_kubestronaut_result(request)

# Batch prediction endpoint
@app.post("/batch-predict", response_model=list)
async def batch_predict_endpoint(requests: list[KubestronautPredictionRequest]):
    return batch_predict(requests)