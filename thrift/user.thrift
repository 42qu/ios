include "error.shrift"
include "type.shrift"

service UserAPI {


UserInfo getUserInfo(
    1: string accessToken,
    2: i64 id
)
    throws (
        1: Error.UserException userException,
        2: Error.SystemException systemException,
        3: Error.NotFoundException notFoundException
    ),


UserInfo saveUserInfo(
    1: string accessToken,
    2: UserInfo userInfo
)
    throws (
        1: Error.UserException userException,
        2: Error.SystemException systemException
    )


}
