
# coding:utf-8

import _env

from model.task.task import TASK_APPLY_STATE, TASK_APPLY_STATE, po_task_get, task_apply_new, task_apply_user_id_list

from ctrl.verify import verify, verify_get_user

from utils.type.ttypes import Task, TaskBasic, TaskExt

@verify
def task_get(self, access_token, id, ext_only=True):
    p = po_task_get(id)
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
    task_apply_new(task_id, uid, TASK_APPLY_STATE.APPLY)
    return True

