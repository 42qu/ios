include "Types.shrift"

service UserAPI {
  UserInfo getUserInfo(1: string accessToken,
                       2: UserID id)
    throws (1: Errors.UserException userException,
            2: Errors.SystemException systemException
            3: Errors.NotFoundException notFoundException),

  UserInfo editUserInfo(1: string accessToken,
                        2: UserInfo userInfo)
    throws (1: Errors.UserException userException,
            2: Errors.SystemException systemException)
}
