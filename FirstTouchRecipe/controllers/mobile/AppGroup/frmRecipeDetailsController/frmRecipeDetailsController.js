/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/

define({ 

  onNavigate: function(data){
    if(!isNullorEmpty(data)){
      this.record = data;
    }
    this.view.preShow = this.onPreShow;
    this.view.postShow = this.onPostShow;
  },
  
  onInit: function() {
    this.toggleAlert(false);
  },
  
  onPreShow: function(){
    this.view.MobileHeader.isImageVisible = true;
    this.view.MobileHeader.headerImgSource = "icon_chevron_left.png";
    this.view.MobileHeader.titleText = "Recipe";
    this.view.MobileHeader.isSearchVisible = false;
    this.view.RecipeDetails.showRecipeDetails(this.record);
  },

  onPostShow: function(){
    const self = this;
    this.view.MobileHeader.onClickHeaderImg = () =>{
      self.navToRecipes(false);
    }
  },
  
  navToEditRecipeForm: function() {
    const record = (this.record && this.record[0]) ? this.record[0].data : null;
    const navRecipeForm = new voltmx.mvc.Navigation("AppGroup/frmRecipeForm"); 
    navRecipeForm.navigate({
      isEdit: true,
      record,
    });
  },

  /**
      * @function : navToRecipes
      * @description : Navigates to RecipesCatalog Form
      * @param : no params
      * @returns {boolean} true/false : no return value
      */
  navToRecipes : function(isCancel){
    let navDetails = new voltmx.mvc.Navigation("frmViewRecipes"); 
    navDetails.navigate({
      isCancel
    });
  },
  
  toggleAlert: function(show) {
    this.view.AlertDialog.setVisibility(show);
  },
  
  onRecipeDeleteClick: function() {
    const record = (this.record && this.record[0]) ? this.record[0].data : null;
    this.view.AlertDialog.setYesBtnText("Delete");
    this.view.AlertDialog.setNoBtnText("Cancel");
    this.view.AlertDialog.setMessage("Are you sure you want to delete this recipe?");
    const self = this;
    const deleteHandler = function() {
      self.toggleAlert(false);
      deleteObject("Recipe", record, (response) => {
        voltmx.print("Record deleted: " + JSON.stringify(response));
        self.navToRecipes(false);
      }, (error) => {
        showError(error.errmsg);
        voltmx.print("Error in record delete: " + JSON.stringify(error));
      });
    };
    this.view.AlertDialog.setYesBtnClickCallback(deleteHandler);
    this.toggleAlert(true);
  },

});