/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/

define({ 

  onNavigate: function(context){
    if (context && context.loginContext) {
      GlobalState.loginContext = context.loginContext;
    }
    GlobalState.isCancel = context.isCancel;
    this.view.preShow = this.onPreShow;
  },

  onInit: function() {
    this.toggleAlertContainer(false);
    this.view.RecipeList.onDeleteClick = this.onRecipeDeleteClick.bind(this);
    this.view.AlertDialog.setCloseListener(this.onAlertDialogClose.bind(this));
  },

  onPreShow: function(){
    this.view.MobileHeader.isSearchVisible = true;
    this.view.MobileHeader.onSearchTextChange = this.searchRecipeCatalog; 
    if(GlobalState.isCancel === true){
      // do nothing
    }else{
      this.view.RecipeList.segRecipeRemoveAll();
      this.view.RecipeList.lblSuggestedText = "";
      this.refreshRecipeList();
    }
  },

  toggleAlertContainer: function(show) {
    this.view.flxViewRecipe.flxAlertContainer.setVisibility(show);
    this.view.AlertDialog.setVisibility(show);
  },

  onAlertDialogClose: function() {
    this.toggleAlertContainer(false);
  },

  refreshRecipeList: function() {
    voltmx.model.ApplicationContext.showLoadingScreen('Loading...');
    getObject(JAC.APPLICATION_OBJECT, "", this.getListsSuccessCallback, this.getListsFailureCallback);
  },

  getListsSuccessCallback: function(response){
    voltmx.application.dismissLoadingScreen();
    this.getImagesData(response);
  },

  getListsFailureCallback: function(error){
    voltmx.application.dismissLoadingScreen();
    showError(error.errmsg);
    voltmx.print("Failed to Fetch Recipes: " + JSON.stringify(error));
  },

  /**
      * @function : getImagesData
      * @description : Recipes list success
      * @param : response
      * @returns {boolean} true/false : no return value
      */
  getImagesData: function(response){
    try{
      if(response !==null && response.opstatus === 0){
        RecipeList = [];
        this.view.MobileHeader.searchText = "";
        var currentForm = voltmx.application.getCurrentForm();
        currentForm.RecipeList.showRecipeList(response);
      }
    }catch(error){
      voltmx.print("Error in data mapping: " + error);      
    }
  },

  onRecipeDeleteClick: function(record) {
    this.view.AlertDialog.setYesBtnText("Delete");
    this.view.AlertDialog.setNoBtnText("Cancel");
    this.view.AlertDialog.setMessage("Are you sure you want to delete this recipe?");
    const self = this;
    const deleteHandler = function() {
      self.toggleAlertContainer(false);
      deleteObject("Recipe", record, (response) => {
        voltmx.print("Record deleted: " + JSON.stringify(response));
        self.refreshRecipeList();
      }, (error) => {
        self.showError(error.errmsg);
        voltmx.print("Error in record delete: " + JSON.stringify(error));
      });
    };
    this.view.AlertDialog.setYesBtnClickCallback(deleteHandler);
    this.toggleAlertContainer(true);
  },

  /**
   * Display an error message
   * msg: The message to display
   */
  showError: function(msg) {
    voltmx.ui.Alert({
      "alertType": constants.ALERT_TYPE_ERROR,
      "message": msg
    }, {
      "iconPosition": constants.ALERT_ICON_POSITION_LEFT
    });
  },

  searchRecipeCatalog: function(){
    var currentForm = voltmx.application.getCurrentForm();
    currentForm.RecipeList.searchRecipeList(this.view.MobileHeader.searchText);
  },

});