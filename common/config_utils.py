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
    def LOG_PATH(self):
        value = self.read_ini('path', 'LOG_PATH')
        return value

    @property
    def CASE_DATA_PATH(self):
        value = self.read_ini('path', 'CASE_DATA_PATH')
        return value

    @property
    def REPORT_PATH(self):
        value = self.read_ini('path', 'REPORT_PATH')
        return value


    @property
    def LOG_LEVEL(self):
        value = int(self.read_ini('log', 'LOG_LEVEL'))
        return value

config=ConfigUtils()


if __name__=='__main__':
    current_path = os.path.dirname(__file__)
    cfgpath = os.path.join(current_path, "../conf/local_config.ini")
    config_u=ConfigUtils()
    print(config_u.hosts)
    print(config_u.LOG_LEVEL)
    print(config_u.REPORT_PATH)
    print(config_u.LOG_PATH)
    print(config_u.CASE_DATA_PATH)




