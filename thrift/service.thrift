include "type.thrift"

service Sns {
    
    # Auth
    
    type.AuthResponse login_by_mail(
        1: i64                client_id,
        2: string             client_secret,
        3: string             mail,
        4: string             password
    )
    
    void logout(
        1: string             access_token
    )
    
    # User

    /* 约定：id为0，相当于查询自己 */
    type.UserExt user_ext_get(
        1: string             access_token,
        2: i64                gid,
    )

    void user_set(
        1: string    access_token,
        2: type.User          user
    )
 
    list<type.UserBasic> user_list(
        1: string             access_token,
        2: type.UserListType  type,
        3: i64                last_id,
        4: i64                num
    )

    list<type.UserBasic> user_list_fetch(
        1: list<i64>          id_list
    )
    
    # Task
    
    /* 约定: last_id 为0，相当于为最后一条信息的id */
    list<type.TaskBasic> task_list(
        1: string             access_token,
        2: type.TaskListType  type,
        3: type.TaskFilter    filter,
        4: i64                last_id,
        5: i64                num
    )

    list<type.TaskBasic> task_list_fetch(
        1: list<i64>          id_list
    )
    
    type.TaskExt task_ext_get (
        1: string             access_token,
        2: i64                gid,
    )
    
    void task_set (
        1: string       access_token,
        2: type.Task    task
    )
    
    i64 task_new( # Return task id
        1: string     access_token,
        2: type.Task  task 
    )

    bool task_apply(
        1: string access_token,
        2: i64    gid,
        3: string txt
    )
    
    bool task_reject(
        1: string access_token,
        2: i64    gid
    )
    
    bool task_accept(
        1: string access_token,
        2: i64    gid
    )
 
    bool my_task_accept(
        1: string access_token,
        2: i64    task_id,
        3: i64    user_id,
    )
    
    bool my_task_reject(
        1: string access_token,
        2: i64    task_id,
        3: i64    user_id,
        4: string txt
    )
   
    # Message

    list<type.Msg> msg_list(
        1: string             access_token,
        2: type.MsgType       type,
        3: i64                last_id,
        4: i64                num
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

