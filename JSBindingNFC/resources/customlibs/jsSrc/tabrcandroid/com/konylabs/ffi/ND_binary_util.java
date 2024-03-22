package com.konylabs.ffi;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Vector;
import com.konylabs.api.TableLib;
import com.konylabs.vm.LuaTable;



import com.kony.binary.utility.BlobStoreUtil;
import com.kony.binary.utility.PollingUtility;
import com.kony.binary.utility.DownloadUtil;
import com.konylabs.libintf.Library;
import com.konylabs.libintf.JSLibrary;
import com.konylabs.vm.LuaError;
import com.konylabs.vm.LuaNil;


public class ND_binary_util extends JSLibrary {

 
 
	public static final String renameFile = "renameFile";
 
 
	public static final String saveBase64File = "saveBase64File";
 
 
	public static final String decodeBase64File = "decodeBase64File";
 
 
	public static final String getBase64FromFile = "getBase64FromFile";
 
 
	public static final String deleteBlobFile = "deleteBlobFile";
 
 
	public static final String getBase64FromFiles = "getBase64FromFiles";
 
 
	public static final String deleteAllBinaryFiles = "deleteAllBinaryFiles";
 
 
	public static final String createBlobsDir = "createBlobsDir";
 
 
	public static final String notifyToPrepareJobs = "notifyToPrepareJobs";
 
 
	public static final String notifyToProcessJobs = "notifyToProcessJobs";
 
 
	public static final String binaryThreadInit = "binaryThreadInit";
 
	String[] methods = { renameFile, saveBase64File, decodeBase64File, getBase64FromFile, deleteBlobFile, getBase64FromFiles, deleteAllBinaryFiles, createBlobsDir, notifyToPrepareJobs, notifyToProcessJobs, binaryThreadInit };


 Library libs[] = null;
 public Library[] getClasses() {
 libs = new Library[0];
 return libs;
 }



	public ND_binary_util(){
	}

	public Object[] execute(int index, Object[] params) {
		// TODO Auto-generated method stub
		Object[] ret = null;
 
		int paramLen = params.length;
 int inc = 1;
		switch (index) {
 		case 0:
 if (paramLen != 2){ return new Object[] {new Double(100),"Invalid Params"}; }
 java.lang.String tempFilePath0 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 tempFilePath0 = (java.lang.String)params[0];
 }
 java.lang.String filePath0 = null;
 if(params[1] != null && params[1] != LuaNil.nil) {
 filePath0 = (java.lang.String)params[1];
 }
 ret = this.renameFile( tempFilePath0, filePath0 );
 
 			break;
 		case 1:
 if (paramLen != 2){ return new Object[] {new Double(100),"Invalid Params"}; }
 java.lang.String fileName1 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 fileName1 = (java.lang.String)params[0];
 }
 java.lang.String base641 = null;
 if(params[1] != null && params[1] != LuaNil.nil) {
 base641 = (java.lang.String)params[1];
 }
 ret = this.saveBase64File( fileName1, base641 );
 
