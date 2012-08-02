
# coding:utf-8

import _env

from kits import obj

from model.task.task import TASK_APPLY_STATE, TASK_APPLY_STATE, po_task_get, task_apply_new, task_apply_user_id_list, po_task_new

from ctrl.verify import verify, verify_get_user

from utils.type.ttypes import Task, TaskBasic, TaskExt

@verify
def task_get(self, access_token, id, ext_only=True):
    print 'task_get %s' % id
    p = po_task_get(id)
    if not p:
        return
    t = p.task

    s = TASK_APPLY_STATE
    _d = dict()
    for i in (s.APPLY, s.ACCEPT):
        _d[i] = list(task_apply_user_id_list(id, i))

    basic = TaskBasic(
            id = p.id,
            name = p.name,
            sponsor = p.user_id,
            intro = p.txt,
            state = t.state,
            area_id = t.area_id,
            begin_time = t.begin_time,
            reward = t.reward,
            reward_cent = t.reward_cent,
            apply_count = len(_d[s.APPLY]),
            invite_count = 0,
            accept_count = len(_d[s.ACCEPT]),
        ) if not  ext_only else None

    ext = TaskExt(
            applied = _d[s.APPLY],
            invited = [],
            accepted = _d[s.ACCEPT],
        )

    return Task(basic=basic, ext=ext)

@verify_get_user
def task_apply(self, access_token, task_id, txt='', uid=None):
    print 'task_apply %s' % task_id
    po = po_task_get(task_id)
    if po:
        po.task.apply(uid, txt)
        return True
    else:
        return False

@verify_get_user
def my_task_accept(self, access_token, task_id, user_id,  uid=None):
    po = po_task_get(task_id)
    if po and po.can_admin(uid):
        po.task.accept(user_id)

@verify_get_user
def my_task_reject(self, access_token, task_id, user_id, txt='', uid=None):
    po = po_task_get(task_id)
    if po and po.can_admin(uid):
        po.task.reject(user_id, txt)

@verify_get_user
def task_new(self, access_token, task, uid=None):
    bas = task.basic
    #ext = tasl.ext

    o = obj()
    o.name = bas.name
    o.txt = bas.intro
    o.area_id = bas.area_id
    o.address = bas.address
    o.begin_time = bas.begin_time
    o.reward = bas.reward
    o.reward_cent = bas.reward_cent
    po_task_new(uid, o, bas.tag_id)

