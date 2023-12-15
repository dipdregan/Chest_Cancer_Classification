import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "mlProject"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    ##All the Components related to data and model pipeline
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/Data_pipeline/__init__.py",
    f"src/{project_name}/components/Data_pipeline/data_ingetion.py",
    f"src/{project_name}/components/Data_pipeline/data_validation.py",
    f"src/{project_name}/components/Data_pipeline/data_transformation.py",
    f"src/{project_name}/components/Model_pipeline/__init__.py",
    f"src/{project_name}/components/Model_pipeline/model_trainer.py",
    f"src/{project_name}/components/Model_pipeline/model_evaluation.py",
    #Utilities
    f"src/{project_name}/Utils/__init__.py",
    f"src/{project_name}/Utils/utils.py",
    #Entity
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/configuration_entity.py",
    f"src/{project_name}/entity/artifact_entity.py",
    #Pipelines
    f"src/{project_name}/Pipeline/__init__.py",
    f"src/{project_name}/Pipeline/stage_01_data_ingetion.py",
    f"src/{project_name}/Pipeline/stage_02_data_validation.py",
    f"src/{project_name}/Pipeline/stage_03_data_transformation.py",
    f"src/{project_name}/Pipeline/stage_04_model_trainer.py",
    f"src/{project_name}/Pipeline/stage_05_model_evaluation.py",
    #constants
    f"src/{project_name}/Constants/__init__.py",
    f"src/{project_name}/Constants/constants.py",
    
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"


]




for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")