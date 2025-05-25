from pathlib import Path

class DirectoryManager:
    def __init__(self, base_path: str = "data/raw_storage"):
        self.base_path = Path(base_path)

    def get_data_path(self, source: str, data_name: str, filename: str = None) -> Path:
        """
        Ensures directories exist and returns the full path to save the file.

        - source: the source folder name
        - data_name: dataset folder inside source
        - filename: optional filename inside data_name folder, e.g., 'dataName.parquet'
        """
        source_dir = self.base_path / source
        data_dir = source_dir / data_name

        # Create folders if they don't exist
        data_dir.mkdir(parents=True, exist_ok=True)

        if filename:
            return data_dir / filename
        else:
            return data_dir

    def path_exists(self, path: Path) -> bool:
        return path.exists()