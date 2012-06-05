include "exception.thrift"
include "type.thrift"

service Sns {

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

    type.UserInfo user_info_get(
        1: string access_token,
        2: i64 id
    ) throws (1: exception.Exception e),

    type.UserInfo user_info_set(
        1: string access_token,
        2: type.UserInfo user_info
    )

    type.Task task_get(
        1: string access_token,
        2: i64 id
    )

    i64 task_new( // Return task id
        1: string access_token,
        2: type.Task task 
    )

    void task_apply(
        1: string access_token,
        2: i64 task_id
    )

    void task_reject(
        1: string access_token,
        2: i64 user_id
    )
    
    void task_accept(
        1: string access_token,
        2: i64 user_id
    )
    
    type.CommentList get_comment(
        1: string access_token,
        2: i64 id
    )
    
    void make_comment(
        1: string access_token,
        2: i64    id,
        3: string text
    )

    type.PersonList person_page(
        1: string access_token,
        2: i64 start,
        3: i64 limit
    )

}

