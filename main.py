import os
os.system("python3 src/data_ingestion.py")
print('Data Ingestion Run')

os.system("python3 src/data_preprocessing.py")
print('Data preprocessing run')

os.system("python3 src/feature_engineering.py")
print('feature_engineering run')

os.system("python3 src/model_building.py")
print('model building is run')

os.system("python3 src/model_evaluation.py")
print("model evaluation run")