# Global

typedef i64 timestamp

# Auth

struct AuthRequest {
    1:  required    i64     client_id,
    2:  required    string  client_secret
}

struct AuthResponse {
    1:  required    string        access_token,
    2:  required    timestamp     expire_in,
    3:  required    i64           user_id
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
    1:  required    i64             id,
    2:  required    string          name,
    3:  required    UserGender      gender,
    4:  required    string          org,
    5:  required    string          job,
    6:  required    string          avator # URL
}

struct UserExt {
    1:  required    string      intro,
    2:  required    list<i64>   following,
    3:  required    list<i64>   followed
}

struct User {
    1:  optional    UserBasic   basic,
    2:  required    UserExt     ext
}

# Task

enum TaskStatus {
    Removed = 0,    
    Apply = 16,    # Applied but no response
    Reject = 32,
    Close = 64,
    Open = 128
}

enum TaskSort {
    ByTime = 0,
    ByCount = 1
}

struct TaskFilter {
    1:  required    TaskSort        sort,
    2:  optional    i64             city_id,
    3:  optional    i64             tag_id,
    4:  optional    i64             distance,
    5:  optional    UserGender      sponsor_gender,
    6:  optional    i64             level,
    7:  optional    bool            reward,
    8:  optional    i64             reward_cent
}

struct TaskBasic {
    1:  required    i64             id,
    2:  required    string          name,
    3:  required    i64             sponsor,
    4:  required    i64             tag_id,
    5:  required    string          intro,
    6:  required    TaskStatus      state,
    7:  required    i64             area_id,
    8:  required    string          address,
    9:  required    timestamp       begin_time,
    10: required    string          reward,
    11: required    i64             reward_cent,
    12: required    i64             apply_count,
    13: required    i64             invite_count,
    14: required    i64             accept_count
}

struct TaskExt {
    1:  required    list<i64>           applied,
    2:  required    list<i64>           invited,
    3:  required    list<i64>           accepted
}

struct Task {
    1:  optional    TaskBasic   basic,
    2:  required    TaskExt     ext
}

enum TaskListType {
    All = 0,
    Recommend = 2,
    Nearby = 4,
    Following = 8
}

struct TaskListRequest {
    1:  required    i64             lastid,
    2:  required    i64             length
    3:  required    TaskListType    type
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

