import json
import pickle
import shutil
from pathlib import Path
import filecmp
BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"
ACTIVE_FILE = MODELS_DIR / "active_model.json"

def register_model(model_file, version):

    model_file = Path(model_file)
    metadata_file = model_file.with_name(f"{model_file.stem}_metadata.json")
    model_dir = MODELS_DIR / version

    if not model_file.is_file():
        raise FileNotFoundError(f"Model not found: {model_file}")

    if not metadata_file.is_file():
        raise FileNotFoundError(f"Metadata not found: {metadata_file}")

    if model_dir.exists():
        raise FileExistsError(f"Model {version} already exists")

    # Read metadata and add the version number
    with open(metadata_file, "r") as f:
        metadata = json.load(f)

    metadata["version"] = version

    # Create version folder
    model_dir.mkdir(parents=True)

    # Save model and metadata
    shutil.copy2(model_file, model_dir / "model.pkl")

    with open(model_dir / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)

    print(f"Registered model {version}")

def register_all_models():

    training_dir = BASE_DIR / "training"

    for model_file in training_dir.glob("*.pkl"):

        # Check whether this exact model is already registered
        registered = any(
            filecmp.cmp(model_file, saved_model, shallow=False)
            for saved_model in MODELS_DIR.glob("v*/model.pkl")
        )

        if registered:
            print(f"Skipping {model_file.name}: Already registered")
            continue

        # Find the next available version number
        versions = [
            int(folder.name[1:])
            for folder in MODELS_DIR.glob("v*")
            if folder.is_dir() and folder.name[1:].isdigit()
        ]

        version = f"v{max(versions, default=0) + 1}"

        register_model(model_file, version)

def activate_model(version):

    model_path = MODELS_DIR / version / "model.pkl"

    if not model_path.exists():
        raise FileNotFoundError(f"Model {version} does not exist")

    with open(ACTIVE_FILE, "w") as f:
        json.dump({"active_version": version}, f, indent=4)

    print(f"Active model changed to {version}")