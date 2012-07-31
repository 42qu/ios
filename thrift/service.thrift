include "type.thrift"

service Sns {
    
    # Auth
    
    i64 login_by_mail(
        1: required type.AuthRequest auth,
        2: required string mail,
        3: required string password
    )
    
    void logout(
        1: required string access_token
    )
    
    # User
    
    /* 约定：uid为0，相当于查询自己 */
    type.User user_get(
        1: required string  access_token,
        2: required i64     uid,
        3: required bool    ext_only = true
    )

    void user_set(
        1: required  string    access_token,
        2: required  type.User user
    )
     
    list<type.UserBasic> user_list(
        1: required string             access_token,
        2: required type.UserListType  type,
        3: required i64                last_id,
        4: required i64                num
    )

    # Task
    
    /* 约定: last_id 为0，相当于为最后一条信息的id */
    list<type.TaskBasic> task_list(
        1: required string             access_token,
        2: required type.TaskListType  type,
        3: required i64                last_id,
        4: required i64                num
        5: required type.TaskFilter    filter,
    )
    
    type.Task task_get (
        1: required i64                access_token,
        2: required i64                tid,
        3: required bool               ext_only = true,
    )
    
    void task_set (
        1: required string       access_token,
        2: required type.Task    task
    )
    
    i64 task_new( # Return task id
        1: string     access_token,
        2: type.Task  task 
    )

    bool task_apply(
        1: string access_token,
        2: i64    tid
    )
    
    bool task_reject(
        1: string access_token,
        2: i64    tid
    )
    
    bool task_accept(
        1: string access_token,
        2: i64    tid
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

