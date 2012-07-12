# Global

typedef i64 timestamp

# Auth

struct AuthRequest {
    1:  required    string  client_id,
    2:  required    string  client_serect
}

struct AuthResponse {
    1:  required    string  access_token,
    2:  required    i64     expire_in,
    3:  optional    string  refresh_token
}

# Task

enum TaskStatus {
    None = 0,    
    Applied,    # Applied but no response
    Accepted,
    Rejected
}

struct TaskBasic {
    1:  required    i64             tid,
    2:  required    string          title,
    3:  required    i64             sponsor,
    4:  required    string          intro,
    5:  required    TaskStatus      status,
    6:  required    timestamp       begin_time,
    7:  required    timestamp       end_time,
    8:  required    i64             planed, # 计划人数
    9:  required    i64             applied,
    10: required    i64             invited,
    11: required    i64             accepted
}

struct TaskExt {
    1:  required    list<TaskStatus>    status,
    2:  required    list<i64>           applied_list,
    3:  required    list<i64>           invited_list,
    4:  required    list<i64>           accepted_list
}

struct Task {
    1:  optional    TaskBasic   basic,
    2:  required    TaskExt     ext
}

enum TaskListType {
    All = 0,
    Recommend,
    Nearby,
    Following,
    Staring
}

struct TaskListRequest {
    1:  required    i64             lasttid,
    2:  required    i64             length
    3:  required    TaskListType    type
}

# User

enum UserGender {
    Unknown = 0,
    Male,
    Female
}

struct UserBasic {
    1:  required    string          name,
    2:  required    UserGender      gender,
    3:  required    string          org,
    4:  required    string          job,
    5:  required    string          avator # URL
}

struct UserExt {
    1:  required    string      intro,
    2:  required    list<i64>   following_list,
    3:  required    list<i64>   followed_list
}

struct User {
    1:  optional    UserBasic   basic,
    2:  required    UserExt     ext
}

# end

