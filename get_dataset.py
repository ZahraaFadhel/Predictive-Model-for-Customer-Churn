import kagglehub

# Download latest version of the dataset
path = kagglehub.dataset_download("blastchar/telco-customer-churn", path="data/")

print("Path to dataset files:", path)