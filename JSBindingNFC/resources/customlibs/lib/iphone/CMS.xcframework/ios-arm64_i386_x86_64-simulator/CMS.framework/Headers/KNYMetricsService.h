//
//  KNYMetricsService.h
//  KNYClient
//
//  Copyright (c) 2014 Kony. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "KNYMetricsServiceConstants.h"

#if ! __has_feature(objc_arc)
#error This file must be compiled with ARC. Either turn on ARC for the project or use -fobjc-arc flag
#endif

/**
 KNYMetricsService
*/
@interface KNYMetricsService : NSObject

- (id)init __attribute__((unavailable("...")));

/**
 userid related to metrics.
 userid length cannot be more than 100.
 */
@property (nonatomic, readwrite) NSString *userId;

/**
 Flow Tag for the metrics events.
 Set to nil to clear previously set flowTag.
 length cannot be more than 256.
 */
@property (nonatomic, readwrite) NSString *flowTag;

/**
 Throws exception, when invoked before initialializing the KNYClient.
 
 @return Returns the shared instance of KNYMetricsService
 */
+ (instancetype)sharedMetricsService;

/**
 Metrics API
 
 @param groupId group id -  groupId length cannot be more than 250.
 @param data    data to be send
 */
- (void)sendCustomMetrics:(NSString *)groupId
                  andData:(NSObject *)data;

/**
  This method will take the required values to set the event Configuration values.
  When eventConfigType is
  - KNYEventConfigTypeBuffer eventBufferAutoFlushCount and eventBufferMaxCount are considered.
  - KNYEventConfigTypeIntant eventBufferAutoFlushCount and eventBufferMaxCount are ignored.

  @param eventConfigType - sets the Current Configuration Type
  @param eventBufferAutoFlushCount - event buffer count to auto flush the events
  								possible values any positive integer
  								Default value 15
  @param eventBufferMaxCount - Maximum event buffer count to store the events
  								possible values any positive integer
  								Default value 1000
 */
    - (void)setEventConfig:(KNYEventConfigType)eventConfigType
 eventBufferAutoFlushCount:(NSUInteger)eventBufferAutoFlushCount
       eventBufferMaxCount:(NSUInteger)eventBufferMaxCount;

/**
  This method will send the buffered events to the server at once.
 */
- (void)flushEvents;

/**
  This method takes the event details from the developer and schedule it for sending to server as per Configuration values set by the developer.
  @param eventType - string literal for formID can be null.
  @param eventSubType - string literal for eventSubType(max 256 Chars)
  @param formID -   string literal for formID(max 256 Chars)
  @param widgetID - string literal for widgetID(max 256 Chars)
  @param flowTag - string literal to override flow tag (max 256 Chars)
 */
- (void)sendEvent:(KNYEventType)eventType
     eventSubType:(NSString *)eventSubType
           formID:(NSString *)formID
         widgetID:(NSString *)widgetID
          flowTag:(NSString *)flowTag;


/**
 This method takes the event details from the developer and schedule it for sending to server as per Configuration values set by the developer.
 @param eventType - string literal for formID can be null.
 @param eventSubType - string literal for eventSubType(max 256 Chars)
 @param formID -   string literal for formID(max 256 Chars)
 @param widgetID - string literal for widgetID(max 256 Chars)
 @param flowTag - string literal to override flow tag (max 256 Chars)
 @param metaData – string literal that can be set by developer while setting a custom event for sending custom data as part of event.
 */
- (void)sendEvent:(KNYEventType)eventType
    eventSubType:(NSString *)eventSubType
          formID:(NSString *)formID
        widgetID:(NSString *)widgetID
         flowTag:(NSString *)flowTag
        metaData:(NSString*)metaData;

/**
 sets the Metrics Service end-point URL
 
 @param URLString   metricservice end-point URL
 @param serviceName metricsServiceName (values = "session", "custom")
 */

- (void)setMetricsServiceEndPoint:(NSString*)URLString
                      serviceName:(NSString*)serviceName __attribute__ ((deprecated));

/**
 * This method will return the a List of the buffered events.
 * @return  returns dictionary of events stored in buffer.
 */

- (NSDictionary*)eventsInBuffer;

/**
 report error to metrics server
 @param errorCode - string errorCode can be nil if not applicable.
 @param errorType - string errorType can be nil if not applicable.
 @param errorMessage - string errorMessage can be nil if not applicable.
 @param errorDetails - string(JSON) errorDetails is a json string that can have key-value pairs for the following keys errfile, errmethod, errline, errstacktrace, errcustommsg, errcrashreport, formID, widgetID, flowTag.
*/

- (void)reportError:(NSString*)errorCode
          errorType:(NSString*)errorType
       errorMessage:(NSString*)errorMessage
       errorDetails:(NSString*)errorDetails;

/**
 report exception to metrics server
 @param exceptionCode - string exceptionCode can be nil if not applicable.
 @param exceptionType - string type of exception. Ex: Eval Error, syntax error. Can be nil if not applicable.
 @param exceptionMessage - string exceptionMessage Can be nil if not applicable.
 @param exceptionDetails - string(JSON) exceptionDetails is a json string that can have key-value pairs for the following keys exceptionfile, exceptionmethod, exceptionline, exceptionstacktrace, formID, widgetID, flowTag.
*/

- (void)reportHandledException:(NSString*)exceptionCode
                 exceptionType:(NSString*)exceptionType
              exceptionMessage:(NSString*)exceptionMessage
              exceptionDetails:(NSString*)exceptionDetails;
/**
 setSessionId is Used only by Kony IDE Dev
 @param sessionId - string literal ex:- any GUID
 */

- (void)setSetSessionId:(NSString *)sessionId;

/**
 setBatchSize method sets the batch size for metrics events batching.
 @param batch - batch size for metrics events batching
 */
- (void)setBatchSize:(int)batch;

/**
 * This method will return kony reporting params.
 * @return  returns dictionary of kony reporting params.
 */
- (NSDictionary *)commonParametersForReporting;

/**
 * This method will shoot IST call after generating session
 */
- (void)captureSessionInfo;
@end
