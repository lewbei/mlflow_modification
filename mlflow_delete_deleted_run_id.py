import os
import shutil
import yaml

# Set this to True to delete folders, False just to show what would be deleted
delete_folders = True

experiment_id = "885930349420756297"
artifact_base_path = f"C:/Users/lewka/mlruns/{experiment_id}"

deleted_runs = []
active_runs = []

# Iterate through each run directory and check meta.yaml
for run_id in os.listdir(artifact_base_path):
    run_path = os.path.join(artifact_base_path, run_id)
    meta_yaml_path = os.path.join(run_path, "meta.yaml")

    if os.path.isdir(run_path) and os.path.exists(meta_yaml_path):
        with open(meta_yaml_path, "r") as file:
            meta_content = yaml.safe_load(file)

        if meta_content.get("lifecycle_stage") == "deleted":
            deleted_runs.append(run_path)
        elif meta_content.get("lifecycle_stage") == "active":
            active_runs.append(run_path)

# Perform deletion or just list folders
if delete_folders:
    print("Deleting the following folders:")
    for path in deleted_runs:
        print(f"Deleting: {path}")
        shutil.rmtree(path)
else:
    print("Folders that would be deleted (simulation):")
    for path in deleted_runs:
        print(path)

print(f"\nTotal folders marked as deleted: {len(deleted_runs)}")

print("\nActive folders:")
for path in active_runs:
    print(path)

print(f"\nTotal active folders: {len(active_runs)}")
