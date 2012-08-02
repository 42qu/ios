#coding:utf-8
import _env

from ctrl.user import login_by_mail, user_get
from ctrl.task import task_get, task_apply, my_task_accept

import logging

class Handler(object):
    login_by_mail = login_by_mail
    
    def logout(self, acess_token):
        pass

    user_get = user_get
    task_get = task_get
    task_apply = task_apply
    my_task_accept = my_task_accept

    def user_info_get(self, access_token, uid, ext_only=True):
        b = UserBasic()

    def user_info_set(self, access_token, user_info):
        return u.user_info_set(access_token, user_info)

    def task_new(self, access_token, task):
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
    #print h.user_get('NYUrNthVRWe9moLBp5NhMQ', 168)
    #print h.task_get('NYUrNthVRWe9moLBp5NhMQ', 191, False)
    #print h.task_apply('NYUrNthVRWe9moLBp5NhMQ', 191, '123')
    h.my_task_accept('NYUrNthVRWe9moLBp5NhMQ', 191, 123)
    #print ret

