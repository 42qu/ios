include "error.thrift"
include "type.thrift"

service UserAPI {
    type.UserInfo info_get( 1: string accessToken, 2: i64 id)
        throws (
            1: error.UserException userException,
            2: error.SystemException systemException,
            3: error.NotFoundException notFoundException
           ),

    type.UserInfo info_set(1: string accessToken,2: type.UserInfo userInfo)
        throws (
            1: error.UserException userException,
            2: error.SystemException systemException
          )
}

