<table style="border-collapse: collapse; border: none;">
  <tr style="border-collapse: collapse; border: none;">
    <td style="border-collapse: collapse; border: none;">
      <a href="http://www.openairinterface.org/">
         <img src="https://gitlab.eurecom.fr/uploads/-/system/user/avatar/716/avatar.png?width=800" alt="" border=3 height=50 width=50>
         </img>
      </a>
    </td>
    <td style="border-collapse: collapse; border: none; vertical-align: center;">
      <b><font size = "5">House Price Predictor</font></b>
    </td>
  </tr>
</table>

# Author
**Luis Felipe Ariza Vesga** 
emails: lfarizav@gmail.com, lfarizav@unal.edu.co
# 🏠 House Price Predictor – An MLOps Learning Project

Welcome to the **House Price Predictor** project! This is a real-world, end-to-end MLOps use case designed to help you master the art of building and operationalizing machine learning pipelines.

You'll start from raw data and move through data preprocessing, feature engineering, experimentation, model tracking with MLflow, and optionally using Jupyter for exploration – all while applying industry-grade tooling.
<<<<<<< HEAD


=======
This project is forked from https://github.com/mlopsbootcamp/hosue-price-predictor
>>>>>>> d83eca9805deb659a25922000744e701bd0738a4
---

## 📦 Project Structure

```
house-price-predictor/
├── configs/                # YAML-based configuration for models
├── data/                   # Raw and processed datasets
├── deployment/
│   └── mlflow/             # Docker Compose setup for MLflow
├── models/                 # Trained models and preprocessors
├── notebooks/              # Optional Jupyter notebooks for experimentation
├── src/
│   ├── data/               # Data cleaning and preprocessing scripts
│   ├── features/           # Feature engineering pipeline
│   ├── models/             # Model training and evaluation
├── requirements.txt        # Python dependencies
└── README.md               # You’re here!
```

---

## 🛠️ Setting up Learning/Development Environment

To begin, ensure the following tools are installed on your system:

