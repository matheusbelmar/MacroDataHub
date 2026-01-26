import os
import json
from macrodatahub.domain.ports.storage_port import StoragePort

class LocalStorageAdapter(StoragePort):

    def enforce_path(self, path):
        os.makedirs(path, exist_ok=True)

    def save_raw(
            self, 
            data: dict,
            base_path: str,
            ext:  str) -> None:
        
        self.enforce_path(base_path)

        if ext == 'json':
            path = base_path + r".json"
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        

    def load_raw(self) -> dict:
        raise NotImplementedError("load_raw() is not implemented yet.")
