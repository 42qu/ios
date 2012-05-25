// ----- Auth -----
struct Auth {
  1:  required i64 id,
  2:  required string password,
  3:  required string clientKey,
  4:  required string clientSecret
}

enum {
  AUTH_SUCCESS = 0,
  AUTH_FAIL_REASON_UNKNOWN,
  AUTH_FAIL_SERVER_ERROR,
  AUTH_FAIL_CLIENT_KEY_NOT_AUTHORIZED,
  AUTH_FAIL_CLIENT_SECRET_WRONG,
  AUTH_FAIL_ID_NOT_EXIST,
  AUTH_FAIL_ID_INVALID,
  AUTH_FAIL_PASSWORD_WRONG
} typedef i64 AUTH_RESPONSE_STATUS

struct AuthResponse {
  1:  required AUTH_RESPONSE_STATUS status,
  2:  required i64 id,
  3:  optional string name,
  4:  required string accessToken,
  5:  optional i64 expireDate,
  6:  optional string refreshToken
}

// ----- User Link -----

enum {
  USER_LINK_TYPE_UNKNOWN = 0,
  USER_LINK_TYPE_42QU,
  USER_LINK_TYPE_DOUBAN,
  USER_LINK_TYPE_WEIBO
} typedef i64 USER_LINK_TYPE

struct UserLink {
  1:  required  i64 id,
  2:  required  USER_LINK_TYPE type,
  3:  required  string value,
  4:  optional  string customType
}

// ----- User Phone -----

enum {
  USER_PHONE_TYPE_UNKNOWN = 0,
  USER_PHONE_TYPE_PUBLIC,
  USER_PHONE_TYPE_CUSTOM,
  USER_PHONE_TYPE_MOBILE,
  USER_PHONE_TYPE_HOME,
  USER_PHONE_TYPE_BUSINESS,
  USER_PHONE_TYPE_FAX
} typedef i64 USER_PHONE_TYPE

struct UserPhone {
  1:  required  i64 id,
  2:  required  USER_PHONE_TYPE type,
  3:  required  string value,
  4:  optional  string customType 
}

// ----- User Mail -----

enum {
  USER_MAIL_TYPE_UNKNOWN = 0,
  USER_MAIL_TYPE_PUBLIC,
  USER_MAIL_TYPE_CUSTOM,
  USER_MAIL_TYPE_HOME,
  USER_MAIL_TYPE_BUSINESS
} typedef i64 USER_MAIL_TYPE

struct UserMail {
  1:  required  i64 id,
  2:  required  USER_MAIL_TYPE type,
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
