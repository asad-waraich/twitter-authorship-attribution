import nbformat
from pathlib import Path

# Path to your notebook
nb_path = Path("notebooks/02_model_training.ipynb")

# Load notebook
nb = nbformat.read(nb_path, as_version=4)

# Ensure metadata.widgets exists
widgets = nb.metadata.get("widgets", {})

# Add missing 'state' key if needed
if "state" not in widgets:
    widgets["state"] = {}

# Remove broken metadata keys if any
for cell in nb.cells:
    if "metadata" in cell and "widgets" in cell["metadata"]:
        w = cell["metadata"]["widgets"]
        if not isinstance(w, dict):
            cell["metadata"]["widgets"] = {}
        if "state" not in cell["metadata"]["widgets"]:
            cell["metadata"]["widgets"]["state"] = {}

# Save back the notebook
nb.metadata["widgets"] = widgets
nbformat.write(nb, nb_path)
print(f"✅ Fixed metadata for: {nb_path}")