# Global

typedef i64 timestamp

# Auth

struct AuthRequest {
    1:  required    string  id,
    2:  required    string  serect
}

struct AuthResponse {
    1:  required    i64     uid,
    2:  required    string  name,
    3:  required    string  access,
    4:  optional    string  refresh,
    5:  optional    i64     expire
}

# Task

struct TaskBasic {
    1:  required    i64             tid,
    2:  required    string          title,
    3:  required    i64             sponsor,
    4:  required    string          intro,
    5:  required    TaskBasicStatus status,
    6:  required    timestamp       begin,
    7:  required    timestamp       end,
    8:  required    i64             planed, # 计划人数
    9:  required    i64             applied,
    10: required    i64             invited,
    11: required    i64             accepted
}

enum TaskExtStatus {
    None = 0,    
    Applied,    # Applied but no response
    Accepted,
    Rejected
}

struct TaskExt {
    1:  required    list<TaskExtStatus> status,
    2:  required    list<i64>           appliedList,
    3:  required    list<i64>           invitedList,
    4:  required    list<i64>           acceptedList
}

struct Task {
    1:  optional    TaskBasic   basic,
    2:  required    TaskExt     ext
}

enum TaskListType {
    All = 0,
    Recommend,
    Nearby,
    Follow,
    Starred
}

struct TaskListRequest {
    1:  required    i64             lasttid,
    2:  required    i64             length
    3:  required    TaskListType    type
}

struct TaskListResponse {
    1:  required    i64             lastid, # the new one
    2:  required    i64             length
    3:  required    TaskListType    type
    4:  required    list<TaskBasic> taskList
}

# User

enum UserBasicGender {
    Unknown = 0,
    Male,
    Female,
    Other
}

struct UserBasic {
    1:  required    string          name,
    2:  required    UserBasicGender gender,
    3:  required    string          org,
    4:  required    string          job,
    5:  required    string          avator # URL
}

struct UserExt {
    1:  required    string      intro,
    2:  required    list<i64>   followingList,
    3:  required    list<i64>   followedList
}

struct User {
    1:  optional    UserBasic   basic,
    2:  required    UserExt     ext
}

# end
