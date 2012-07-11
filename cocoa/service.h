/**
 * Autogenerated by Thrift Compiler (0.8.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

#import <Foundation/Foundation.h>

#import <TProtocol.h>
#import <TApplicationException.h>
#import <TProtocolUtil.h>
#import <TProcessor.h>

#import "exception.h"
#import "type.h"

@protocol Sns <NSObject>
- (AuthResponse *) login_by_mail: (AuthRequest *) auth : (NSString *) mail : (NSString *) password;  // throws TException
- (void) logout: (NSString *) access_token;  // throws TException
- (UserInfo *) user_info_get: (NSString *) access_token : (int64_t) uid : (BOOL) ext_only;  // throws TException
- (NSArray *) task_list: (NSString *) access_token : (int) type : (int64_t) last_id : (int64_t) num;  // throws TException
- (TaskInfo *) task_get: (int64_t) access_token : (int64_t) tid : (BOOL) ext_only;  // throws TException
- (int64_t) task_new: (NSString *) access_token : (TaskInfo *) task;  // throws TException
- (BOOL) task_apply: (NSString *) access_token : (int64_t) tid;  // throws TException
- (BOOL) task_reject: (NSString *) access_token : (int64_t) user_id;  // throws TException
- (BOOL) task_accept: (NSString *) access_token : (int64_t) user_id;  // throws TException
@end

@interface SnsClient : NSObject <Sns> {
  id <TProtocol> inProtocol;
  id <TProtocol> outProtocol;
}
- (id) initWithProtocol: (id <TProtocol>) protocol;
- (id) initWithInProtocol: (id <TProtocol>) inProtocol outProtocol: (id <TProtocol>) outProtocol;
@end

@interface SnsProcessor : NSObject <TProcessor> {
  id <Sns> mService;
  NSDictionary * mMethodMap;
}
- (id) initWithSns: (id <Sns>) service;
- (id<Sns>) service;
@end

@interface serviceConstants : NSObject {
}
@end
