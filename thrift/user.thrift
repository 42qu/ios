include "error.shrift"
include "type.shrift"

service UserAPI {


UserInfo userInfo_Get(
    1: string accessToken,
    2: i64 id
)
    throws (
        1: Error.UserException userException,
        2: Error.SystemException systemException,
        3: Error.NotFoundException notFoundException
    ),


UserInfo userInfo_Save(
    1: string accessToken,
    2: UserInfo userInfo
)
    throws (
        1: Error.UserException userException,
        2: Error.SystemException systemException
    )


}
