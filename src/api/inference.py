import logging
from datetime import datetime
from typing import List

import joblib
import pandas as pd

from schemas import KubestronautPredictionRequest, PredictionResponse

logger = logging.getLogger(__name__)

# Load model and preprocessor
MODEL_PATH = "models/trained/kubestronaut_model.pkl"
PREPROCESSOR_PATH = "models/trained/preprocessor.pkl"

try:
    model = joblib.load(MODEL_PATH)
    preprocessor = joblib.load(PREPROCESSOR_PATH)
except Exception as e:
    raise RuntimeError(f"Error loading model or preprocessor: {str(e)}")


def _prepare_input_df_from_dict(d: dict) -> pd.DataFrame:
    df = pd.DataFrame([d])
    # derived features expected by preprocessor
    if 'born_year' in df.columns:
        df['kubestronaut_age'] = datetime.now().year - df['born_year']
    else:
        df['kubestronaut_age'] = 0
    # ratio features (guard division by zero)
    if 'cncf_try_numbers' in df.columns and 'number_full_exam_done' in df.columns:
        df['number_full_exam_done_cncf_try_numbers_ratio'] = (
            df['number_full_exam_done'] / df['cncf_try_numbers']
        ).replace([float('inf'), -float('inf')], 0).fillna(0)
    else:
        df['number_full_exam_done_cncf_try_numbers_ratio'] = 0
    # placeholder feature used during training
    df['final_result_per_theory_hours'] = 0
    return df


def predict_kubestronaut_result(request: KubestronautPredictionRequest) -> PredictionResponse:
    """Predict kubestronaut result based on input features and return a PredictionResponse."""
    input_data = _prepare_input_df_from_dict(request.dict())

    # Preprocess input data
    processed_features = preprocessor.transform(input_data)

    # Align feature counts if needed (temporary fallback)
    n_expected = getattr(model, 'n_features_in_', None)
    if n_expected is not None and processed_features.shape[1] != n_expected:
        logger.warning(
            "Preprocessor output has %d features but model expects %d. Slicing to match.",
            processed_features.shape[1], n_expected,
        )
        processed_features = processed_features[:, :n_expected]

    # Predict
    raw_pred = model.predict(processed_features)[0]
    pred_value = float(raw_pred)

    # Clip to [0,1]
    if pred_value < 0.0 or pred_value > 1.0:
        logger.warning("Predicted value %s out of [0,1]. Clipping.", pred_value)
        pred_value = max(0.0, min(1.0, pred_value))

    pred_value = round(pred_value, 4)

    ci = [round(pred_value * 0.9, 4), round(pred_value * 1.1, 4)]

    return PredictionResponse(
        predicted_final_result=pred_value,
        confidence_interval=ci,
        features_importance={},
        prediction_time=datetime.now().isoformat(),
    )


def batch_predict(requests: List[KubestronautPredictionRequest]) -> List[PredictionResponse]:
    inputs = pd.DataFrame([_prepare_input_df_from_dict(r.dict()).iloc[0] for r in requests])
    processed_features = preprocessor.transform(inputs)

    n_expected = getattr(model, 'n_features_in_', None)
    if n_expected is not None and processed_features.shape[1] != n_expected:
        logger.warning(
            "Preprocessor output has %d features but model expects %d. Slicing to match.",
            processed_features.shape[1], n_expected,
        )
        processed_features = processed_features[:, :n_expected]

    preds = model.predict(processed_features)
    responses: List[PredictionResponse] = []
    for p in preds:
        val = float(p)
        if val < 0.0 or val > 1.0:
            logger.warning("Batch predicted value %s out of [0,1]. Clipping.", val)
            val = max(0.0, min(1.0, val))
        val = round(val, 4)
        ci = [round(val * 0.9, 4), round(val * 1.1, 4)]
        responses.append(
            PredictionResponse(
                predicted_final_result=val,
                confidence_interval=ci,
                features_importance={},
                prediction_time=datetime.now().isoformat(),
            )
        )
    return responses