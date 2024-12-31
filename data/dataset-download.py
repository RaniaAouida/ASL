import kagglehub

# Download latest version of the processed WLASL dataset
path = kagglehub.dataset_download("risangbaskoro/wlasl-processed")

print("Path to dataset files:", path)
