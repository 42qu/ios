// ----- Auth -----
struct Auth {
  1:  required i64 id,
  2:  required string password,
  3:  required string clientKey,
  4:  required string clientSecret
}

enum AuthResponseStatus {
  AUTH_SUCCESS = 0,
  AUTH_FAIL_REASON_UNKNOWN,
  AUTH_FAIL_SERVER_ERROR,
  AUTH_FAIL_CLIENT_KEY_NOT_AUTHORIZED,
  AUTH_FAIL_CLIENT_SECRET_WRONG,
  AUTH_FAIL_ID_NOT_EXIST,
  AUTH_FAIL_ID_INVALID,
  AUTH_FAIL_PASSWORD_WRONG
}

struct AuthResponse {
  1:  required  AuthResponseStatus status,
  2:  required  i64 id,
  3:  optional  string name,
  4:  required  string accessToken,
  5:  optional  i64 expireDate,
  6:  optional  string refreshToken
}

// ----- User Link -----

enum UserLinkType {
  USER_LINK_TYPE_UNKNOWN = 0,
  USER_LINK_TYPE_42QU,
  USER_LINK_TYPE_DOUBAN,
  USER_LINK_TYPE_WEIBO
}

struct UserLink {
  1:  required  i64 id,
  2:  required  UserLinkType type,
  3:  required  string value,
  4:  optional  string customType
}

// ----- User Phone -----

enum UserPhoneType {
  USER_PHONE_TYPE_UNKNOWN = 0,
  USER_PHONE_TYPE_PUBLIC,
  USER_PHONE_TYPE_CUSTOM,
  USER_PHONE_TYPE_MOBILE,
  USER_PHONE_TYPE_HOME,
  USER_PHONE_TYPE_BUSINESS,
  USER_PHONE_TYPE_FAX
}

struct UserPhone {
  1:  required  i64 id,
  2:  required  UserPhoneType type,
  3:  required  string value,
  4:  optional  string customType 
}

// ----- User Mail -----

enum UserMailType {
  USER_MAIL_TYPE_UNKNOWN = 0,
  USER_MAIL_TYPE_PUBLIC,
  USER_MAIL_TYPE_CUSTOM,
  USER_MAIL_TYPE_HOME,
  USER_MAIL_TYPE_BUSINESS
}

struct UserMail {
  1:  required  i64 id,
  2:  required  UserMailType type,
  3:  required  string value,
  4:  optional  string customType
}

// ----- User Info -----

struct UserInfo {
  1:  required  i64                 id,
  2:  required  string              name,
  3:  optional  string              intro,
  4:  optional  binary              picture,
  5:  optional  list<UserLink>      userLinkList,
  6:  optional  list<UserPhone>     userPhoneList,
  7:  optional  list<UserMail>      userMailList
}
