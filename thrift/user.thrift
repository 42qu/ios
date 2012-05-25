include "Types.shrift"

service UserAPI {



UserInfo user_info_get(
    1: string access_token,
    2: i64 id
)
    throws (
        1: Errors.UserException user_exception,
        2: Errors.SystemException system_exception
        3: Errors.NotFoundException not_found_exception
    ),


UserInfo user_info_save(
    1: string access_token,
    2: UserInfo user_info
)
    throws (
        1: Errors.UserException user_exception,
        2: Errors.SystemException system_exception
    )


}
