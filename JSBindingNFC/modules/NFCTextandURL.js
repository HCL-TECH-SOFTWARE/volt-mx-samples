    NdefMessage=java.import('android.nfc.NdefMessage');
	NdefRecord =java.import('android.nfc.NdefRecord');
    KonyMain = java.import('com.konylabs.android.KonyMain');
    context1	=	KonyMain.getActivityContext();
    Intent= java.import('android.content.Intent');
    Context	=java.import('android.content.Context');
    NfcAdapter=java.import('android.nfc.NfcAdapter');
	Ndef=java.import('android.nfc.tech.Ndef');
	Tag=java.import('android.nfc.Tag');
	Uri=java.import('android.net.Uri');
	File=java.import('java.io.File');
    
var newclass1 = java.newClass('newclass1', 'java.lang.Object',['android.nfc.NfcAdapter$OnNdefPushCompleteCallback'] , {
        onNdefPushComplete: function(test) {
        kony.print("NDEF Push Completed  "+test )
        }
    });
    
var newclass2 = java.newClass('newclass2', 'java.lang.Object',['android.nfc.NfcAdapter$CreateNdefMessageCallback'] , {
        createNdefMessage: function(event) {
        kony.print("NDEF Message  Completed  "+event )
        adapter = NfcAdapter.getDefaultAdapter(context1);
        var mes1=createndefmessage();
        adapter.enableForegroundNdefPush(context1,mes1);
        return mes1;
        }
    });

//Function to send NFC Text
function ValidateNFCText() {
	alert("Please bring second device closer to beam");
    var mes1=createndefmessage();
    adapter.enableForegroundNdefPush(context1,mes1);
}

//Function to make NFC Text object
function createndefmessage()
{
	//message is hardcoded. Please change according to your requirement
	var m1=NdefRecord.createTextRecord ("en","First sample NDEF text record");
	var m2=NdefRecord.createTextRecord ("en","Second sample NDEF text record");
	var jsNdefArray = [];
	jsNdefArray[0] = m1;
	jsNdefArray[1] = m2;
	var data = java.newArray('android.nfc.NdefRecord', jsNdefArray);
	mNdefMessage = new NdefMessage(data);	
	return mNdefMessage;
}

//Function to make NFC Text object
function createndefuri()
{       
//file is hardcoded. Please change according to File available in your device
	var transferFile = "lta.pdf";
    var pathoffile = "/sdcard/beam/"
    var externalFile = new File(pathoffile, transferFile);
    externalFile.setReadable(true, false);
    var external = Uri.fromFile(externalFile);
    kony.print("File url is"+external);
    var uriArray = [];
    uriArray[0]=external;
	var uridata = java.newArray('android.net.Uri', uriArray);
    return uridata
}

//Function to send NFC URL/File
function ValidateNFCUri() {			
			alert("Please bring second device closer to beam");
           var mes1=createndefuri();
           adapter.setBeamPushUris(mes1,context1);
   }
   
