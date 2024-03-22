package com.konylabs.ffi;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Vector;
import com.konylabs.api.TableLib;
import com.konylabs.vm.LuaTable;



import com.kony.binarydatamanager.ffi.BinaryDataFFI;
import com.konylabs.libintf.Library;
import com.konylabs.libintf.JSLibrary;
import com.konylabs.vm.LuaError;
import com.konylabs.vm.LuaNil;


public class N_binarydata extends JSLibrary {

 
 
	public static final String deleteBinaryObject = "deleteBinaryObject";
 
 
	public static final String startDownload = "startDownload";
 
 
	public static final String pauseDownload = "pauseDownload";
 
 
	public static final String resumeDownload = "resumeDownload";
 
 
	public static final String createDownloadTask = "createDownloadTask";
 
 
	public static final String clearBinaryDataManagerState = "clearBinaryDataManagerState";
 
 
	public static final String getBinaryDataFilePath = "getBinaryDataFilePath";
 
 
	public static final String getOnlineBinaryData = "getOnlineBinaryData";
 
 
	public static final String uploadBinaryData = "uploadBinaryData";
 
	String[] methods = { deleteBinaryObject, startDownload, pauseDownload, resumeDownload, createDownloadTask, clearBinaryDataManagerState, getBinaryDataFilePath, getOnlineBinaryData, uploadBinaryData };


 Library libs[] = null;
 public Library[] getClasses() {
 libs = new Library[0];
 return libs;
 }



	public N_binarydata(){
	}

	public Object[] execute(int index, Object[] params) {
		// TODO Auto-generated method stub
		Object[] ret = null;
 
		int paramLen = params.length;
 int inc = 1;
		switch (index) {
 		case 0:
 if (paramLen != 7){ return new Object[] {new Double(100),"Invalid Params"}; }
 java.lang.String dbName0 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 dbName0 = (java.lang.String)params[0];
 }
 java.lang.String tableName0 = null;
 if(params[1] != null && params[1] != LuaNil.nil) {
 tableName0 = (java.lang.String)params[1];
 }
 java.lang.String binaryColumnName0 = null;
 if(params[2] != null && params[2] != LuaNil.nil) {
 binaryColumnName0 = (java.lang.String)params[2];
 }
 com.konylabs.vm.LuaTable primaryKeyTable0 = null;
 if(params[3] != null && params[3] != LuaNil.nil) {
 primaryKeyTable0 = (com.konylabs.vm.LuaTable)params[3];
 }
 com.konylabs.vm.LuaTable options0 = null;
 if(params[4] != null && params[4] != LuaNil.nil) {
 options0 = (com.konylabs.vm.LuaTable)params[4];
 }
 com.konylabs.vm.Function successCallback0 = null;
 if(params[5] != null && params[5] != LuaNil.nil) {
 successCallback0 = (com.konylabs.vm.Function)params[5];
 }
 com.konylabs.vm.Function errorCallback0 = null;
 if(params[6] != null && params[6] != LuaNil.nil) {
 errorCallback0 = (com.konylabs.vm.Function)params[6];
 }
 ret = this.deleteBinaryObject( dbName0, tableName0, binaryColumnName0, primaryKeyTable0, options0, successCallback0, errorCallback0 );
 
 			break;
 		case 1:
 if (paramLen != 3){ return new Object[] {new Double(100),"Invalid Params"}; }
 java.lang.String downloadID1 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 downloadID1 = (java.lang.String)params[0];
 }
 com.konylabs.vm.Function successCallback1 = null;
 if(params[1] != null && params[1] != LuaNil.nil) {
 successCallback1 = (com.konylabs.vm.Function)params[1];
 }
 com.konylabs.vm.Function errorCallback1 = null;
 if(params[2] != null && params[2] != LuaNil.nil) {
 errorCallback1 = (com.konylabs.vm.Function)params[2];
 }
 ret = this.startDownload( downloadID1, successCallback1, errorCallback1 );
 
