define({
    /*
        This is an auto generated file and any modifications to it may result in corruption of the action sequence.
    */
    AS_AppEvents_PreAppInit: function AS_AppEvents_PreAppInit(eventobject) {
        var self = this;
        voltmx.theme.setCurrentTheme(voltmx.store.getItem('theme') || 'JanusLightTheme', function() {
            return;
        }, function(err) {
            alert("Error setting theme:" + err);
        });
    }
});