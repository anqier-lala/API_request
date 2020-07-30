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
        value = self.read_ini('log', 'LOG_PATH')
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


    @property
    def smtp_server(self):
        smtp_server_value = self.read_ini('email', 'smtp_server')
        return smtp_server_value

    @property
    def smtp_sender(self):
        smtp_sender_value = self.read_ini('email', 'smtp_sender')
        return smtp_sender_value

    @property
    def smtp_password(self):
        smtp_password_value = self.read_ini('email', 'smtp_password')
        return smtp_password_value

    @property
    def smtp_receiver(self):
        smtp_receiver_value = self.read_ini('email', 'smtp_receiver')
        return smtp_receiver_value

    @property
    def smtp_cc(self):
        smtp_cc_value = self.read_ini('email', 'smtp_cc')
        return smtp_cc_value

    @property
    def smtp_subject(self):
        smtp_subject_value = self.read_ini('email', 'smtp_subject')
        return smtp_subject_value


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





