include "error.thrift"
include "type.thrift"

service Sns {

    type.AuthResponse login(
        1: type.Auth auth
    )
        throws (
            1: error.UserException userException,
            2: error.SystemException systemException
        ),

    type.UserInfo userInfo_get(
        1: string accessToken,
        2: i64 id
    )
        throws (
            1: error.UserException userException,
            2: error.SystemException systemException,
            3: error.NotFoundException notFoundException
        ),

    type.UserInfo userInfo_set(
        1: string accessToken,
        2: type.UserInfo userInfo
    )
        throws (
            1: error.UserException userException,
            2: error.SystemException systemException
        )
}

service Event {

    type.EventInfo eventInfo_get(
        1: string accessToken,
        2: i64 id
    )
        throws (
            1: error.UserException userException,
            2: error.SystemException systemException,
            3: error.NotFoundException notFoundException
        ),

    type.EventInfo eventInfo_set(
        1: string accessToken,
        2: type.EventInfo eventInfo
    )
        throws (
            1: error.UserException userException,
            2: error.SystemException systemException
        )

    i64 eventPublish( // Return a new created event id
        1: string accessToken
    )
        throws (
            1: error.UserException userException,
            2: error.SystemException systemException
        )

    type.EventInfo eventApply(
        1: string accessToken,
        2: i64 id
    )
        throws (
            1: error.UserException userException,
            2: error.SystemException systemException,
            3: error.NotFoundException notFoundException
        )
}
