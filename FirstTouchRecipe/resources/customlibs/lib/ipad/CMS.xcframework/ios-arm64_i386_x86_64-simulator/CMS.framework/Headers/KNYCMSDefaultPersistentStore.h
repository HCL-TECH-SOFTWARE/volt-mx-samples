/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
//
//  KNYCMSDefaultPersistentStore.h
//  Metrics
//
//  Created by Mukesh Sharma on 29/01/18.

#import <Foundation/Foundation.h>

@interface KNYCMSDefaultPersistentStore : NSObject

+ (instancetype)sharedPersistentStore;

- (void)storeItem:(NSString *)item forKey:(NSString *)key;
- (NSString *)getItemForKey:(NSString *)key;
- (void)removeItemForKey:(NSString *)key;
- (void)storeMapItem:(NSDictionary *)item forKey:(NSString *)key;
- (NSDictionary *)getMapItemForKey:(NSString *)key;

- (void)storeDataItem:(id)item forKey:(NSString *)key;
- (id)getDataItemForKey:(NSString *)key;

@end
