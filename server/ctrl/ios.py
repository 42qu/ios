#coding:utf-8
import _env
#from utils.type.ttypes import 
#from server.model.ios import t
import logging

class Handler(object):
    def login(self,auth):
        pass

    def userInfo_get(self, accessToken, id):
        pass

    def userInfo_set(self, accessToken, userInfo):
        pass

    def eventInfo_get(self, accessToken, id):
        pass
    
    def eventInfo_set(self, accessToken, eventInfo):
        pass

    def eventPublish(self, accessToken):
        pass

    def eventApply(self, accessToken, id):
        pass

if __name__ == '__main__':
    pass

