#coding:utf-8
import _env

from decorator import decorator

from model.app.oauth2 import user_id_by_access_token

from utils.type.ttypes import User, UserGender, UserBasic, UserExt

from ctrl.user import login_by_mail, user_get

import logging

def verify(func, *args, **argkw):
    def new(self, token, *args,**argkw):
        if len(args)<1:
            return func()
        if user_id_by_access_token(token):
            return func(self, *args,**argkw)
        else:
            return Exception(ecode.PERMISSION_DENIED)
    return new

class Handler(object):
    login_by_mail = login_by_mail
    
    def logout(self, acess_token):
        pass

    user_get = decorator(verify, user_get)

    def user_info_get(self, access_token, uid, ext_only=True):
        b = UserBasic()

    def user_info_set(self, access_token, user_info):
        return u.user_info_set(access_token, user_info)

    def task_get(self, access_token, id):
        pass
    
    def task_new(self, access_token, task):
        pass

    def task_apply(self, access_token, task_id):
        pass

    def task_reject(self, access_token, user_id):
        pass

    def task_accept(self, access_token, user_id):
        pass

if __name__ == '__main__':
    from utils.type.ttypes import AuthRequest
    r = AuthRequest()
    r.client_id = 178
    r.client_secret = '7mVpcYfpSwOowDzOGekYdA'
    h = Handler()
    #ret = h.login_by_mail(r, 'fy0@qq.com','794613852')
    print h.user_get(168)
    #print ret

