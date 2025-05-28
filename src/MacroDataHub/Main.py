from src.MacroDataHub.utils.config_manager import ConfigManager

class Main:
    def __init__(self):
        self.ConfigMan = ConfigManager()

        self.data_dir     = self.ConfigMan.data_dir
        self.config_dir   = self.ConfigMan.config_dir
        self.project_home = self.ConfigMan.project_home

