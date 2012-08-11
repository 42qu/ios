
# coding:utf-8

import _env

from model.base.user_mail import user_id_by_mail
from model.base.user_password import user_password_verify
from model.app.oauth2 import code_new, access_token_new
from utils.type.ttypes import AuthResponse

import model.base.user_name
import model.user.user_ico

from model.base.user import User as _User
from model.user.user_career import user_title
from model.user.user_info import motto_by_id, user_info_by_id
from utils.type.ttypes import User, UserGender, UserMarry, UserBasic, UserExt

from server.ctrl.verify import verify

def _user_to_user_basic(u):
    if u:
        return UserBasic(
            gid = u.id,
            name = u.name,
            gender = 0,
            org = u.title[0],
            title = u.title[1],
            avatar = u.ico.link
        )

def login_by_mail(self, client_id, client_secret,  mail, pw):
    print 'login_by_mail'
    user_id = user_id_by_mail(mail)
    if user_id:
        if user_password_verify(user_id, pw):
            code = code_new(client_id, user_id)
            if code:
                ret = access_token_new(client_id, client_secret, code)
                if ret:
                    return AuthResponse(**ret)
                else:
                    print '获取 token 失败'
        else:
            # 验证失败
            print '验证失败'
    else:
        # 用户不存在
        print '用户不存在'

@verify
def user_ext_get(self, access_token, id):
    print 'user_ext_get'
    # TODO:另一端暂无对应
    u = _User(id)
    info = user_info_by_id(id)

    ext = UserExt(
            motto = motto_by_id(id),
            intro = info.txt,
            marry = UserMarry(info.marrige_state),
            following=[],
            followed=[]
        )

    return ext

@verify
def user_list_fetch(self, id_list):
    lst = []
    for i in id_list:
        lst.append(_User(i))
    return map(_user_to_user_basic, lst)

