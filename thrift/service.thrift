include "error.thrift"
include "type.thrift"

service Sns {

    type.AuthResponse login(
        1: type.Auth auth
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

    i64 task_new(
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
