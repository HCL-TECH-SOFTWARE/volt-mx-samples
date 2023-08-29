var WindowsOfflineObjects={};
WindowsOfflineObjects.OfflineSDKObject=function(){}
WindowsOfflineObjects.OfflineSDKObject.prototype.create= function(sdkObjectName,record,options,successCallback,failureCallback){};
WindowsOfflineObjects.OfflineSDKObject.prototype.updateByPK= function(sdkObjectName,record,options,successCallback,failureCallback){};
WindowsOfflineObjects.OfflineSDKObject.prototype.get= function(sdkObjectName,options,successCallback,failureCallback){};
WindowsOfflineObjects.OfflineSDKObject.prototype.deleteByPK= function(sdkObjectName,options,successCallback,failureCallback){};
WindowsOfflineObjects.OfflineSDKObject.prototype.startSync= function(sdkObjectName,options,successCallback,failureCallback,progressCallback){};
WindowsOfflineObjects.OfflineSDKObject.prototype.rollback= function(sdkObjectName,primaryKeyValueMap,successCallback,failureCallback){};

WindowsOfflineObjects.OfflineSDKObjectService=function(){}
WindowsOfflineObjects.OfflineSDKObjectService.prototype.startSync= function(sdkObjectServiceName,options,successCallback,failureCallback,progressCallback){};
WindowsOfflineObjects.OfflineSDKObjectService.prototype.rollback= function(sdkObjectServiceName,successCallback,failureCallback){};

WindowsOfflineObjects.setToken= function(token){};
WindowsOfflineObjects.setup= function(objServiceList,options,successCallback,failureCallback){};
WindowsOfflineObjects.drop= function(options,successCallback,failureCallback){};
WindowsOfflineObjects.rollback= function(successCallback,failureCallback){};
WindowsOfflineObjects.reset= function(objServiceList,options,successCallback,failureCallback){};