 			break;
 		case 2:
 if (paramLen != 3){ return new Object[] {new Double(100),"Invalid Params"}; }
 java.lang.String downloadID2 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 downloadID2 = (java.lang.String)params[0];
 }
 com.konylabs.vm.Function successCallback2 = null;
 if(params[1] != null && params[1] != LuaNil.nil) {
 successCallback2 = (com.konylabs.vm.Function)params[1];
 }
 com.konylabs.vm.Function errorCallback2 = null;
 if(params[2] != null && params[2] != LuaNil.nil) {
 errorCallback2 = (com.konylabs.vm.Function)params[2];
 }
 ret = this.pauseDownload( downloadID2, successCallback2, errorCallback2 );
 
 			break;
 		case 3:
 if (paramLen != 3){ return new Object[] {new Double(100),"Invalid Params"}; }
 java.lang.String downloadID3 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 downloadID3 = (java.lang.String)params[0];
 }
 com.konylabs.vm.Function successCallback3 = null;
 if(params[1] != null && params[1] != LuaNil.nil) {
 successCallback3 = (com.konylabs.vm.Function)params[1];
 }
 com.konylabs.vm.Function errorCallback3 = null;
 if(params[2] != null && params[2] != LuaNil.nil) {
 errorCallback3 = (com.konylabs.vm.Function)params[2];
 }
 ret = this.resumeDownload( downloadID3, successCallback3, errorCallback3 );
 
 			break;
 		case 4:
 if (paramLen != 7){ return new Object[] {new Double(100),"Invalid Params"}; }
 java.lang.String databaseName4 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 databaseName4 = (java.lang.String)params[0];
 }
 java.lang.String tableName4 = null;
 if(params[1] != null && params[1] != LuaNil.nil) {
 tableName4 = (java.lang.String)params[1];
 }
 java.lang.String binaryColumnName4 = null;
 if(params[2] != null && params[2] != LuaNil.nil) {
 binaryColumnName4 = (java.lang.String)params[2];
 }
 com.konylabs.vm.LuaTable pkTableObject4 = null;
 if(params[3] != null && params[3] != LuaNil.nil) {
 pkTableObject4 = (com.konylabs.vm.LuaTable)params[3];
 }
 com.konylabs.vm.LuaTable downloadConfigObject4 = null;
 if(params[4] != null && params[4] != LuaNil.nil) {
 downloadConfigObject4 = (com.konylabs.vm.LuaTable)params[4];
 }
 com.konylabs.vm.Function successCallback4 = null;
 if(params[5] != null && params[5] != LuaNil.nil) {
 successCallback4 = (com.konylabs.vm.Function)params[5];
 }
 com.konylabs.vm.Function errorCallback4 = null;
 if(params[6] != null && params[6] != LuaNil.nil) {
 errorCallback4 = (com.konylabs.vm.Function)params[6];
 }
 ret = this.createDownloadTask( databaseName4, tableName4, binaryColumnName4, pkTableObject4, downloadConfigObject4, successCallback4, errorCallback4 );
 
 			break;
 		case 5:
 if (paramLen != 0){ return new Object[] {new Double(100),"Invalid Params"}; }
 ret = this.clearBinaryDataManagerState( );
 
 			break;
 		case 6:
 if (paramLen != 6){ return new Object[] {new Double(100),"Invalid Params"}; }
 java.lang.String databaseName6 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 databaseName6 = (java.lang.String)params[0];
 }
 java.lang.String tableName6 = null;
 if(params[1] != null && params[1] != LuaNil.nil) {
 tableName6 = (java.lang.String)params[1];
 }
 java.lang.String binaryColumnName6 = null;
 if(params[2] != null && params[2] != LuaNil.nil) {
 binaryColumnName6 = (java.lang.String)params[2];
 }
 com.konylabs.vm.LuaTable primaryKeyTable6 = null;
 if(params[3] != null && params[3] != LuaNil.nil) {
 primaryKeyTable6 = (com.konylabs.vm.LuaTable)params[3];
 }
 com.konylabs.vm.Function successCallback6 = null;
 if(params[4] != null && params[4] != LuaNil.nil) {
 successCallback6 = (com.konylabs.vm.Function)params[4];
 }
 com.konylabs.vm.Function errorCallback6 = null;
 if(params[5] != null && params[5] != LuaNil.nil) {
 errorCallback6 = (com.konylabs.vm.Function)params[5];
 }
 ret = this.getBinaryDataFilePath( databaseName6, tableName6, binaryColumnName6, primaryKeyTable6, successCallback6, errorCallback6 );
 
 			break;
 		case 7:
 if (paramLen != 8){ return new Object[] {new Double(100),"Invalid Params"}; }
 com.konylabs.vm.LuaTable fileParams7 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 fileParams7 = (com.konylabs.vm.LuaTable)params[0];
 }
 Boolean streaming7 = null;
 if(params[1] != null && params[1] != LuaNil.nil) {
 streaming7 = (Boolean)params[1];
 }
 com.konylabs.vm.LuaTable downloadConfig7 = null;
 if(params[2] != null && params[2] != LuaNil.nil) {
 downloadConfig7 = (com.konylabs.vm.LuaTable)params[2];
 }
 com.konylabs.vm.Function fileDownloadStartedCallback7 = null;
 if(params[3] != null && params[3] != LuaNil.nil) {
 fileDownloadStartedCallback7 = (com.konylabs.vm.Function)params[3];
 }
 com.konylabs.vm.Function chunkDownloadCompletedCallback7 = null;
 if(params[4] != null && params[4] != LuaNil.nil) {
 chunkDownloadCompletedCallback7 = (com.konylabs.vm.Function)params[4];
 }
 com.konylabs.vm.Function fileDownloadCompletedCallback7 = null;
 if(params[5] != null && params[5] != LuaNil.nil) {
 fileDownloadCompletedCallback7 = (com.konylabs.vm.Function)params[5];
 }
 com.konylabs.vm.Function downloadFailureCallback7 = null;
 if(params[6] != null && params[6] != LuaNil.nil) {
 downloadFailureCallback7 = (com.konylabs.vm.Function)params[6];
 }
 com.konylabs.vm.LuaTable options7 = null;
 if(params[7] != null && params[7] != LuaNil.nil) {
 options7 = (com.konylabs.vm.LuaTable)params[7];
 }
 ret = this.getOnlineBinaryData( fileParams7, streaming7, downloadConfig7, fileDownloadStartedCallback7, chunkDownloadCompletedCallback7, fileDownloadCompletedCallback7, downloadFailureCallback7, options7 );
 
 			break;
 		case 8:
 if (paramLen != 6){ return new Object[] {new Double(100),"Invalid Params"}; }
 com.konylabs.vm.LuaTable uploadParams8 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 uploadParams8 = (com.konylabs.vm.LuaTable)params[0];
 }
 com.konylabs.vm.Function uploadStartedCallback8 = null;
 if(params[1] != null && params[1] != LuaNil.nil) {
 uploadStartedCallback8 = (com.konylabs.vm.Function)params[1];
 }
 com.konylabs.vm.Function uploadChunkCompletedCallback8 = null;
 if(params[2] != null && params[2] != LuaNil.nil) {
 uploadChunkCompletedCallback8 = (com.konylabs.vm.Function)params[2];
 }
 com.konylabs.vm.Function uploadCompletedCallback8 = null;
 if(params[3] != null && params[3] != LuaNil.nil) {
 uploadCompletedCallback8 = (com.konylabs.vm.Function)params[3];
 }
 com.konylabs.vm.Function uploadErrorCallback8 = null;
 if(params[4] != null && params[4] != LuaNil.nil) {
 uploadErrorCallback8 = (com.konylabs.vm.Function)params[4];
 }
 com.konylabs.vm.LuaTable options8 = null;
 if(params[5] != null && params[5] != LuaNil.nil) {
 options8 = (com.konylabs.vm.LuaTable)params[5];
 }
 ret = this.uploadBinaryData( uploadParams8, uploadStartedCallback8, uploadChunkCompletedCallback8, uploadCompletedCallback8, uploadErrorCallback8, options8 );
 
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
		return "binarydata";
	}


	/*
	 * return should be status(0 and !0),address
	 */
 
 
 	public final Object[] deleteBinaryObject( java.lang.String inputKey0, java.lang.String inputKey1, java.lang.String inputKey2, com.konylabs.vm.LuaTable inputKey3, com.konylabs.vm.LuaTable inputKey4, com.konylabs.vm.Function inputKey5, com.konylabs.vm.Function inputKey6 ){
 
		Object[] ret = null;
 com.kony.binarydatamanager.ffi.BinaryDataFFI.deleteBinaryObject( inputKey0
 , inputKey1
 , inputKey2
 , (java.util.Hashtable)TableLib.convertToHash(inputKey3)
 , (java.util.Hashtable)TableLib.convertToHash(inputKey4)
 , (com.konylabs.vm.Function)inputKey5
 , (com.konylabs.vm.Function)inputKey6
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] startDownload( java.lang.String inputKey0, com.konylabs.vm.Function inputKey1, com.konylabs.vm.Function inputKey2 ){
 
		Object[] ret = null;
 com.kony.binarydatamanager.ffi.BinaryDataFFI.startDownload( inputKey0
 , (com.konylabs.vm.Function)inputKey1
 , (com.konylabs.vm.Function)inputKey2
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] pauseDownload( java.lang.String inputKey0, com.konylabs.vm.Function inputKey1, com.konylabs.vm.Function inputKey2 ){
 
		Object[] ret = null;
 com.kony.binarydatamanager.ffi.BinaryDataFFI.pauseDownload( inputKey0
 , (com.konylabs.vm.Function)inputKey1
 , (com.konylabs.vm.Function)inputKey2
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] resumeDownload( java.lang.String inputKey0, com.konylabs.vm.Function inputKey1, com.konylabs.vm.Function inputKey2 ){
 
		Object[] ret = null;
 com.kony.binarydatamanager.ffi.BinaryDataFFI.resumeDownload( inputKey0
 , (com.konylabs.vm.Function)inputKey1
 , (com.konylabs.vm.Function)inputKey2
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] createDownloadTask( java.lang.String inputKey0, java.lang.String inputKey1, java.lang.String inputKey2, com.konylabs.vm.LuaTable inputKey3, com.konylabs.vm.LuaTable inputKey4, com.konylabs.vm.Function inputKey5, com.konylabs.vm.Function inputKey6 ){
 
		Object[] ret = null;
 com.kony.binarydatamanager.ffi.BinaryDataFFI.createTask( inputKey0
 , inputKey1
 , inputKey2
 , (java.util.Hashtable)TableLib.convertToHash(inputKey3)
 , (java.util.Hashtable)TableLib.convertToHash(inputKey4)
 , (com.konylabs.vm.Function)inputKey5
 , (com.konylabs.vm.Function)inputKey6
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] clearBinaryDataManagerState( ){
 
		Object[] ret = null;
 com.kony.binarydatamanager.ffi.BinaryDataFFI.clearBinaryDataManagerState( );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] getBinaryDataFilePath( java.lang.String inputKey0, java.lang.String inputKey1, java.lang.String inputKey2, com.konylabs.vm.LuaTable inputKey3, com.konylabs.vm.Function inputKey4, com.konylabs.vm.Function inputKey5 ){
 
		Object[] ret = null;
 com.kony.binarydatamanager.ffi.BinaryDataFFI.getBinaryDataFilePath( inputKey0
 , inputKey1
 , inputKey2
 , (java.util.Hashtable)TableLib.convertToHash(inputKey3)
 , (com.konylabs.vm.Function)inputKey4
 , (com.konylabs.vm.Function)inputKey5
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] getOnlineBinaryData( com.konylabs.vm.LuaTable inputKey0, Boolean inputKey1, com.konylabs.vm.LuaTable inputKey2, com.konylabs.vm.Function inputKey3, com.konylabs.vm.Function inputKey4, com.konylabs.vm.Function inputKey5, com.konylabs.vm.Function inputKey6, com.konylabs.vm.LuaTable inputKey7 ){
 
		Object[] ret = null;
 com.kony.binarydatamanager.ffi.BinaryDataFFI.getBinaryData( (java.util.Hashtable)TableLib.convertToHash(inputKey0)
 , inputKey1.booleanValue() , (java.util.Hashtable)TableLib.convertToHash(inputKey2)
 , (com.konylabs.vm.Function)inputKey3
 , (com.konylabs.vm.Function)inputKey4
 , (com.konylabs.vm.Function)inputKey5
 , (com.konylabs.vm.Function)inputKey6
 , (java.util.Hashtable)TableLib.convertToHash(inputKey7)
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] uploadBinaryData( com.konylabs.vm.LuaTable inputKey0, com.konylabs.vm.Function inputKey1, com.konylabs.vm.Function inputKey2, com.konylabs.vm.Function inputKey3, com.konylabs.vm.Function inputKey4, com.konylabs.vm.LuaTable inputKey5 ){
 
		Object[] ret = null;
 com.kony.binarydatamanager.ffi.BinaryDataFFI.uploadBinaryData( (java.util.Hashtable)TableLib.convertToHash(inputKey0)
 , (com.konylabs.vm.Function)inputKey1
 , (com.konylabs.vm.Function)inputKey2
 , (com.konylabs.vm.Function)inputKey3
 , (com.konylabs.vm.Function)inputKey4
 , (java.util.Hashtable)TableLib.convertToHash(inputKey5)
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
};
