import configparser
import os

class Search_Settings:
    config_file = os.path.join("components", "settings_dir", "search_settings.cfg")
    observers = []

    @staticmethod
    def write_filter(filter_option):
        """Writes the filter option to the config file and notifies observers."""
        config = configparser.ConfigParser()

        # Ensure the config file exists
        if not os.path.exists(Search_Settings.config_file):
            # If file doesn't exist, create it (this is done implicitly during writing)
            with open(Search_Settings.config_file, 'w') as file:
                pass

        # Read existing configuration
        config.read(Search_Settings.config_file)

        # Ensure 'Search' section exists
        if 'Search' not in config.sections():
            config.add_section('Search')

        # Set the Search option
        config.set('Search', 'search_option', filter_option)

        # Write the configuration back to the file
        with open(Search_Settings.config_file, 'w') as configfile:
            config.write(configfile)

        # Notify observers of the change
        Search_Settings.notify_observers(filter_option)

        return filter_option

    @staticmethod
    def get_filter():
        """Reads the filter option from the config file."""
        config = configparser.ConfigParser()
        config.read(Search_Settings.config_file)

        # Return the filter option if exists, else None
        if config.has_section('Search') and config.has_option('Search', 'search_option'):
            return config.get('Search', 'search_option')
        else:
            return None

    @staticmethod
    def add_observer(observer):
        """Adds an observer to the list."""
        Search_Settings.observers.append(observer)

    @staticmethod
    def remove_observer(observer):
        """Removes an observer from the list."""
        if observer in Search_Settings.observers:
            Search_Settings.observers.remove(observer)

    @staticmethod
    def notify_observers(new_filter,**args):
        """Notifies all observers of the filter change."""
        for observer in Search_Settings.observers:
            observer(new_filter)  # Call the observer with the new filter value
