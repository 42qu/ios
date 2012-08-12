include "type.thrift"

service Sns {
    
    # Auth
    
    type.AuthResponse login(
        1:  string      client_id,
        2:  string      client_secret,
        3:  string      mail,
        4:  string      password
    )
    
    bool logout(
        1:  string      access_token
    )
    
    # User
    
    /* 约定：id为0，相当于查询自己 */
    type.User user_get(
        1:  string      access_token,
        2:  i64         user_id
    )

    bool user_set(
        1:  string      access_token,
        2:  type.User   user
    )
     
    #list<type.UserBasic> user_list(
    #    1:  string      access_token,
    #    2:  list<i64>   id_list
    #)

    # Task
    
    #/* 约定: last_id 为0，相当于为最后一条信息的id */
    #list<type.TaskBasic> task_list(
    #    1:  string      access_token,
    #    2:  type.TaskListType   type,
    #    3:  type.TaskFilter     filter,
    #    4:  i64         last_id,
    #    5:  i64         num
    #)
    
    type.Task task_get (
        1:  string      access_token,
        2:  i64         task_id,
    )
    
    bool task_set (
        1:  string      access_token,
        2:  type.Task   task
    )
    
    i64 task_new( # Return task id
        1:  string      access_token,
        2:  type.Task   task 
    )

    bool task_apply(
        1:  string      access_token,
        2:  i64         task_id,
        3:  string      postscript
    )

    bool task_invite(
        1:  string      access_token,
        2:  i64         task_id,
        3:  list<i64>   user_id_list,
        4:  string      postscript
    )
    
    bool task_reply_application(
        1:  string      access_token,
        2:  i64         task_id,
        3:  i64         user_id,
        4:  bool        accepted,
        5:  string      postscript
    )
    
    bool task_reply_invitation(
        1:  string      access_token,
        2:  i64         task_id,
        3:  bool        accepted,
        4:  string      postscript
    )
    
    # Message

    list<type.Msg> msg_list(
        1: required string             access_token,
        2: required type.MsgType       type,
        3: required i64                last_id,
        4: required i64                num
    )

    void msg_send(
        1:  required string   access_token,
        2:  required i64      send_to,
        3:  required type.Msg msg
    )

    # Feed

    list<type.FeedMsg> feed (
        1: required string             access_token,
        2: required i64                last_id,
        3: required i64                num
    )

    # Summary

    type.Summary summary(
        1: required string access_token
    )

}

