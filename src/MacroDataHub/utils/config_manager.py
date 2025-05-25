import yaml
from pathlib import Path

class ConfigLoader:
    def __init__(self, config_path: str = "/home/mbelmar/Documentos/Programaçao - Projetos/Projetos/MacroDataHub/config/config.yaml"):
        self.config_file = Path(config_path)
        self.Configs = self._load_config()
        self.project_home = Path(__file__).resolve().parents[3]


        # Correct usage
        self.Config_dir = self.Configs["paths"]["config_dir"]
        self.Data_dir   = self.Configs["paths"]["data_dir"]

    def _load_config(self) -> dict:
        with open(self.config_file, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def run(self):
        print(self.project_home)

if __name__ == "__main__":
    config = ConfigLoader()
    config.run()