 			break;
 		case 2:
 if (paramLen != 1){ return new Object[] {new Double(100),"Invalid Params"}; }
 java.lang.String base64FilePath2 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 base64FilePath2 = (java.lang.String)params[0];
 }
 ret = this.decodeBase64File( base64FilePath2 );
 
 			break;
 		case 3:
 if (paramLen != 1){ return new Object[] {new Double(100),"Invalid Params"}; }
 java.lang.String filePath3 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 filePath3 = (java.lang.String)params[0];
 }
 ret = this.getBase64FromFile( filePath3 );
 
 			break;
 		case 4:
 if (paramLen != 1){ return new Object[] {new Double(100),"Invalid Params"}; }
 java.lang.String base64FilePath4 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 base64FilePath4 = (java.lang.String)params[0];
 }
 ret = this.deleteBlobFile( base64FilePath4 );
 
 			break;
 		case 5:
 if (paramLen != 1){ return new Object[] {new Double(100),"Invalid Params"}; }
 com.konylabs.vm.LuaTable filePaths5 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 filePaths5 = (com.konylabs.vm.LuaTable)params[0];
 }
 ret = this.getBase64FromFiles( filePaths5 );
 
 			break;
 		case 6:
 if (paramLen != 0){ return new Object[] {new Double(100),"Invalid Params"}; }
 ret = this.deleteAllBinaryFiles( );
 
 			break;
 		case 7:
 if (paramLen != 0){ return new Object[] {new Double(100),"Invalid Params"}; }
 ret = this.createBlobsDir( );
 
 			break;
 		case 8:
 if (paramLen != 0){ return new Object[] {new Double(100),"Invalid Params"}; }
 ret = this.notifyToPrepareJobs( );
 
 			break;
 		case 9:
 if (paramLen != 0){ return new Object[] {new Double(100),"Invalid Params"}; }
 ret = this.notifyToProcessJobs( );
 
 			break;
 		case 10:
 if (paramLen != 4){ return new Object[] {new Double(100),"Invalid Params"}; }
 com.konylabs.vm.Function prepareJobs10 = null;
 if(params[0] != null && params[0] != LuaNil.nil) {
 prepareJobs10 = (com.konylabs.vm.Function)params[0];
 }
 com.konylabs.vm.Function getPrepareJobs10 = null;
 if(params[1] != null && params[1] != LuaNil.nil) {
 getPrepareJobs10 = (com.konylabs.vm.Function)params[1];
 }
 com.konylabs.vm.Function succCallback10 = null;
 if(params[2] != null && params[2] != LuaNil.nil) {
 succCallback10 = (com.konylabs.vm.Function)params[2];
 }
 com.konylabs.vm.Function errCallback10 = null;
 if(params[3] != null && params[3] != LuaNil.nil) {
 errCallback10 = (com.konylabs.vm.Function)params[3];
 }
 ret = this.binaryThreadInit( prepareJobs10, getPrepareJobs10, succCallback10, errCallback10 );
 
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
		return "binary.util";
	}


	/*
	 * return should be status(0 and !0),address
	 */
 
 
 	public final Object[] renameFile( java.lang.String inputKey0, java.lang.String inputKey1 ){
 
		Object[] ret = null;
 Boolean val = new Boolean(com.kony.binary.utility.BlobStoreUtil.renameFile( inputKey0
 , inputKey1
 ));
 
 			ret = new Object[]{val, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] saveBase64File( java.lang.String inputKey0, java.lang.String inputKey1 ){
 
		Object[] ret = null;
 java.lang.String val = com.kony.binary.utility.BlobStoreUtil.saveBase64File( inputKey0
 , inputKey1
 );
 
 			ret = new Object[]{val, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] decodeBase64File( java.lang.String inputKey0 ){
 
		Object[] ret = null;
 java.lang.String val = com.kony.binary.utility.BlobStoreUtil.decodeBase64File( inputKey0
 );
 
 			ret = new Object[]{val, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] getBase64FromFile( java.lang.String inputKey0 ){
 
		Object[] ret = null;
 java.lang.String val = com.kony.binary.utility.BlobStoreUtil.getBase64FromFile( inputKey0
 );
 
 			ret = new Object[]{val, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] deleteBlobFile( java.lang.String inputKey0 ){
 
		Object[] ret = null;
 Boolean val = new Boolean(com.kony.binary.utility.BlobStoreUtil.deleteBlobFile( inputKey0
 ));
 
 			ret = new Object[]{val, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] getBase64FromFiles( com.konylabs.vm.LuaTable inputKey0 ){
 
		Object[] ret = null;
 java.util.Vector retval = com.kony.binary.utility.BlobStoreUtil.getBase64FromFiles( (java.util.Vector)TableLib.convertToList(inputKey0)
 );
 LuaTable val = TableLib.convertToLuaTable(retval);
 
 			ret = new Object[]{val, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] deleteAllBinaryFiles( ){
 
		Object[] ret = null;
 Boolean val = new Boolean(com.kony.binary.utility.BlobStoreUtil.deleteAllBinaryFiles( ));
 
 			ret = new Object[]{val, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] createBlobsDir( ){
 
		Object[] ret = null;
 com.kony.binary.utility.BlobStoreUtil.createBlobsDir( );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] notifyToPrepareJobs( ){
 
		Object[] ret = null;
 com.kony.binary.utility.PollingUtility.notifyToPrepareJobs( );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] notifyToProcessJobs( ){
 
		Object[] ret = null;
 com.kony.binary.utility.PollingUtility.notifyToProcessJobs( );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
 
 	public final Object[] binaryThreadInit( com.konylabs.vm.Function inputKey0, com.konylabs.vm.Function inputKey1, com.konylabs.vm.Function inputKey2, com.konylabs.vm.Function inputKey3 ){
 
		Object[] ret = null;
 com.kony.binary.utility.DownloadUtil.binaryThreadInit( (com.konylabs.vm.Function)inputKey0
 , (com.konylabs.vm.Function)inputKey1
 , (com.konylabs.vm.Function)inputKey2
 , (com.konylabs.vm.Function)inputKey3
 );
 
 ret = new Object[]{LuaNil.nil, new Double(0)};
 		return ret;
	}
 
};
