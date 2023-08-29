package com.konylabs.ffi;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Vector;
import com.konylabs.api.TableLib;
import com.konylabs.vm.LuaTable;



import com.kony.logger.Core.KonyJSFacade;
import com.konylabs.libintf.Library;
import com.konylabs.libintf.JSLibrary;
import com.konylabs.vm.LuaError;
import com.konylabs.vm.LuaNil;


public class N_KonyLogger extends JSLibrary {

 
 
	public static final String getLogLevel = "getLogLevel";
 
 
	public static final String flush = "flush";
 
 
	public static final String setConfig = "setConfig";
 
 
	public static final String setPersistorConfig = "setPersistorConfig";
 
 
	public static final String setLogLevel = "setLogLevel";
 
 
	public static final String activatePersistors = "activatePersistors";
 
 
	public static final String deactivatePersistors = "deactivatePersistors";
 
 
	public static final String setClaimsToken = "setClaimsToken";

	public static final String subscribeLogListener = "subscribeLogListener";
 
	public static final String unsubscribeLogListener = "unsubscribeLogListener";
	
	public static final String setGlobalRequestParam = "setGlobalRequestParam";
	
	public static final String removeGlobalRequestParam = "removeGlobalRequestParam";
	
	public static final String resetGlobalRequestParams = "resetGlobalRequestParams";
 
	String[] methods = { getLogLevel, flush, setConfig, setPersistorConfig, setLogLevel, activatePersistors, deactivatePersistors, setClaimsToken, subscribeLogListener, unsubscribeLogListener, 
	setGlobalRequestParam, removeGlobalRequestParam, resetGlobalRequestParams};


 Library libs[] = null;
 public Library[] getClasses() {
 libs = new Library[1];
 libs[0] = new InitializeLogger();
 return libs;
 }



	public N_KonyLogger(){
	}

	public Object[] execute(int index, Object[] params) {
		// TODO Auto-generated method stub
		Object[] ret = null;
 
		int paramLen = params.length;
 int inc = 1;
		switch (index) {
 		case 0:
 if (paramLen != 0){ return new Object[] {new Double(100),"Invalid Params"}; }
 ret = this.getLogLevel( );
 
 			break;
 		case 1:
 if (paramLen != 0){ return new Object[] {new Double(100),"Invalid Params"}; }
 ret = this.flush( );
 
 			break;
 		case 2:
 if (paramLen != 1){ return new Object[] {new Double(100),"Invalid Params"}; }
 com.konylabs.vm.LuaTable config2 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 config2 = (com.konylabs.vm.LuaTable)params[0];
 }
 ret = this.setConfig( config2 );
 
 			break;
 		case 3:
 if (paramLen != 1){ return new Object[] {new Double(100),"Invalid Params"}; }
 com.konylabs.vm.LuaTable persistor3 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 persistor3 = (com.konylabs.vm.LuaTable)params[0];
 }
 ret = this.setPersistorConfig( persistor3 );
 
