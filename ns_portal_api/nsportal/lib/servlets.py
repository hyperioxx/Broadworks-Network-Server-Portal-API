import requests


class Base(object):
    def __init__(self):
        self.servlet = None
        self.host = "localhost"
        self.url = "/servlet/{}"

    def send_request(self,servlet):
        response = requests.get()


class GetWebServerPortal(Base):
    def __init__(self):
        pass

class GetHostingNEInfo(Base):
    def __init__(self):
        pass


class AuthorizeToken(Base):
    def __init__(self):
        pass


class GetHostNodeAddresses(Base):
    def __init__(self):
        pass


class GetServingAS(Base):
    def __init__(self):
        pass

class GetHostsForEnterprise(Base):
    def __init__(self):
        pass

class GetAllHostingNeNodeAddresses(Base):
    def __init__(self):
        pass


class GetDeviceFileServingAS(Base):
    def __init__(self):
        pass