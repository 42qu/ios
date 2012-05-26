#coding:utf-8
import _env
from utils.type.ttypes import AuthResponse, AuthResponseStatus, UserInfo

from model.user_mail import user_id_by_mail
from model.user_auth import mail_password_verify
from model.zsite import Zsite
#from model.api_user import json_info
#from model.follow import follow_id_list_by_from_id, follow_id_list_by_to_id, follow_count_by_to_id, follow_count_by_from_id, follow_rm, follow_new
from model.oauth2 import oauth_access_token_new, oauth_refresh_token_new, oauth_secret_verify

from array import array
from time import time

def login(mail, pw, client_id, client_secret):
    
    user_id = None
    if oauth_secret_verify(client_id, client_secret):
        if mail_password_verify(mail,pw):
            user_id = user_id_by_mail(mail)
            if user_id:
                id, access_token = oauth_access_token_new(client_id, user_id)
                refresh_token = oauth_refresh_token_new(client_id, id)
                user = Zsite.mc_get(user_id)
                name = user.name
                
                status = AuthResponseStatus(AUTH_SUCCESS)
                return AuthResponse({
                    'status'        : status,
                    'id'            : user_id,
                    'name'          : name,
                    'accessToken'   : access_token,
                    'refresh_Token' : refresh_token,
                    'expireDate'    : 87063,
                })

def userinfo_get(accessToken, id):
    user_id = user_id_by_mail(mail)
    #return 

def userinfo_set(accessToken, userInfo):
    pass


if __name__ == '__main__':
    print login('user','pw',10299882,'df36723f6bc246f0a485e74ff852a6c3')


