/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define({

 //Type your controller code here 
  onRecipeImageClick: function(context) {
      let navDetails = new voltmx.mvc.Navigation("frmRecipeDetails");
      navDetails.navigate([context.widgetInfo.data[context.rowIndex]]);
  },

 });