/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define(function() {

	return{
    constructor: function(appConfig){
      this.view.preShow = this.onPreShowFooterBar;
    },

    onPreShowFooterBar: function(){
      this.view.flxFooter.lblVersion.text = appConfig.appVersion;
    }
  };

});
