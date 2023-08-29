/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/

define(function() {

  return {
    constructor: function(baseConfig, layoutConfig, pspConfig) {
      this.view.segIngredients.setVisibility(false);
      this.view.segDirections.setVisibility(false);
      this.view.segIngredients.rowTemplate ="flxDetailsMain";
      this.view.segDirections.rowTemplate = "flxDirections";
    },

    /**
      * @function : showRecipeDetails
      * @description : Displays all the details of a selected recipe from recipe catalog
      * @param : no params
      * @returns {boolean} true/false : no return value
      */
    showRecipeDetails: function(record){
      var list = [];
      var stepsList = [];
      this.view.imgRecipe.base64 = record[0].imgRecipe.base64;
      this.view.lblRecipeName.text = record[0].lblName;
      this.view.lblCookTime.text = "Cook Time";
      this.view.lblCookTimeValue.text = record[0].lblCookTimeVal;
      this.view.lblPrepTime.text = "Prep Time";
      this.view.lblPrepTimeValue.text = record[0].lblPrepTimeVal;
      this.view.lblServings.text = "Servings";
      this.view.lblServingsValue.text = record[0].Servings.toString();
      this.view.lblIngredients.text = "Ingredients";
      this.view.segIngredients.widgetDataMap = {
        "lblListIngredients" : "lblListIngredients"
      };
      if(!isNullorEmpty(record[0].Ingredients)){
        var ingredientsList = isSplitToList(record[0].Ingredients, JAC.INGREDIENT_SEPARATOR);
        for(var i=0; i< ingredientsList.length; i++){
        var data = {
          lblListIngredients: ingredientsList[i]
        };
        list.push(data);
      }
      this.view.segIngredients.setData(list);
      this.view.segIngredients.setVisibility(true);
      }else{
        this.view.segIngredients.setVisibility(false);
      }
     
      this.view.lblSteps.text = "Directions";      
      this.view.segDirections.widgetDataMap = {
        "lblDirections" : "lblDirections"
      };
      if(!isNullorEmpty(record[0].Directions)){
      var directionsList = isSplitToList(record[0].Directions, "\n");
      for(var j=0; j < directionsList.length; j++){
        var stepsData = {
          lblDirections: directionsList[j]
        };
        stepsList.push(stepsData);
      }
      this.view.segDirections.setData(stepsList);
      this.view.segDirections.setVisibility(true);
      }else{
        this.view.segDirections.setVisibility(false);
      }
    }

  };
});