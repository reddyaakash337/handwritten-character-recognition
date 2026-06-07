import os

project_path = "/Users/aakashreddy/Desktop/handwritten_character_project"

# Important file extensions
important_extensions = {
    ".py", ".ipynb", ".csv", ".txt", ".md",
    ".json", ".yaml", ".yml",
    ".keras", ".h5", ".pkl", ".joblib",
    ".png", ".jpg", ".jpeg",
    ".pdf", ".docx"
}

# Folders to ignore
ignore_folders = {
    "venv", ".git", "__pycache__",
    ".ipynb_checkpoints", "node_modules"
}

print("Important Project Files:\n")

for root, dirs, files in os.walk(project_path):
    # Skip unwanted folders
    dirs[:] = [d for d in dirs if d not in ignore_folders]

    important_files = []

    for file in files:
        ext = os.path.splitext(file)[1].lower()

        if ext in important_extensions:
            important_files.append(file)

    if important_files:
        relative_folder = os.path.relpath(root, project_path)
        print(f"\n📁 {relative_folder}")

        for file in important_files:
            print(f"   ├── {file}")