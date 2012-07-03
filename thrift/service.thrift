include "exception.thrift"
include "type.thrift"

service Sns {

    ###### Auth ######

    type.AuthResponse login_by_mail(
        1:type.AuthRequestMail auth
    ) throws (1: exception.Exception e),

    type.AuthResponse login_by_oauth(
        1:string  client_id,
        2:string  client_secret,
        3:string  access_token,
        4:string  mail
    )

    type.AuthResponse login_by_oauth2(
        1:string  client_id,
        2:string  client_secret,
        3:string  access_token,
        4:string  mail
    )
    
    void logout(1:string access_token)
    
    ###### User ######
    
    type.UserInfo user_info_get(
        1:  string  access_token,
        2:  i64     id
    ) throws (1: exception.Exception e),

    type.User user_get(
        1:  string  access_token,
        2:  i64     id
    ) throws (1: exception.Exception e),

    ###### Task ######
    
    type.TaskList task_list(
        1: string access_token
        2: i64 start,
        3: i64 limit
    )
    
    type.Task task_info(
        1: string access_token,
        2: i64 id
    )

    # 创建任务
    i64 task_new( // Return task id
        1: string access_token,
        2: type.Task task 
    )

    # 申请任务
    void task_apply(
        1: string access_token,
        2: i64 task_id
    )
    
    # 拒绝任务
    void task_reject(
        1: string access_token,
        2: i64 user_id
    )
    
    # 接收任务
    void task_accept(
        1: string access_token,
        2: i64 user_id
    )
    
    type.CommentList comment_get(
        1: string access_token,
        2: i64 id
    )
    
    void comment_make(
        1: string access_token,
        2: i64    id,
        3: string text
    )

    #type.PersonList person_page(
    #    1: string access_token,
    #    2: i64 start,
    #    3: i64 limit
    #)

}

