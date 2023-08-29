/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define(function(){

  return{
    constructor: function(appConfig){
      this.view.onClick = this.onClickCloseAboutBox;
      this.view.preShow = this.onPreShowAboutBox;
    },

    onClickCloseAboutBox: function(){
      this.view.isVisible = false;
    },

    onPreShowAboutBox: function(){
      this.view.lblRuntimeAppVersion.text = appConfig.runtimeAppVersion;
      this.view.lblClientAppVersion.text = appConfig.appVersion;
      this.view.lblAppId.text = appConfig.appId;
      this.view.lblAppKey.text = appConfig.appKey;
      this.view.lblIsDebug.setVisibility(!!appConfig.isDebug);
    }
  };

});
