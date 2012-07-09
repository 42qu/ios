#coding:utf-8
import _env
from utils.type.ttypes import AuthRequest, AuthResponse, UserInfo
from utils.exception.ttypes import Exception, ExceptionCode as ecode

from time import time

token_lst = ['access_token']

# 虚拟认证
def oauth_secret_verify(client_id, client_secret):
    if client_id == 'client_id' and client_secret == 'client_secret':
        return true

def access_token_verify(func):
    def new(*args,**argkw):
        if len(args)<1:
            return func()
        #if oauth_access_token_verify(args[0]):
        #    return func(*args,**argkw)
        if args[0] in token_lst:
            return func(*args,**argkw)
        else:
            return Exception(ecode.PERMISSION_DENIED)
    return new

def login_by_email(auth, mail, pw):
    if oauth_secret_verify(auth.client_id, auth.client_secret):
        if mail=="test@42qu.com" and pw == "123455":
            return AuthResponse(
                '查内姆',
                'access_token',
                'refresh_token',
                87063
            )
        else:
            return Exception(ecode.USER_VERIFY_FAILED)
    else:
        return Exception(ecode.PERMISSION_DENIED)

login_by_email()

@access_token_verify
def logout(access_token):
    pass

@access_token_verify
def user_info_get(access_token, uid):
    UserInfo(uid, 
    return UserInfo(id, name, intro, pic, link, phone, mail)

def user_info_set(access_token, user_info):
    pass

if __name__ == '__main__':
    pass
    #login_by_oauth2('10046352','1f082771f7c940849f6fd02ba5d3519f')

    #ret = login_by_email('54080@42qu.com','pw',u'10046352',u'1f082771f7c940849f6fd02ba5d3519f')
    #print ret.access_token
    #print ret.id
    #print user_info_get(ret.access_token,ret.id)

