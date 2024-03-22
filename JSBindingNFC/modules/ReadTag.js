    NdefMessage=java.import('android.nfc.NdefMessage');
    IntentFilter = java.import('android.content.IntentFilter');
	NdefRecord =java.import('android.nfc.NdefRecord');
    KonyMain = java.import('com.konylabs.android.KonyMain');
    context1	=	KonyMain.getActivityContext();
    Intent= java.import('android.content.Intent');
    PackageManager = java.import('android.content.pm.PackageManager');
    Context	=java.import('android.content.Context');
    Handler=java.import('android.os.Handler');
    Service	=java.import('android.app.Service');
    NfcAdapter=java.import('android.nfc.NfcAdapter');
	UnsupportedEncodingException=java.import('java.io.UnsupportedEncodingException');
	Bundle=java.import('android.os.Bundle');
	Ndef=java.import('android.nfc.tech.Ndef');
	Settings=java.import('android.provider.Settings');
	Tag=java.import('android.nfc.Tag');
	PendingIntent=java.import('android.app.PendingIntent');
	URI=java.import('android.net.Uri');
	String=java.import('java.lang.String');
	Arrays=java.import('java.util.Arrays');
	Locale=java.import('java.util.Locale');
	Charset=java.import('java.nio.charset.Charset');
	NfcF=java.import('android.nfc.tech.NfcF');
	StringBuilder=java.import('java.lang.StringBuilder');
	var MIME_TEXT_PLAIN = "text/plain";
    var TAG = "NfcDemo";


function OnCreated() {
    // Intent filter
    var ndefIntent = new IntentFilter(NfcAdapter.ACTION_TAG_DISCOVERED);
    var intentfilter=[];
    intentfilter[0]=ndefIntent;
    var intentfilters=java.newArray('android.content.IntentFilter',intentfilter );
	var activityLifeCycleListener = new MyActivityLifeCycleListener();
    KonyMain.addActivityLifeCycleListener(activityLifeCycleListener);
    
    // Pending Intent
    mPendingIntent = PendingIntent.getActivity(context1, 0,new Intent(context1, context1.getClass()).addFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP), 0);
	kony.print("Pending Intent is"+mPendingIntent);
	adapter.enableForegroundDispatch(context1, mPendingIntent,null, null);
	
	alert("Please bring the NFC tag closer to read");
	
	
   	}
var MyActivityLifeCycleListener = java.newClass('MyActivityLifeCycleListener', 'com.konylabs.ffi.KonyActivityLifeCycleListener',[] , {
   
    onNewIntent : function(Intent) {
        var action = Intent.getAction();
		var tag = Intent.getParcelableExtra(NfcAdapter.EXTRA_TAG);
		var s = action + "\n\n" + tag.toString();
        var data=[];
        var recs=[];
        var payload=[];
		// parse through all NDEF messages and their records and pick text type only
		data = Intent.getParcelableArrayExtra(NfcAdapter.EXTRA_NDEF_MESSAGES);
		if (data != null) {
				for (var i = 0; i < data.length; i++) {					
					recs = (data[i]).getRecords();
					for (var j = 0; j < recs.length; j++) {
						if (recs[j].getTnf() == NdefRecord.TNF_WELL_KNOWN &&
								Arrays.equals(recs[j].getType(), NdefRecord.RTD_TEXT)) {

							payload = recs[j].getPayload();
							var textEncoding = ((payload[0] & 0200) == 0) ? "UTF-8" : "UTF-16";
							var langCodeLen = payload[0] & 0077;

							s += ("\n\nNdefMessage[" + i + "], NdefRecord[" + j + "]:\n\"" +
									new String(payload, langCodeLen + 1,
											payload.length - langCodeLen - 1, textEncoding) +
											"\"");
						}
					}
				}
			} 
  		frmHome.lblTagData.text=s;
		}
    });
