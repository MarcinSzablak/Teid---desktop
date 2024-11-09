import configparser
import os

class Settings:
    
    config_file = "components/settings_dir/settings.cfg"
    
    @staticmethod
    def set_directory(directory):
        config = configparser.ConfigParser()
        
        if not os.path.exists(Settings.config_file):
            with open(Settings.config_file, 'w') as file:
                pass
        
        config.read(Settings.config_file)
        
        if 'Settings' not in config.sections():
            config.add_section('Settings')
        
        config.set('Settings', 'directory', directory)
        
        with open(Settings.config_file, 'w') as configfile:
            config.write(configfile)
        
        return directory

    @staticmethod
    def get_directory():
        config = configparser.ConfigParser()
        config.read(Settings.config_file)
        
        if config.has_section('Settings') and config.has_option('Settings', 'directory'):
            return config.get('Settings', 'directory')
        else:
            return None

    @staticmethod
    def check_directory():
        config = configparser.ConfigParser()
        config.read(Settings.config_file)
        
        if config.has_section('Settings') and config.has_option('Settings', 'directory'):
            directory = config.get('Settings', 'directory')
            if directory:
                return True
        return False
