#coding:utf-8
import _env
from utils.type.ttypes import AuthResponse, UserInfo
from utils.exception.ttypes import Exception, ExceptionCode as ecode

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
        else:
            raise Exception(ecode.PERMISSION_DENIED)
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
                
                return AuthResponse(
                        user_id,
                        name,
                        access_token,
                        refresh_token,
                        87063
                )
            else:
                raise Exception(ecode.INNER_ERROR)
        else:
            raise Exception(ecode.USER_VERIFY_FAILED)
    else:
        raise Exception(ecode.PERMISSION_DENIED)

@access_token_verify
def user_info_get(access_token, id):
    user = Zsite.mc_get(id)
    if not user:
        raise Exception(ecode.USER_NOT_EXIST)
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

if __name__ == '__main__':
    pass
    #login_by_oauth2('10046352','1f082771f7c940849f6fd02ba5d3519f')

    #ret = login_by_email('54080@42qu.com','pw',u'10046352',u'1f082771f7c940849f6fd02ba5d3519f')
    #print ret.access_token
    #print ret.id
    #print user_info_get(ret.access_token,ret.id)

