#coding:utf-8
import _env
from utils.type.ttypes import AuthResponse, AuthResponseStatus, UserInfo

from model.user_mail import user_id_by_mail, mail_by_user_id
from model.user_auth import mail_password_verify
from model.zsite import Zsite
#from model.api_user import json_info
#from model.follow import follow_id_list_by_from_id, follow_id_list_by_to_id, follow_count_by_to_id, follow_count_by_from_id, follow_rm, follow_new
from model.oauth2 import oauth_access_token_new, oauth_refresh_token_new, oauth_secret_verify, oauth_access_token_verify

from model.ico import ico_url
from time import time

def access_token_verify(func):
    def new(*args,**argkw):
        if len(args)<1:
            return func()
        if oauth_access_token_verify(args[0]):
            return func(*args,**argkw)
    return new

def login_by_email(mail, pw, client_id, client_secret):
    
    user_id = None
    if oauth_secret_verify(client_id, client_secret):
        if mail_password_verify(mail,pw):
            user_id = int(user_id_by_mail(mail))
            if user_id:
                id, access_token = oauth_access_token_new(client_id, user_id)
                refresh_token = oauth_refresh_token_new(client_id, id)
                user = Zsite.mc_get(user_id)
                name = user.name
                
                status = AuthResponseStatus.AUTH_SUCCESS
                return AuthResponse(
                        status,
                        user_id,
                        name,
                        access_token,
                        refresh_token,
                        87063
                )
            else:
                print 'failed 1'
        else:
            print 'failed 2'
    else:
        print 'failed 3'

@access_token_verify
def user_info_get(access_token, id):
    user = Zsite.mc_get(id)
    if not user:
        # TODO:ERROR 查无此人
        return
    name = user.name
    intro = user.txt
    pic = ico_url(id)
    link = ['暂无']
    phone = ['暂无']
    mail = [mail_by_user_id(id)]
    return UserInfo(id, name, intro, pic, link, phone, mail)

def user_info_set(access_token, user_info):
    pass

def b(f):
    def new(*arg,**argw):
        return f(*arg,**argw)
    return new

@b
def a(c):
    print 'a'

if __name__ == '__main__':
    ret = login_by_email('54080@42qu.com','pw',u'10046352',u'1f082771f7c940849f6fd02ba5d3519f')
    print ret.access_token
    print ret.id
    print user_info_get(ret.access_token,ret.id)

