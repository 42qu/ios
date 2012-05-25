// ----- User Link -----

enum USER_LINK_TYPE {
  USER_LINK_TYPE_UNKNOWN = 0,
  USER_LINK_TYPE_42QU,
  USER_LINK_TYPE_DOUBAN,
  USER_LINK_TYPE_WEIBO,
}

struct UserLink {
  1:  required  i64 id,
  2:  required  USER_LINK_TYPE type,
  3:  required  string value,
  4:  optional  string customType
}

// ----- User Phone -----

enum USER_PHONE_TYPE {
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
  2:  required  USER_PHONE_TYPE type,
  3:  required  string value,
  4:  optional  string customType 
}

// ----- User Mail -----

enum USER_MAIL_TYPE {
  USER_MAIL_TYPE_UNKNOWN = 0,
  USER_MAIL_TYPE_PUBLIC,
  USER_MAIL_TYPE_CUSTOM,
  USER_MAIL_TYPE_HOME,
  USER_MAIL_TYPE_BUSINESS
}

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

