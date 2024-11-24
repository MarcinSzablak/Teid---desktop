import configparser
import os

class Filter_Settings:
    config_file = "components/settings_dir/filter_settings.cfg"
    @staticmethod
    def write_filter(filter_option):
        config = configparser.ConfigParser()
        
        if not os.path.exists(Filter_Settings.config_file):
            with open(Filter_Settings.config_file, 'w') as file:
                pass
        
        config.read(Filter_Settings.config_file)
        
        if 'Filter' not in config.sections():
            config.add_section('Filter')
        
        config.set('Filter', 'filter_option', filter_option)
        
        with open(Filter_Settings.config_file, 'w') as configfile:
            config.write(configfile)
        
        return filter_option
    
    @staticmethod
    def get_filter():
        config = configparser.ConfigParser()
        config.read(Filter_Settings.config_file)
        
        if config.has_section('Filter') and config.has_option('Filter', 'filter_option'):
            return config.get('Filter', 'filter_option')
        else:
            return None