- [Python 3.11.13](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [Visual Studio Code](https://code.visualstudio.com/) or your preferred editor
- [UV – Python package and environment manager](https://github.com/astral-sh/uv)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) **or** [Podman Desktop](https://podman-desktop.io/)

---

## 🚀 Preparing Your Environment

1. **Fork this repo** on GitHub.

2. **Clone your forked copy:**

   ```bash
   git clone https://github.com/lfarizav/hosue-price-predictor.git
   cd hosue-price-predictor
   ```

3. **Setup Python Virtual Environment using UV:**
   ```bash
   luis@lfarizav:~/hosue-price-predictor$ uv venv --python python3.11
   source .venv/bin/activate
   Using CPython 3.11.13
   Creating virtual environment at: .venv
   Activate with: source .venv/bin/activate
   (hosue-price-predictor) luis@lfarizav:~/hosue-price-predictor$ ls
   data  deployment  LICENSE  models  notebooks  README.md  requirements.txt  src  streamlit_app
   ```
4. **Install dependencies:**
   ```bash
   (hosue-price-predictor) luis@lfarizav:~/hosue-price-predictor$ uv pip install -r requirements.txt
   Resolved 94 packages in 719ms
   Prepared 94 packages in 11.47s
   Installed 94 packages in 39ms
    + alembic==1.16.5
    + anyio==4.11.0
    + asttokens==3.0.0
    + blinker==1.9.0
    + certifi==2025.10.5
    + charset-normalizer==3.4.3
    + click==8.3.0
    + cloudpickle==2.2.1
    + comm==0.2.3
    + contourpy==1.3.2
    + cycler==0.12.1
    + databricks-cli==0.18.0
    + debugpy==1.8.17
    + decorator==5.2.1
    + docker==6.1.3
    + entrypoints==0.4
    + executing==2.2.1
    + fastapi==0.95.2
    + flask==2.3.3
    + fonttools==4.60.1
    + gitdb==4.0.12
    + gitpython==3.1.45
    + greenlet==3.2.4
    + gunicorn==20.1.0
    + h11==0.16.0
    + idna==3.10
    + importlib-metadata==6.11.0
    + iniconfig==2.1.0
    + ipykernel==6.29.5
    + ipython==9.6.0
    + ipython-pygments-lexers==1.1.1
    + itsdangerous==2.2.0
    + jedi==0.19.2
    + jinja2==3.1.6
    + joblib==1.3.1
    + jupyter-client==8.6.3
    + jupyter-core==5.8.1
    + kiwisolver==1.4.9
    + mako==1.3.10
    + markdown==3.9
    + markupsafe==3.0.3
    + matplotlib==3.7.1
    + matplotlib-inline==0.1.7
    + mlflow==2.3.1
    + nest-asyncio==1.6.0
    + numpy==1.24.3
    + oauthlib==3.3.1
    + packaging==23.2
    + pandas==1.5.3
    + parso==0.8.5
    + pexpect==4.9.0
    + pillow==11.3.0
    + platformdirs==4.4.0
    + pluggy==1.6.0
    + prompt-toolkit==3.0.52
    + protobuf==4.25.8
    + psutil==7.1.0
    + ptyprocess==0.7.0
    + pure-eval==0.2.3
    + pyarrow==11.0.0
    + pydantic==1.10.24
    + pygments==2.19.2
    + pyjwt==2.10.1
    + pyparsing==3.2.5
    + pytest==7.3.1
    + python-dateutil==2.9.0.post0
    + pytz==2023.4
    + pyyaml==6.0
    + pyzmq==27.1.0
    + querystring-parser==1.2.4
    + requests==2.32.5
    + scikit-learn==1.2.2
    + scipy==1.15.3
    + seaborn==0.12.2
    + setuptools==65.5.0
    + six==1.17.0
    + smmap==5.0.2
    + sniffio==1.3.1
    + sqlalchemy==2.0.43
    + sqlparse==0.5.3
    + stack-data==0.6.3
    + starlette==0.27.0
    + tabulate==0.9.0
    + threadpoolctl==3.6.0
    + tornado==6.5.2
    + traitlets==5.14.3
    + typing-extensions==4.15.0
    + urllib3==2.5.0
    + uvicorn==0.22.0
    + wcwidth==0.2.14
    + websocket-client==1.8.0
    + werkzeug==3.1.3
    + xgboost==1.7.5
    + zipp==3.23.0
   ```
---

## 📊 Setup MLflow for Experiment Tracking

To track experiments and model runs:

```bash
cd deployment/mlflow
docker compose up -d
WARN[0000] /home/luis/hosue-price-predictor/deployment/mlflow/docker-compose.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 6/6
 ✔ mlflow Pulled                                                                                                                                                                                      19.3s 
   ✔ ccaf924377f9 Pull complete                                                                                                                                                                        3.6s 
   ✔ 5e584f8f28c3 Pull complete                                                                                                                                                                        3.7s 
   ✔ 954774345a61 Pull complete                                                                                                                                                                        4.1s 
   ✔ 7360b233c860 Pull complete                                                                                                                                                                        4.1s 
   ✔ 0e9ec008394e Pull complete                                                                                                                                                                       12.9s 
[+] Running 2/2
 ✔ Network mlflow_default            Created                                                                                                                                                           0.0s 
 ✔ Container mlflow-tracking-server  Started                                                                                                                                                           0.6s 
WARN[0000] /home/luis/hosue-price-predictor/deployment/mlflow/docker-compose.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
```
```bash
docker compose ps
WARN[0000] /home/luis/hosue-price-predictor/deployment/mlflow/docker-compose.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
NAME                     IMAGE                          COMMAND                  SERVICE   CREATED          STATUS          PORTS
mlflow-tracking-server   ghcr.io/mlflow/mlflow:latest   "mlflow server --hos…"   mlflow    32 seconds ago   Up 31 seconds   0.0.0.0:5555->5000/tcp, [::]:5555->5000/tcp

```

> 🐧 **Using Podman?** Use this instead:

```bash
podman compose -f mlflow-docker-compose.yml up -d
podman compose ps
```

Access the MLflow UI at [http://localhost:5555](http://localhost:5555)

---

## 📒 Using JupyterLab (Optional)

If you prefer an interactive experience, launch JupyterLab with:

```bash
   (hosue-price-predictor) luis@lfarizav:~/hosue-price-predictor$ uv pip install jupyterlab
   Resolved 93 packages in 289ms
   Prepared 50 packages in 945ms
   Installed 50 packages in 68ms
 + argon2-cffi==25.1.0
 + argon2-cffi-bindings==25.1.0
 + arrow==1.3.0
 + async-lru==2.0.5
 + attrs==25.4.0
 + babel==2.17.0
 + beautifulsoup4==4.14.2
 + bleach==6.2.0
 + cffi==2.0.0
 + defusedxml==0.7.1
 + fastjsonschema==2.21.2
 + fqdn==1.5.1
 + httpcore==1.0.9
 + httpx==0.28.1
 + isoduration==20.11.0
 + json5==0.12.1
 + jsonpointer==3.0.0
 + jsonschema==4.25.1
 + jsonschema-specifications==2025.9.1
 + jupyter-events==0.12.0
 + jupyter-lsp==2.3.0
 + jupyter-server==2.17.0
 + jupyter-server-terminals==0.5.3
 + jupyterlab==4.4.9
 + jupyterlab-pygments==0.3.0
 + jupyterlab-server==2.27.3
 + lark==1.3.0
 + mistune==3.1.4
 + nbclient==0.10.2
 + nbconvert==7.16.6
 + nbformat==5.10.4
 + notebook-shim==0.2.4
 + overrides==7.7.0
 + pandocfilters==1.5.1
 + prometheus-client==0.23.1
 + pycparser==2.23
 + python-json-logger==4.0.0
 + referencing==0.36.2
 + rfc3339-validator==0.1.4
 + rfc3986-validator==0.1.1
 + rfc3987-syntax==1.1.0
 + rpds-py==0.27.1
 + send2trash==1.8.3
 + soupsieve==2.8
 + terminado==0.18.1
 + tinycss2==1.4.0
 + types-python-dateutil==2.9.0.20250822
 + uri-template==1.3.0
 + webcolors==24.11.1
 + webencodings==0.5.1
```
```bash
(hosue-price-predictor) luis@lfarizav:~/hosue-price-predictor$ python -m jupyterlab
[I 2025-10-07 12:29:42.459 ServerApp] jupyter_lsp | extension was successfully linked.
[I 2025-10-07 12:29:42.462 ServerApp] jupyter_server_terminals | extension was successfully linked.
[I 2025-10-07 12:29:42.465 ServerApp] jupyterlab | extension was successfully linked.
[I 2025-10-07 12:29:42.648 ServerApp] notebook_shim | extension was successfully linked.
[I 2025-10-07 12:29:42.660 ServerApp] notebook_shim | extension was successfully loaded.
[I 2025-10-07 12:29:42.662 ServerApp] jupyter_lsp | extension was successfully loaded.
[I 2025-10-07 12:29:42.663 ServerApp] jupyter_server_terminals | extension was successfully loaded.
[I 2025-10-07 12:29:42.664 LabApp] JupyterLab extension loaded from /home/luis/hosue-price-predictor/.venv/lib/python3.11/site-packages/jupyterlab
[I 2025-10-07 12:29:42.664 LabApp] JupyterLab application directory is /home/luis/hosue-price-predictor/.venv/share/jupyter/lab
[I 2025-10-07 12:29:42.665 LabApp] Extension Manager is 'pypi'.
[I 2025-10-07 12:29:42.687 ServerApp] jupyterlab | extension was successfully loaded.
[I 2025-10-07 12:29:42.688 ServerApp] Serving notebooks from local directory: /home/luis/hosue-price-predictor
[I 2025-10-07 12:29:42.688 ServerApp] Jupyter Server 2.17.0 is running at:
[I 2025-10-07 12:29:42.688 ServerApp] http://localhost:8888/lab?token=481eca176a7f5873022843ccff369ea70cf9e5a2c54a29b7
[I 2025-10-07 12:29:42.688 ServerApp]     http://127.0.0.1:8888/lab?token=481eca176a7f5873022843ccff369ea70cf9e5a2c54a29b7
[I 2025-10-07 12:29:42.688 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
...
...
Shut down this Jupyter server (y/[n])? y
[C 2025-10-07 12:32:03.305 ServerApp] Shutdown confirmed
[I 2025-10-07 12:32:03.306 ServerApp] Shutting down 4 extensions
[I 2025-10-07 12:32:03.307 ServerApp] Shutting down 1 kernel
[I 2025-10-07 12:32:03.308 ServerApp] Kernel shutdown: 1bd3a2c7-e086-4f67-8704-4c6fc107aabb
```
---

## 🔁 Model Workflow

### 🧹 Step 1: Data Processing

Clean and preprocess the raw housing dataset:

```bash
python src/data/run_processing.py   --input data/raw/house_data.csv   --output data/processed/cleaned_house_data.csv
```

---

### 🧠 Step 2: Feature Engineering

Apply transformations and generate features:

```bash
python src/features/engineer.py   --input data/processed/cleaned_house_data.csv   --output data/processed/featured_house_data.csv   --preprocessor models/trained/preprocessor.pkl
```

---

### 📈 Step 3: Modeling & Experimentation

Train your model and log everything to MLflow:

```bash
python src/models/train_model.py   --config configs/model_config.yaml   --data data/processed/featured_house_data.csv   --models-dir models   --mlflow-tracking-uri http://localhost:5555
```

---


## Building FastAPI and Streamlit 

The code for both the apps are available in `src/api` and `streamlit_app` already. To build and launch these apps 

  * Add a  `Dockerfile` in the root of the source code for building FastAPI  
  * Add `streamlit_app/Dockerfile` to package and build the Streamlit app  
  * Add `docker-compose.yaml` in the root path to launch both these apps. be sure to provide `API_URL=http://fastapi:8000` in the streamlit app's environment. 


Once you have launched both the apps, you should be able to access streamlit web ui and make predictions. 

You could also test predictions with FastAPI directly using 

```
curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "sqft": 1500,
  "bedrooms": 3,
  "bathrooms": 2,
  "location": "suburban",
  "year_built": 2000,
  "condition": fair
}'

```

Be sure to replace `http://localhost:8000/predict` with actual endpoint based on where its running. 


## 🧠 Learn More About MLOps

This project is part of the [**MLOps Bootcamp**](https://schoolofdevops.com) at School of DevOps, where you'll learn how to:

- Build and track ML pipelines
- Containerize and deploy models
- Automate training workflows using GitHub Actions or Argo Workflows
- Apply DevOps principles to Machine Learning systems

🔗 [Get Started with MLOps →](https://schoolofdevops.com)

---

## 🤝 Contributing

We welcome contributions, issues, and suggestions to make this project even better. Feel free to fork, explore, and raise PRs!

---

Happy Learning!  
— Team **School of DevOps**
