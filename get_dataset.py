import kagglehub
import shutil
import os

# Download dataset
path = kagglehub.dataset_download("blastchar/telco-customer-churn")
print("Downloaded to:", path)

# Copy to project directory (current one)
current_dir = os.getcwd()
for file in os.listdir(path):
    src = os.path.join(path, file)
    if os.path.isfile(src):
        shutil.copy2(src, current_dir)
        print(f"Copied: {file}")

print(f"\nDataset files are now in: {current_dir}")