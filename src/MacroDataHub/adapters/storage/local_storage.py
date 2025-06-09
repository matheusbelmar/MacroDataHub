import os
import json
from core.ports.storage_port import StoragePort

class LocalStorageAdapter(StoragePort):
    def __init__(self, base_path: str):
        os.makedirs(base_path, exist_ok=True)
        self.base_path = base_path

    def save_raw(self, series_id: str, data: dict) -> None:
        path = os.path.join(self.base_path, f"{series_id}.json")
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
