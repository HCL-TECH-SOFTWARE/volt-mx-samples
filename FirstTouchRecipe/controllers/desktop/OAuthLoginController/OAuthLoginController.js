/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define({
  
  onNavigate: function(context) {
    const self = this;
    if(context && context.disableSSOCheck) {
      self.view.OAuthLoginForm.setVisibility(true);
    } else {
      this.view.OAuthLoginForm.checkSSO(()=>{
        self.view.OAuthLoginForm.setVisibility(true);
      });
    }
  }
});