 			break;
 		case 4:
 if (paramLen != 1){ return new Object[] {new Double(100),"Invalid Params"}; }
 Double logLevel4 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 logLevel4 = (Double)params[0];
 }
 ret = this.setLogLevel( logLevel4 );
 
 			break;
 		case 5:
 if (paramLen != 1){ return new Object[] {new Double(100),"Invalid Params"}; }
 Double activatedList5 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 activatedList5 = (Double)params[0];
 }
 ret = this.activatePersistors( activatedList5 );
 
 			break;
 		case 6:
 if (paramLen != 1){ return new Object[] {new Double(100),"Invalid Params"}; }
 Double deactivatedList6 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 deactivatedList6 = (Double)params[0];
 }
 ret = this.deactivatePersistors( deactivatedList6 );
 
 			break;
 		case 7:
 if (paramLen != 1){ return new Object[] {new Double(100),"Invalid Params"}; }
 java.lang.String claimsToken7 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 claimsToken7 = (java.lang.String)params[0];
 }
 ret = this.setClaimsToken( claimsToken7 );
 
 			break;
 		case 8:
 if (paramLen != 1){ return new Object[] {new Double(100),"Invalid Params"}; }
 com.konylabs.vm.Function logListener0 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 logListener0 = (com.konylabs.vm.Function)params[0];
 }
 ret = this.subscribeLogListener( logListener0 );
 			break;
 		case 9:
 if (paramLen != 0){ return new Object[] {new Double(100),"Invalid Params"}; }
 ret = this.unsubscribeLogListener( );
 
 			break;
		case 10:
		 if (paramLen != 3){ return new Object[] {new Double(100),"Invalid Params"}; }
 java.lang.String paramName10 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 paramName10 = (java.lang.String)params[0];
 }
 java.lang.String paramValue10 = null;
 if(params[1] != null && params[1] != LuaNil.nil) {
 paramValue10 = (java.lang.String)params[1];
 }
 java.lang.String paramType10 = null;
 if(params[2] != null && params[2] != LuaNil.nil) {
 paramType10 = (java.lang.String)params[2];
 }
 ret = this.setGlobalRequestParam( paramName10, paramValue10, paramType10 );
			break;
		case 11:
		 if (paramLen != 2){ return new Object[] {new Double(100),"Invalid Params"}; }
 java.lang.String paramName11 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 paramName11 = (java.lang.String)params[0];
 }
 java.lang.String paramType11 = null;
 if(params[1] != null && params[1] != LuaNil.nil) {
 paramType11 = (java.lang.String)params[1];
 }
 ret = this.removeGlobalRequestParam( paramName11, paramType11 );
			break;
		case 12:
 if (paramLen != 0){ return new Object[] {new Double(100),"Invalid Params"}; }
 ret = this.resetGlobalRequestParams( );
			break;			
 		default:
			break;
		}
 
		return ret;
	}

	public String[] getMethods() {
		// TODO Auto-generated method stub
		return methods;
	}
	public String getNameSpace() {
		// TODO Auto-generated method stub
		return "KonyLogger";
	}


	/*
	 * return should be status(0 and !0),address
	 */
 
 
 	public final Object[] getLogLevel( ){
 
		Object[] ret = null;
 Double val = new Double(com.kony.logger.Core.KonyJSFacade.getLogLevel( ));
 
 			ret = new Object[]{val, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] flush( ){
 
		Object[] ret = null;
 com.kony.logger.Core.KonyJSFacade.flush( );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] setConfig( com.konylabs.vm.LuaTable inputKey0 ){
 
		Object[] ret = null;
 com.kony.logger.Core.KonyJSFacade.setConfig( (java.util.Hashtable)TableLib.convertToHash(inputKey0)
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] setPersistorConfig( com.konylabs.vm.LuaTable inputKey0 ){
 
		Object[] ret = null;
 com.kony.logger.Core.KonyJSFacade.setPersisterConfig( (java.util.Hashtable)TableLib.convertToHash(inputKey0)
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] setLogLevel( Double inputKey0 ){
 
		Object[] ret = null;
 com.kony.logger.Core.KonyJSFacade.setLogLevel( inputKey0.intValue() );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] activatePersistors( Double inputKey0 ){
 
		Object[] ret = null;
 com.kony.logger.Core.KonyJSFacade.activatePersistors( inputKey0.intValue() );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] deactivatePersistors( Double inputKey0 ){
 
		Object[] ret = null;
 com.kony.logger.Core.KonyJSFacade.deactivatePersistors( inputKey0.intValue() );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] setClaimsToken( java.lang.String inputKey0 ){
 
		Object[] ret = null;
 com.kony.logger.Core.KonyJSFacade.setClaimsToken( inputKey0
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
	
 	public final Object[] subscribeLogListener( com.konylabs.vm.Function inputKey0 ){
 
		Object[] ret = null;
 com.kony.logger.Core.KonyJSFacade.subscribeLogListener( (com.konylabs.vm.Function)inputKey0
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] unsubscribeLogListener( ){
 
		Object[] ret = null;
 com.kony.logger.Core.KonyJSFacade.unsubscribeLogListener( );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 

	public final Object[] setGlobalRequestParam( java.lang.String inputKey0, java.lang.String inputKey1, java.lang.String inputKey2 ){
 
		Object[] ret = null;
	com.kony.logger.Core.KonyJSFacade.setGlobalRequestParam( inputKey0
	, inputKey1
	, inputKey2
	);
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
	
	
	public final Object[] removeGlobalRequestParam( java.lang.String inputKey0, java.lang.String inputKey1 ){
 
		Object[] ret = null;
	com.kony.logger.Core.KonyJSFacade.removeGlobalRequestParam( inputKey0
	, inputKey1
	);
	 
	 ret = new Object[]{LuaNil.nil, new Double(0)};
			return ret;
	}
	
	
	public final Object[] resetGlobalRequestParams( ){
 
				Object[] ret = null;
	 com.kony.logger.Core.KonyJSFacade.resetGlobalRequestParams( );
	 
	 ret = new Object[]{LuaNil.nil, new Double(0)};
			return ret;
	}

class InitializeLogger extends JSLibrary {

 
 
	public static final String logTrace = "logTrace";
 
 
	public static final String logDebug = "logDebug";
 
 
	public static final String logWarning = "logWarning";
 
 
	public static final String logInfo = "logInfo";
 
 
	public static final String logError = "logError";
 
 
	public static final String logFatal = "logFatal";
 
 
	public static final String logPerf = "logPerf";
 
	String[] methods = { logTrace, logDebug, logWarning, logInfo, logError, logFatal, logPerf };

	public Object createInstance(final Object[] params) {
 return new com.kony.logger.Core.KonyJSFacade(
 (java.lang.String)params[0] );
 }


	public Object[] execute(int index, Object[] params) {
		// TODO Auto-generated method stub
		Object[] ret = null;
 
		int paramLen = params.length;
 int inc = 1;
		switch (index) {
 		case 0:
 if (paramLen < 1 || paramLen > 2){ return new Object[] {new Double(100),"Invalid Params"};}
 inc = 1;
 
 com.konylabs.vm.LuaTable message0 = null;
 if(params[0+inc] != null && params[0+inc] != LuaNil.nil) {
 message0 = (com.konylabs.vm.LuaTable)params[0+inc];
 }
 ret = this.logTrace(params[0]
 ,message0
 );
 
 			break;
 		case 1:
 if (paramLen < 1 || paramLen > 2){ return new Object[] {new Double(100),"Invalid Params"};}
 inc = 1;
 
 com.konylabs.vm.LuaTable message1 = null;
 if(params[0+inc] != null && params[0+inc] != LuaNil.nil) {
 message1 = (com.konylabs.vm.LuaTable)params[0+inc];
 }
 ret = this.logDebug(params[0]
 ,message1
 );
 
 			break;
 		case 2:
 if (paramLen < 1 || paramLen > 2){ return new Object[] {new Double(100),"Invalid Params"};}
 inc = 1;
 
 com.konylabs.vm.LuaTable message2 = null;
 if(params[0+inc] != null && params[0+inc] != LuaNil.nil) {
 message2 = (com.konylabs.vm.LuaTable)params[0+inc];
 }
 ret = this.logWarning(params[0]
 ,message2
 );
 
 			break;
 		case 3:
 if (paramLen < 1 || paramLen > 2){ return new Object[] {new Double(100),"Invalid Params"};}
 inc = 1;
 
 com.konylabs.vm.LuaTable message3 = null;
 if(params[0+inc] != null && params[0+inc] != LuaNil.nil) {
 message3 = (com.konylabs.vm.LuaTable)params[0+inc];
 }
 ret = this.logInfo(params[0]
 ,message3
 );
 
 			break;
 		case 4:
 if (paramLen < 1 || paramLen > 2){ return new Object[] {new Double(100),"Invalid Params"};}
 inc = 1;
 
 com.konylabs.vm.LuaTable message4 = null;
 if(params[0+inc] != null && params[0+inc] != LuaNil.nil) {
 message4 = (com.konylabs.vm.LuaTable)params[0+inc];
 }
 ret = this.logError(params[0]
 ,message4
 );
 
 			break;
 		case 5:
 if (paramLen < 1 || paramLen > 2){ return new Object[] {new Double(100),"Invalid Params"};}
 inc = 1;
 
 com.konylabs.vm.LuaTable message5 = null;
 if(params[0+inc] != null && params[0+inc] != LuaNil.nil) {
 message5 = (com.konylabs.vm.LuaTable)params[0+inc];
 }
 ret = this.logFatal(params[0]
 ,message5
 );
 
 			break;
 		case 6:
 if (paramLen < 1 || paramLen > 2){ return new Object[] {new Double(100),"Invalid Params"};}
 inc = 1;
 
 com.konylabs.vm.LuaTable message6 = null;
 if(params[0+inc] != null && params[0+inc] != LuaNil.nil) {
 message6 = (com.konylabs.vm.LuaTable)params[0+inc];
 }
 ret = this.logPerf(params[0]
 ,message6
 );
 
 			break;
 		default:
			break;
		}
 
		return ret;
	}

	public String[] getMethods() {
		// TODO Auto-generated method stub
		return methods;
	}
	public String getNameSpace() {
		// TODO Auto-generated method stub
		return "InitializeLogger";
	}

	/*
	 * return should be status(0 and !0),address
	 */
 
 
 	public final Object[] logTrace( Object self ,com.konylabs.vm.LuaTable inputKey0
 ){
 
		Object[] ret = null;
 ((com.kony.logger.Core.KonyJSFacade)self).logTrace( (java.util.Hashtable)TableLib.convertToHash(inputKey0)
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] logDebug( Object self ,com.konylabs.vm.LuaTable inputKey0
 ){
 
		Object[] ret = null;
 ((com.kony.logger.Core.KonyJSFacade)self).logDebug( (java.util.Hashtable)TableLib.convertToHash(inputKey0)
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] logWarning( Object self ,com.konylabs.vm.LuaTable inputKey0
 ){
 
		Object[] ret = null;
 ((com.kony.logger.Core.KonyJSFacade)self).logWarning( (java.util.Hashtable)TableLib.convertToHash(inputKey0)
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] logInfo( Object self ,com.konylabs.vm.LuaTable inputKey0
 ){
 
		Object[] ret = null;
 ((com.kony.logger.Core.KonyJSFacade)self).logInfo( (java.util.Hashtable)TableLib.convertToHash(inputKey0)
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] logError( Object self ,com.konylabs.vm.LuaTable inputKey0
 ){
 
		Object[] ret = null;
 ((com.kony.logger.Core.KonyJSFacade)self).logError( (java.util.Hashtable)TableLib.convertToHash(inputKey0)
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] logFatal( Object self ,com.konylabs.vm.LuaTable inputKey0
 ){
 
		Object[] ret = null;
 ((com.kony.logger.Core.KonyJSFacade)self).logFatal( (java.util.Hashtable)TableLib.convertToHash(inputKey0)
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] logPerf( Object self ,com.konylabs.vm.LuaTable inputKey0
 ){
 
		Object[] ret = null;
 ((com.kony.logger.Core.KonyJSFacade)self).logPerf( (java.util.Hashtable)TableLib.convertToHash(inputKey0)
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
}

};
