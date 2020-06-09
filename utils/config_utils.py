import  os
import configparser

current_path = os.path.dirname(__file__)
cfgpath = os.path.join(current_path, "../conf/local_config.ini")
print(cfgpath)


class ConfigUtils:
    def __init__(self,config_path=cfgpath):
        self.__conf=configparser.ConfigParser()
        self.__conf.read(config_path, encoding="utf-8")

    def read_ini(self,sec,option):
        value=self.__conf.get(sec,option)
        return value

    @property
    def hosts(self):
        value=self.read_ini('default','hosts')
        return value

    @property
    def log_path(self):
        value=self.read_ini('default','log_path')
        return value

    @property
    def log_level(self):
        value=self.read_ini('default','log_level')
        return value


config=ConfigUtils()


if __name__=='__main__':
    current_path = os.path.dirname(__file__)
    cfgpath = os.path.join(current_path, "../conf/local_config.ini")
    config_u=ConfigUtils()
    print(config_u.log_level)


