/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/

define(function() {

  return {
    constructor: function(baseConfig, layoutConfig, pspConfig) {
      this.recipesData = [];
      this.view.segRecipeList.setVisibility(false);
      this.view.lblSuggested.setVisibility(false);
      this.view.flxAddRecipe.onClick = this.navToAddRecipe;
    },

    /**
      * @function : showRecipeList
      * @description : Displays all the RecipesCatalog
      * @param : response
      * @returns {boolean} true/false : no return value
      */
    showRecipeList: function(response){
      const self = this;
      const createListData = function(i) {
        const record = response.records[i];

        let imgRecipe = {
          src: "icon_image.png",
        };

        const imageData = extractImageData(record.PictureRT);
        if(imageData) {
          imgRecipe = {
            base64 : imageData,
          }
        }

        return {
          imgRecipe,
          lblName: record.Name,
          lblCookTime: "Cook Time:",
          lblCookTimeVal: record.CookTime + " min", 
          lblPrepTime: "Prep Time:",
          lblPrepTimeVal: record.PrepTime + " min",
          imgEdit: "icon_edit.png",
          imgDelete: "icon_delete.png",
          flxEdit: { onClick: function() {
            self.onClickEditRecipe(record);
          } },
          flxDelete: { onClick: function() {
            self.onClickDeleteRecipe(record);
          } },
          "Servings" : record.Servings,
          "Directions" : record.Directions,
          "Ingredients" : record.Ingredients,
          data: record

        };
      };

      try{
        this.recipesData = [];
        if(response !==null && response.opstatus === 0){
          for(var i = 0; i < response.records.length; i++){
            const index = i;
            const data = createListData(index);
            this.recipesData.push(data);
          }

          this.view.lblSuggested.text = response.records.length + " " + "Recipes";
          this.view.lblSuggested.setVisibility(true);
          this.view.segRecipeList.setData(this.recipesData);
          this.view.segRecipeList.setVisibility(true);
        }
        voltmx.application.dismissLoadingScreen();
      }catch(error){
        voltmx.application.dismissLoadingScreen();
        voltmx.print("Error in data mapping: " + error);
      }

    },

    navToAddRecipe: function() {
      const navDetails = new voltmx.mvc.Navigation("AppGroup/frmRecipeForm"); 
      navDetails.navigate({
        isEdit: false
      });
    },

    onClickEditRecipe: function(record){
      const navDetails = new voltmx.mvc.Navigation("AppGroup/frmRecipeForm"); 
      navDetails.navigate({
        isEdit: true,
        record,
      });
    },

    addDeleteHandler: function(deleteHandler) {
      this.deleteHandler = deleteHandler;
    },

    onClickDeleteRecipe: function(record){
      this.onDeleteClick(record);
    },

    /**
      * @function : searchRecipeList
      * @description : Displays all the Search Results
      * @param : searchValue
      * @returns {boolean} true/false : no return value
      */
    searchRecipeList: function(searchTextChange){
      var searchTextChange = searchTextChange.trim().toLowerCase();
      var newList = [];
      if(!isNullorEmpty(searchTextChange)){
        newList = this.recipesData.filter(word => filterSearchResults(word,searchTextChange));
        this.view.segRecipeList.data = newList;
        if (newList.length <= 1) {
          this.view.lblSuggested.text = newList.length + " " + "Recipe";
        } else {
          this.view.lblSuggested.text = newList.length + " " + "Recipes";        
        }
      }else{
        this.view.segRecipeList.data = this.recipesData;
        this.view.lblSuggested.text = this.recipesData.length + " " + "Recipes";
      }
    }

  };
});