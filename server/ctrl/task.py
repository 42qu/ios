
# coding:utf-8

import _env

from kits import obj
from ctrl.verify import verify, verify_get_user

from model.base.user_name import UserName

from model.task.task import TASK_APPLY_STATE, TASK_APPLY_STATE, po_task_get, po_task_get_list, task_apply_new, task_apply_user_id_list, po_task_new

from model.task.tag import po_task_id_list_order_by_time, po_task_id_list_order_by_count, po_task_tag_id

from utils.type.ttypes import Task, TaskBasic, TaskExt
from utils.type.ttypes import TaskListType, TaskFilter, TaskSort

def _po_task_to_task_basic(po):
    if po and po.task:
        t = po.task
        basic = TaskBasic(
            id = po.id,
            name = po.name,
            sponsor = po.user_id,
            sponsor_name = UserName.get(po.user_id),
            intro = po.txt,
            state = t.state,
            area_id = t.area_id,
            end_time = t.end_time,
            reward = t.reward,
            reward_cent = t.reward_cent,
            apply_count = 0,
            invite_count = 0,
            accept_count = 0,
        )
        return basic

def _task_basic_to_po_task(bas):
    o = obj()
    o.name = bas.name
    o.txt = bas.intro
    o.area_id = bas.area_id
    o.address_id = bas.address_id
    o.end_time = bas.end_time
    o.reward = bas.reward
    o.reward_cent = bas.reward_cent
    return o

@verify
def task_ext_get(self, access_token, id, ext_only=True):
    print 'task_get %s' % id
    p = po_task_get(id)
    if not p:
        return
    t = p.task

    s = TASK_APPLY_STATE
    _d = dict()
    for i in (s.APPLY, s.ACCEPT):
        _d[i] = list(task_apply_user_id_list(id, i))

    ext = TaskExt(
            applied = _d[s.APPLY],
            invited = [],
            accepted = _d[s.ACCEPT],
        )

    return ext

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
    _task_basic_to_po_task(task.basic)
    po_task_new(uid, o, bas.tag_id)

@verify_get_user
def task_list(self, access_token, type, filter, last_id, num, uid=None):
    print 'task_list'
    lst = []
    if type == TaskListType.All:
        if filter.sort == TaskSort.ByTime:
            po_list = po_task_id_list_order_by_time
        else:
            po_list = po_task_id_list_order_by_count
        lst =  po_list(filter.tag_id, filter.city_id, filter.state, last_id, num)

    ret = []

    for i in lst:
        po = po_task_get(i)
        if po:
            baisc = _po_task_to_task_basic(po)
            ret.append(baisc)

    return ret

@verify
def task_list_fetch(self, id_list):
    return map(_po_task_to_task_basic, po_task_get_list(id_list))

