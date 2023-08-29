/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define(function() {
  return {
    constructor: function(baseConfig, layoutConfig, pspConfig) {
      this.view.btnSaveRecipe.onClick = this.saveRecipe;
      this.view.btnCloseRecipe.onClick = this.onCloseRecipeBtnClick;
      this.view.btnSelectRecipeImage.onClick = this.onSelectRecipeImageBtnClick;
    },
    //Logic for getters/setters of custom properties
    initGettersSetters: function() {
      defineGetter(this, 'isEdit', () => {
        return this._isEdit;
      });
      defineSetter(this, 'isEdit', value => {
        this._isEdit = value;

      });
      defineGetter(this, 'record', () => {
        return this._record;
      });
      defineSetter(this, 'record', value => {
        this._record = value;
        this.updateRecipeForm();
      });
    },
    onSelectRecipeImageBtnClick: function() {
      getImageFile(this.view.imgRecipe, (base64Encoded, type) => {
        if (!(base64Encoded === undefined || base64Encoded === "")) {
          this.view.imgRecipe.base64 = base64Encoded;
          this.view.imgRecipe.type = type;
          this.view.imgDefault.setVisibility(false);
          this.view.imgRecipe.setVisibility(true);
        }
      });
    },

    onRecipeNameChanged: function() {
      this.view.lblRecipeNameErr.setVisibility(false);
    },

    onPrepTimeChanged: function() {
      this.view.lblPrepTimeErr.setVisibility(false);
    },

    onCookTimeChanged: function() {
      this.view.lblCookTimeErr.setVisibility(false);
    },

    onServingsChanged: function() {
      this.view.lblServingsErr.setVisibility(false);
    },

    onCloseRecipeBtnClick: function() {
      this.clearRecipeForm();
      if(this.saveCancel) {
        this.saveCancel();
      }
    },

    showError: function(msg) {
      voltmx.ui.Alert({
        "alertType": constants.ALERT_TYPE_ERROR,
        "message": msg
      }, {
        "iconPosition": constants.ALERT_ICON_POSITION_LEFT
      });
    },


    updateRecipeForm: function() {
      clean(this._record);
      this.view.btnSaveRecipe.text = this._isEdit ? "Update" : "Save";
      this.view.lblAddRecipe.text = this._isEdit ? "Update Recipe" : " Add Recipe";
      // this.view.tbxDifficulty.text = this._isEdit ? this._record.Difficulty : "";
      this.view.tarDirections.text = this._isEdit ? this._record.Directions : "";
      this.view.tbxIngredients.text = "";
      this.view.imgDefault.setVisibility(!this._isEdit);
      this.view.imgRecipe.setVisibility(this._isEdit);
      if (this._isEdit) {
        this.view.imgRecipe.base64 = extractImageData(this._record.PictureRT);
      }
      this.view.tbxRecipeName.text = this._isEdit ? this._record.Name : "";
      this.view.tbxPrepTime.text = this._isEdit ? this._record.PrepTime.toString() : "";
      this.view.tbxCookTime.text = this._isEdit ? this._record.CookTime.toString() : "";
      this.view.tbxServings.text = this._isEdit ? this._record.Servings.toString() : "";
      const ingredients = this._isEdit ? (this._record.Ingredients ? this._record.Ingredients.split(JAC.INGREDIENT_SEPARATOR) : []) : [];
      const self = this;
      const ingredientUIData = ingredients.map(e => {
        return {
          "lblIngredient": {"text": e},
          imgDelete: "cross_1_1_1.png",
          flxDeleteContainer : {
            onTouchEnd : function() {
              const existingData = self.view.IngredientList.segIngredient.data;
              const newData = existingData.filter((row)=>{
                return row.lblIngredient.text !== e;
              })
              self.view.IngredientList.segIngredient.setData(newData);
            }
          }
        }});
      this.view.IngredientList.segIngredient.setData(ingredientUIData);
      this.view.lblRecipeNameErr.setVisibility(false);
      this.view.lblPrepTimeErr.setVisibility(false);
      this.view.lblCookTimeErr.setVisibility(false);
      this.view.lblServingsErr.setVisibility(false);

    },

    clearRecipeForm: function() {
      this.view.tarDirections.text = "";
      this.view.tbxIngredients.text = "";
      this.view.tbxRecipeName.text = "";
      this.view.tbxPrepTime.text =  "";
      this.view.tbxCookTime.text = "";
      this.view.tbxServings.text = "";
      this.view.imgRecipe.base64 = "";
    },

    validation: function() {
      let pass = true;
      const recipeName = this.view.tbxRecipeName.text;
      if (!recipeName) {
        this.view.lblRecipeNameErr.setVisibility(true);
        pass = false;
      }

      let prepTime = this.view.tbxPrepTime.text;
      if (prepTime) {
        if (isNaN(Number(prepTime))) {
          this.view.lblPrepTimeErr.setVisibility(true);
          pass = false;
        }
      }

      let cookTime = this.view.tbxCookTime.text;
      if (cookTime) {
        if (isNaN(Number(cookTime))) {
          this.view.lblCookTimeErr.setVisibility(true);
          pass = false;
        }
      }

      let servings = this.view.tbxServings.text;
      if (servings) {
        if (isNaN(Number(servings))) {
          this.view.lblServingsErr.setVisibility(true);
          pass = false;
        }
      }

      return pass;
    },

    addIngredient: function() {
      let ingredient = this.view.tbxIngredients.text;
      const allIngredients = this.view.IngredientList.segIngredient.data || [];
      const existing = allIngredients.filter((row)=>{
        return row.lblIngredient.text == ingredient
      })
      if(existing.length > 0)
      {
        this.view.tbxIngredients.text = "";
        return;
      }

      ingredient = ingredient ? ingredient : "";
      let ingredientText = ingredient.trim();
      const self = this;
      if (ingredientText.length > 0) {
        let ingredientRow = {
          lblIngredient: {
            text: ingredientText,
          },
          imgDelete: "cross_1_1_1.png",
          flxDeleteContainer : {
            onTouchEnd : function() {
              const existingData = self.view.IngredientList.segIngredient.data;
              const newData = existingData.filter((row)=>{
                return row.lblIngredient.text !== ingredientText;
              })
              self.view.IngredientList.segIngredient.setData(newData);
            }
          }
        }
        let dataArr = [];
        dataArr.push(ingredientRow);
        this.view.IngredientList.segIngredient.addAll(dataArr);
      }
      this.view.tbxIngredients.text = "";
    },

    saveRecipe: function() {
      voltmx.model.ApplicationContext.showLoadingScreen('Loading...');
      if (this.validation()) {        
        const record = {
          Directions: this.view.tarDirections.text,
          Name: this.view.tbxRecipeName.text,
          PrepTime: this.view.tbxPrepTime.text,
          CookTime: this.view.tbxCookTime.text,
          Servings: this.view.tbxServings.text,
        };

        if (this.view.IngredientList.segIngredient.data && this.view.IngredientList.segIngredient.data.length > 0) {
          record.Ingredients = this.view.IngredientList.segIngredient.data.map(e => e.lblIngredient.text).join(JAC.INGREDIENT_SEPARATOR);
        }

        if (this.view.imgRecipe.base64 && this.view.imgRecipe.base64 !== "") {
          record.PictureRT = createImageHTMLString(this.view.imgRecipe.base64);
        }

        clean(record);

        const self = this;
        if (this._isEdit) {
          record.x_0040unid = this._record.x_0040unid;
          updateObject("Recipe", record, (response) => {
            voltmx.print("Record updated: " + JSON.stringify(response));
            this.clearRecipeForm();
            if(self.saveSuccess) {
              self.saveSuccess();
            }
          }, (error) => {
            voltmx.application.dismissLoadingScreen();
            showError(error.errmsg);
            voltmx.print("Error in record update: " + JSON.stringify(error));
          });
        } else {
          createObject("Recipe", record, (response) => {
            voltmx.print("Record created: " + JSON.stringify(response));
            this.clearRecipeForm();
            if(self.saveSuccess) {
              self.saveSuccess();
            }
          }, (error) => {
            kony.application.dismissLoadingScreen();
            showError(error.errmsg);
            voltmx.print("Error in record save: " + JSON.stringify(error));
          });
        }
      } else {
        voltmx.model.ApplicationContext.dismissLoadingScreen();
      }
    },


  };
});
