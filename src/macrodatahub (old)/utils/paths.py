from pathlib import Path

# Get the root path dynamically
PROJECT_ROOT = Path(__file__).resolve().parents[2]  # Adjust depending on file depth
DATA_PATH = PROJECT_ROOT / "data"
RAW_STORAGE_PATH = DATA_PATH / "raw_storage"