import yaml
from pathlib import Path

class ConfigManager:
    def __init__(self, config_path: str = "config/config.yaml"):
        
        self.config_file = Path(config_path)
        self.Configs = self._load_config()

        self.config_dir = self.Configs["paths"]["config_dir"]
        self.data_dir   = self.Configs["paths"]["data_dir"]
        self.project_home = self.Configs.get("paths", {}).get("home_dir")
        

    def _load_config(self) -> dict:
        with open(self.config_file, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def _dump_config(self) -> None:
        with open(self.config_file, "w", encoding="utf-8") as f:
            yaml.dump(config, f, default_flow_style=False, allow_unicode=True)

    def usr_interactive(self, cml: str) -> str:
        
        user_input = input(cml)
        if user_input.lower() == 'y':
            response = 'y' 
        elif user_input.lower() == 'n':
            response = 'n'
        else:   
            print('"s" or "n" answers only')
            response = self.usr_interactive(cml)
        return response

    def base_dir_eval(self):

        response1=self.usr_interactive("Wish to make current directory into base directory (y/n) ?")

        if response1 =='y':
            self.project_home=Path.cwd()
                    
        else:
            while True:
                user_input = input("Input desired home directory path: ").strip()
                pj_dir = Path(user_input).expanduser().resolve()

                if pj_dir.exists():
                    break
                else:
                    create = input(f"Directory '{pj_dir}' does not exist. Create it? (y/n): ").strip().lower()
                    if create == 'y':
                        try:
                            pj_dir.mkdir(parents=True, exist_ok=True)
                            print(f"Created directory: {pj_dir}")
                            break
                        except Exception as e:
                            print(f"Failed to create directory: {e}")
                    else:
                        print("Please enter a valid directory.")
        
            self.project_home=pj_dir
        
        self.Configs["paths"].update({"home_dir": pj_dir})
        self._dump_config(self.Configs)
        return 

    def run(self):
        print(self.project_home)

if __name__ == "__main__":
    config = ConfigManager()
    config.run()