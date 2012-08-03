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

#import "type.h"

@protocol Sns <NSObject>
- (AuthResponse *) login_by_mail: (AuthRequest *) auth : (NSString *) mail : (NSString *) password;  // throws TException
- (void) logout: (NSString *) access_token;  // throws TException
- (User *) user_get: (NSString *) access_token : (int64_t) id : (BOOL) ext_only;  // throws TException
- (void) user_set: (NSString *) access_token : (User *) user;  // throws TException
- (NSArray *) user_list: (NSString *) access_token : (int) type : (int64_t) last_id : (int64_t) num;  // throws TException
- (NSArray *) task_list: (NSString *) access_token : (int) type : (TaskFilter *) filter : (int64_t) last_id : (int64_t) num;  // throws TException
- (Task *) task_get: (NSString *) access_token : (int64_t) id : (BOOL) ext_only;  // throws TException
- (void) task_set: (NSString *) access_token : (Task *) task;  // throws TException
- (int64_t) task_new: (NSString *) access_token : (Task *) task;  // throws TException
- (BOOL) task_apply: (NSString *) access_token : (int64_t) id : (NSString *) txt;  // throws TException
- (BOOL) task_reject: (NSString *) access_token : (int64_t) id;  // throws TException
- (BOOL) task_accept: (NSString *) access_token : (int64_t) id;  // throws TException
- (BOOL) my_task_accept: (NSString *) access_token : (int64_t) task_id : (int64_t) user_id;  // throws TException
- (BOOL) my_task_reject: (NSString *) access_token : (int64_t) task_id : (int64_t) user_id : (NSString *) txt;  // throws TException
- (NSArray *) msg_list: (NSString *) access_token : (int) type : (int64_t) last_id : (int64_t) num;  // throws TException
- (void) msg_send: (NSString *) access_token : (int64_t) send_to : (Msg *) msg;  // throws TException
- (NSArray *) feed: (NSString *) access_token : (int64_t) last_id : (int64_t) num;  // throws TException
- (Summary *) summary: (NSString *) access_token;  // throws TException
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
