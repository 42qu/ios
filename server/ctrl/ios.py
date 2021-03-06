#coding:utf-8
import _env

from ctrl.user import login_by_mail, user_ext_get, user_list_fetch
from ctrl.task import task_ext_get, task_list, task_list_fetch
from ctrl.task import task_apply, task_new
from ctrl.task import my_task_accept, my_task_reject

import logging

class Handler(object):
    login_by_mail = login_by_mail
    
    def logout(self, acess_token):
        pass

    user_ext_get = user_ext_get
    task_ext_get = task_ext_get
    task_apply = task_apply
    my_task_accept = my_task_accept
    my_task_reject = my_task_reject
    task_new = task_new

    user_list_fetch = user_list_fetch

    task_list = task_list
    task_list_fetch = task_list_fetch

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

