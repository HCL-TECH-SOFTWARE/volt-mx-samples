function p2kwiet11830495426_frmHome_postshow_seq0(eventobject) {
    adapter = NfcAdapter.getDefaultAdapter(context1);
    if (adapter == null) {
        alert("NFC Not Supported in this Device");
    } else {
        if (!adapter.isEnabled()) {
            alert("Please enable NFC");
            var intent = new Intent(Settings.ACTION_NFC_SETTINGS);
            context1.startActivity(intent);
        }
    }
}