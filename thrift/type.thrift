
typedef i64 timestamp

struct AuthRequest {
  1: required string client_id,
  2: required string client_serect
}

struct AuthResponse {
  1:  required  i64                 uid,
  2:  required  string              name,
  3:  required  string              access_token,
  4:  optional  string              refresh_token,
  5:  optional  i64                 expire_time
}

enum enmSex {
  MALE,
  FEMALE,
  UNKNOW
}

struct UserInfo {
  1: required string name,
  2: required enmSex sex,
  3: required string org,
  4: required string job,
  5: required string small_avator,
  6: required string big_avator,
  7: required string intro
}

struct TaskInfo {
  1: required  i64              tid,
  2: required  string          name,
  3: required  string          intro,
  4: required  timestamp       begin_time,
  5: required  timestamp       end_time,
  6: required  i64             owner,
  7: required  list<i64>       user_apply_list,
  8: required  list<i64>       user_accept_list,
  9: required  list<i64>       user_reject_list 
}

struct TaskSummary {
  1: required list<i64> recommend,
  2: required list<i64> nearby,
  3: required list<i64> follow
}



/*enum AuthLoginPartner {
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

struct AuthRequestMail {
  1:  required  string  client_id,
  2:  required  string  client_secret,
  3:  required  string  mail,
  4:  required  string  password
}

# ############# User Begin ############# #

#
struct UserInfo {
    1:  required    i64         id,
    2:  required    string      nickname,
    3:  required    string      avatar, # Image URL
    4:  required    string      motto
    5:  required    string      org, # Company / School
    6:  required    string      job, # Job / Major
    7:  optional    string      firstname,
    8:  optional    string      lastname,
    9:  optional    string      gender,
    10: optional    timestamp   birthday,
    11: optional    string      location,
    12: optional    string      introduction # Self introduction
}

###
enum UserLinkType {
    Custom = 0,
    Public,

    Homepage,
    Home,
    Work,
    Other,
    
    SNSDouban,
    SNSWeibo, # Sina
    SNSRenren,
    SNSTencent, # Tencent twitr
    SNSGoogle
}

##
struct UserLink {
    1:  required    i64     id,
    2:  required    UserLinkType type,
    3:  required    string  value, # URL
    4:  optional    string  label
}

####
enum UserContactPhoneType {
    Custom = 0,
    Public,

    Mobile,
    IPhone,
    Home,
    Work,
    Main,
    HomeFax,
    WorkFax,
    OtherFax,
    Pager,
    Other
}
    
####
enum UserContactMailType {
    Custom = 0,
    Public,

    Home,
    Work,
    Other
}

###
enum UserContactType {
    None = 0,
    Phone,
    Mail
}

##
struct UserContact {
    1:  required    i64     id,
    2:  required    UserContactType type, # Phone or Mail
    3:  required    i64     subtype, # PhoneType or MailType
    4:  required    string  value, # Phone number or Mail address
    5:  optional    string  label
}

####
enum UserResumeStudyType {
    Undergraduate = 0,
    Master,
    Doctor,
    Janitor,
    Teacher
}

###
struct UserResumeStudy {
    1:  required    timestamp   starttime,
    2:  required    timestamp   endtime,
    3:  required    string      school,
    4:  required    string      major,
    5:  required    UserResumeStudyType type,
    6:  required    string      comment
}

###
struct UserResumeWork {
    1:  required    timestamp   starttime,
    2:  required    timestamp   endtime,
    3:  required    string      org,
    4:  required    string      job,
    5:  required    string      comment
}

##
struct UserResume {
    1:  required    list<UserResumeStudy>   studyList,
    2:  required    list<UserResumeWork>    workList
}

##
enum UserRelationship {
    None = 0,
    Following,
    Followed,
    Friend
}

#
struct User {
    1:  required    UserInfo            info,
    2:  required    list<UserLink>      linkList,
    3:  optional    list<UserContact>   contactList,
    4:  required    UserResume          resume,
    5:  required    UserRelationship    relationship
}

# ############# User End ############# #

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

struct TaskList {
    1: required i64             num,                # 数量
    2: optional list<Task>      data                # 数据
}

// ----- Comment -----
struct Comment {
    #1: required Person          who,                # 评论者
    4: required string          text,               # 评论文本
    3: optional timestamp       time                # 评论时间
}

struct CommentList {
    1: required i64             num,
    2: optional list<Comment>   data
}
*/
