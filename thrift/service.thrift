include "exception.thrift"
include "type.thrift"

service Sns {

    type.AuthResponse login_by_mail(
        1:type.AuthRequestMail auth_request_mail
    )

    type.AuthResponse login_by_oauth(
        1:string  client_key,
        2:string  client_secret,
        //todo
    )

    type.AuthResponse login_by_oauth2(
        1:string  client_key,
        2:string  client_secret,
        //todo
    )

    void logout(1:string access_token)



    type.UserInfo user_info_get(
        1: string access_token,
        2: i64 id
    )

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


}
