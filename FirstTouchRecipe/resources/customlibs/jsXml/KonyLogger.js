var KonyLogger={};
KonyLogger.InitializeLogger=function(){}
KonyLogger.InitializeLogger.prototype.logTrace= function(message){};
KonyLogger.InitializeLogger.prototype.logDebug= function(message){};
KonyLogger.InitializeLogger.prototype.logWarning= function(message){};
KonyLogger.InitializeLogger.prototype.logInfo= function(message){};
KonyLogger.InitializeLogger.prototype.logError= function(message){};
KonyLogger.InitializeLogger.prototype.logFatal= function(message){};
KonyLogger.InitializeLogger.prototype.logPerf= function(message){};

KonyLogger.getLogLevel= function(){};
KonyLogger.flush= function(){};
KonyLogger.setConfig= function(config){};
KonyLogger.setPersistorConfig= function(persistor){};
KonyLogger.setLogLevel= function(logLevel){};
KonyLogger.activatePersistors= function(activatedList){};
KonyLogger.deactivatePersistors= function(deactivatedList){};
KonyLogger.setClaimsToken= function(claimsToken){};
KonyLogger.subscribeLogListener= function(logListener){};
KonyLogger.unsubscribeLogListener= function(){};
KonyLogger.setGlobalRequestParam= function(paramName, paramValue, paramType){};
KonyLogger.removeGlobalRequestParam= function(paramName, paramType){};
KonyLogger.resetGlobalRequestParams= function(){};

