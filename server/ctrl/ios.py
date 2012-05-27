#coding:utf-8
import _env
#from utils.type.ttypes import 
#from server.model.ios import t
import server.model.ios as m
import logging

class Handler(object):
    def login(self,auth):
        return m.login(auth.user,auth.password,auth.clientKey,
                auth.clientSecret)

    def userInfo_get(self, accessToken, id):
        return m.userinfo_get(accessToken, id)

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

