/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define(function(){

  return{
    constructor: function(appConfig){
      this.view.onClick = this.onClickClosePopupDialog;

       this.view.btnNo.onClick = this.onNoBtnClick;
       this.view.btnYes.onClick = this.onYesBtnClick;
    },

    onClickClosePopupDialog: function(){
      this.view.isVisible = false;
      if (this.closeCallback) {
        this.closeCallback();
      }
    },

    onNoBtnClick: function() {
      this.onClickClosePopupDialog();
      if (this.noCallback) {
        this.noCallback();
      }
    },

    onYesBtnClick: function() {
      this.onClickClosePopupDialog();
      if (this.yesCallback) {
        this.yesCallback();
      }
    },

    setMessage: function(message){
      if(message !== undefined && message !== null){
        this.view.richTextMsg.text = message;
      } else {
        this.view.richTextMsg.text = "";
      }

    },

    setYesBtnText: function(text){
      if(text !== undefined && text !== null){
        this.view.btnYes.text = text;
      } else {
        this.view.btnYes.text = "";
      }
    },

    setNoBtnText: function(text){
      if(text !== undefined && text !== null){
        this.view.btnNo.text = text;
      } else {
        this.view.btnNo.text = "";
      }
    },

    setCloseListener: function(callback) {
      this.closeCallback = callback;
    },
    
    setYesBtnClickCallback: function(callback) {
      this.yesCallback = callback;
    },

    setNoBtnClickCallback: function(callback) {
      this.noCallback = callback;
    },
  };

});
