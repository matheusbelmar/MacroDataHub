import yaml
import os
from pathlib import Path

def load_config():

    with open(r"./config/setting.yaml", "r") as f:
        return yaml.safe_load(f)

    base_dir = Path(config_file["Base_dir"])
    Configs={"base_dir": base_dir}


    Storage = config_file["Storage"]
    if Storage["use_local"]:
        local_storage={i: os.path.join(base_dir, i) for i in 
                        [
                        "raw_storage",
                        "reports",
                        "datasets"
                        ]
                    }
        Configs.update({"local_storage": local_storage})

    return Configs