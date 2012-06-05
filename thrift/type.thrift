typedef i64 timestamp

// ----- Auth -----

struct AuthRequestMail {
  1:  required  string  client_id,
  2:  required  string  client_secret,
  3:  required  string  mail,
  4:  required  string  password
}

enum AuthLoginPartner {
    AUTH_PARTNER_DOUBAN = 1,
    AUTH_PARTNER_SINA = 2,
    AUTH_PARTNER_TENCENT = 3,
    AUTH_PARTNER_RENREN = 4,
    AUTH_PARTNER_KAIXIN = 5,
    AUTH_PARTNER_163 = 6,
    AUTH_PARTNER_FANFOU = 7
}

struct AuthRequestPartner {
  1:  required  string            client_id,
  2:  required  string            client_secret,
  3:  required  AuthLoginPartner  partner,
  4:  required  string            access_token,
  5:  required  string            mail
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
  1:  required  i64                 id,
  2:  optional  string              name,
  3:  required  string              access_token,
  4:  optional  string              refresh_token,
  5:  optional  i64                 expire_time
}

// ----- User Link -----

enum UserLinkType {
  USER_LINK_TYPE_UNKNOWN = 0,
  USER_LINK_TYPE_42QU,
  USER_LINK_TYPE_DOUBAN,
  USER_LINK_TYPE_WEIBO
}

struct UserLink {
  1:  required  i64           id,
  2:  required  UserLinkType  type,
  3:  required  string        value,
  4:  optional  string        label
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
  1:  required  i64            id,
  2:  required  UserPhoneType  type,
  3:  required  string         value,
  4:  optional  string         label 
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
  1:  required  i64           id,
  2:  required  UserMailType  type,
  3:  required  string        value,
  4:  optional  string        label
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

// ----- Status -----

struct StatusPost { // Used when posting a status
  1:  required  string        content,
  2:  optional  list<string>  tagList
}

struct StatusComment {
  1:  required  i64        id,
  2:  required  i64        authorID,
  3:  required  string     authorName,
  4:  required  timestamp  date,
  5:  required  string     content
}

struct Status {
  1:  required  i64                  id,
  2:  required  i64                  authorID,
  3:  required  string               authorName,
  4:  required  timestamp            date,
  5:  required  string               content,
  6:  required  i64                  commentCount,
  7:  optional  list<StatusComment>  commentList
}

// ----- Task -----

enum TaskCid {
    TASK_CID_EVENT = 1 // Not used for now
}

struct Task {
  1:  optional i64              id,
  2:  required  string          name,
  3:  required  string          intro,
  4:  required  TaskCid         cid,                        // Not used for now - -|
  5:  required  timestamp       begin_time,
  6:  required  timestamp       end_time,
  7:  optional  UserInfo        owner,
  8:  optional  list<UserInfo>  user_apply_list,
  11: optional  list<UserInfo>  user_accept_list,
  12: optional  list<UserInfo>  user_reject_list 
}

// ----- Person -----
struct Person {
    1: required string          name,               # 名字
    2: required string          org,                # 组织/学校
    3: required string          job,                # 工作/院系
    4: required string          page,               # 个人页链接
    5: optional string          url_avatar,         # 头像
    6: optional string          url_avarar_small    # 小头像
}

struct PersonList {
    1: required i64             num,                # 数量
    2: optional list<Person>    data                # 数据
}

// ----- Comment -----
struct Comment {
    1: required Person          who,                # 评论者
    4: required string          text,               # 评论文本
    3: optional timestamp       time                # 评论时间
}

struct CommentList {
    1: required i64             num,
    2: optional list<Comment>   data
}

