/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define({
  // Delete an ingredient
  onDeleteIngredientRow: function(context) {
    this.executeOnParent("processRemoveIngredient", context.rowIndex);

  },
 });
