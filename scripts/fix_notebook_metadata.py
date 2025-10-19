import nbformat

path = "notebooks/02_model_training.ipynb"  # adjust if needed
nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)

widgets = nb.metadata.get("widgets", {})
if "state" not in widgets:
    widgets["state"] = {}
    nb.metadata["widgets"] = widgets
    nbformat.write(nb, path)
    print(f"✅ Fixed missing 'state' key in {path}")
else:
    print("No fix needed — notebook metadata is already valid.")
