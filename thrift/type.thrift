
// ----- User Link -----

typedef i64 LinkID
enum {
  USER_LINK_CID_UNKNOWN = 0,
  USER_LINK_CID_42QU,
  USER_LINK_CID_DOUBAN,
  USER_LINK_CID_WEIBO
} typedef i64 USER_LINK_CID

struct UserLink {
  1:  required  i64 id,
  2:  required  USER_LINK_CID cid,
  3:  required  string rid
  4:  optional  string txt //自定义的描述 , 比如 饭否 , 点点
}

typedef i64 PhoneID
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
  2:  required  USER_PHONE_TYPE cid,
  3:  required  string rid,
  4:  optional  string txt 
}

enum {
  UserMailTypeUnknown = 0,
  UserMailTypePublic,
  UserMailTypeCustom,
  UserMailTypeHome,
  UserMailTypeBusiness
} typedef i64 UserMailType

struct UserMail {
  1:  required  i64 id,
  2:  required  UserMailType cid,
  3:  required  string rid,
  4:  optional  string customType
}

struct UserInfo {
  1:  required  i64                 id,
  2:  required  string              name,
  3:  optional  string              txt,
  4:  optional  string              ico,
  5:  optional  list<UserLink>      user_link_list,
  6:  optional  list<UserPhone>     user_phone_list,
  7:  optional  list<UserMail>      user_mail_list
}


