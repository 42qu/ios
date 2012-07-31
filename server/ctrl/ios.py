#coding:utf-8
import _env
from model.base.user_mail import user_id_by_mail
from model.base.user_password import user_password_verify

from model.app.oauth2 import code_new, access_token_new

from utils.type.ttypes import AuthResponse

#from utils.type.ttypes import 
#from server.model.ios import t

import logging

class Handler(object):
    def login_by_mail(self, auth, mail, pw):
        print 'login_by_mail'
        user_id = user_id_by_mail(mail)
        if user_id:
            if user_password_verify(user_id, pw):
                code = code_new(auth.client_id, user_id)
                if code:
                    ret = access_token_new(auth.client_id, auth.client_secret, code)
                    if ret:
                        return AuthResponse(ret)
                    else:
                        print '获取 token 失败'
            else:
                # 验证失败
                print '验证失败'
        else:
            # 用户不存在
            print '用户不存在'


    #def login_by_oauth(self, client_id, client_secret):
    #    pass

    #def login_by_oauth2(self, auth):
    #    if u.oauth_secret_verify(auth.client_id, auth.client_secret):
    #        pass

    def logout(self, acess_token):
        pass
    
    def user_info_get(self, access_token, id):
        return u.user_info_get(access_token, id)

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
    ret = h.login_by_mail(r, 'fy0@qq.com','794613852')
    print ret

