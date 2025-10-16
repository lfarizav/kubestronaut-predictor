docker compose down
docker build -t lfarizav/kubestronaut_fastapi
cd streamlit_app
docker build -t lfarizav/kubestronaut_streamlit
cd ..
docker compose up
