FROM python:3.11-slim

LABEL maintainer="Luis Felipe Ariza Vesga <lfarizav@gmail.com> <lfarizav@unal.edu.co>"

WORKDIR /app

COPY src/api/ .

RUN pip install -r requirements.txt

COPY models/trained/*.pkl models/trained/

EXPOSE 8000 

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
