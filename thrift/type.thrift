# Global

typedef i64 timestamp

# Auth

struct AuthResponse {
    1:  required    string      access_token,
    2:  required    timestamp   expire_in,
    3:  required    i64         user_id
}

# User

enum UserGender {
    Unknown = 0,
    Male,
    Female
}

enum UserListType {
    All = 0,
    Recommend,
    Nearby,
    Following,
    Followed,
    Friends
}

struct UserBasic {
    1:  required    i64             user_id,
    2:  required    string          name,
    3:  required    UserGender      gender,
    4:  required    string          org,
    5:  required    string          job,
    6:  required    string          avator # URL
}

struct UserExt {
    1:  required    string          intro,
    2:  required    list<i64>       following,
    3:  required    list<i64>       followed
}

struct User {
    1:  required    UserBasic       basic,
    2:  required    UserExt         ext
}

# Task

enum TaskState {
    Normal = 0,
    Interested, # Added to collection
    Accepted,
    Applied, # Applied but no response
    Invited, # Invited but not yet accepted
    Rejected
}

struct TaskBasic {
    1:  required    i64             task_id,
    2:  required    TaskState       state,
    3:  required    string          title,
    4:  required    string          intro,
    5:  required    string          cover, # URL
    6:  required    UserBasic       sponsor,
    7:  required    timestamp       start_time,
    8:  required    timestamp       end_time,
    9:  required    i64             interested_count,
    10: required    i64             accepted_count,
    11: optional    i64             invited_count,
    12: optional    i64             applied_count,
    13: optional    i64             rejected_count
}

struct TaskExt {
    1:  required    string          intro_detail,
    2:  required    list<i64>       interested_list,
    3:  required    list<i64>       accepted_list,
    4:  optional    list<i64>       invited_list,
    5:  optional    list<i64>       applied_list
    6:  optional    list<i64>       rejected_list
}

struct Task {
    1:  required    TaskBasic       basic,
    2:  required    TaskExt         ext
}

enum TaskListType {
    All = 0,
    Recommend,
    Nearby,
    Following
}

struct TaskListRequest {
    1:  required    TaskListType    type,
    2:  required    i64             lastid,
    3:  required    i64             length
}

# Message

enum MsgType {
    All = 0,
    System = 1,
    Friends = 2,
    Stranger = 4,
    Unread   = 8
}

struct Msg {
    1:  required    i64         sender,
    2:  required    timestamp   time,
    3:  required    string      text,
    4:  optional    MsgType     type
}

# Feed

enum FeedType {
    All,
    Text,
    Article,
    Pic,
    Activity
}

struct FeedMsg {
    1:  required   string     sender,
    2:  required   timestamp  time,
    3:  required   FeedType   type,
    4:  required   string     content
}

# Summary

struct Summary {
    1:  required  i64          unread_msg_num,
    2:  required  i64          following_num,
    3:  required  i64          followed_num
}

# end

