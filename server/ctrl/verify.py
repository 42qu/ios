
# coding:utf-8

import _env

from model.app.oauth2 import user_id_by_access_token

def verify(func):
    def new(self, token, *args,**argkw):
        if len(args)<1:
            return func()
        if user_id_by_access_token(token):
            return func(self, token, *args, **argkw)
        else:
            return
            #return Exception(ecode.PERMISSION_DENIED)
    return new

def verify_get_user(func):
    def new(self, token, *args,**argkw):
        if len(args)<1:
            return func()
        uid = user_id_by_access_token(token)
        if uid:
            return func(self, token, uid=uid, *args, **argkw)
        else:
            return
            #return Exception(ecode.PERMISSION_DENIED)
    return new

