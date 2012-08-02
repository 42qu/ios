
# coding:utf-8

import _env

from model.base.user_mail import user_id_by_mail
from model.base.user_password import user_password_verify
from model.app.oauth2 import code_new, access_token_new
from utils.type.ttypes import AuthResponse

import model.base.user_name
import model.user.user_ico
from model.base.user import User as _User
from utils.type.ttypes import User, UserGender, UserBasic, UserExt

from server.ctrl.verify import verify

def login_by_mail(self, auth, mail, pw):
    print 'login_by_mail'
    user_id = user_id_by_mail(mail)
    if user_id:
        if user_password_verify(user_id, pw):
            code = code_new(auth.client_id, user_id)
            if code:
                ret = access_token_new(auth.client_id, auth.client_secret, code)
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
def user_get(self, access_token, id, ext_only=True):
    u = _User(id)
    
    basic = UserBasic(id=u.id, name=u.name, gender=UserGender.Unknown,
            org='org', job='job', avator=u.ico.link) if not  ext_only else None

    ext = UserExt(intro="简介暂时没有对应参数",
            following=[],
            followed=[]
        )

    return User(basic=basic, ext=ext)

