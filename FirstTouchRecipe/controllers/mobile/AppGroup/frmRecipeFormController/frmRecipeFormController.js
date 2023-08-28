/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define({

  onNavigate: function(context) {
    this.view.RecipeForm.isEdit = context.isEdit;
    this.view.RecipeForm.record = context.record;
    
    this.view.MobileHeader.titleText = context.isEdit ? "Edit Recipe" : "Add Recipe";
    this.view.MobileHeader.isImageVisible = true;
    this.view.MobileHeader.headerImgSource = "icon_chevron_left.png";
    
    this.view.FooterButtons.BtnSubmitText = context.isEdit ? "Update" : "Save";

    this.view.RecipeForm.saveSuccess = this.saveSuccess;
    this.view.RecipeForm.saveCancel = this.saveCancel;
  },
  
  onPostShow: function() {
    this.view.MobileHeader.onClickHeaderImg = this.saveSuccess;
  },
  
  onSaveClick: function() {
    this.view.RecipeForm.saveRecipe();
  },
  
  onCancelClick: function() {
    this.saveCancel();
  },

  saveSuccess: function() {
    this.navToMain(false);
  },

  saveCancel: function() {
    this.navToMain(true);
  },
  
  navToMain: function(isCancel) {
    const navDetails = new voltmx.mvc.Navigation("AppGroup/frmViewRecipes"); 
    navDetails.navigate({
      isCancel,
    });
  }
 });