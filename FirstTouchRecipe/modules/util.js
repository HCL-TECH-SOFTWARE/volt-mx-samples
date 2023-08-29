/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
const GlobalState = {
  loginContext: {},
  isCancel: false
}

var RecipeList = [];

function getImageFileMobile(target, callback) {
  try {
    var querycontext={"mimetype":"image/*"};
    voltmx.phone.openMediaGallery((imageRawByte, permStatus, mimeType) => {
      if(imageRawByte===null){
        return;
      }
      if(voltmx.os.deviceInfo().name.toLowerCase()=='iphone'){
        mimeType=permStatus;
      }

      if (mimeType=='image/png' || mimeType=='image/jpeg' || mimeType=='image/jpg') {
        const base64=kony.convertToBase64(imageRawByte);
        target.base64 = base64;
        if(callback) {
          callback(base64, mimeType);
        }
      }
    }, querycontext);
  } catch(error) {
    alert(JSON.stringify(error));
  }
}

function getImageFileWeb(target, callback) {
  const config = {
    selectMultipleFiles: true,
    filter: ["image/png", "image/jpeg", "image/jpg"]
  };
  voltmx.io.FileSystem.browse(config, function (event, files) {
    const imgFile = event.target.files[0];
    const mimeType = imgFile.type;
    const isImageFile = mimeType=='image/png' || mimeType=='image/jpeg' || mimeType=='image/jpg';
    if(!isImageFile) {
      voltmx.ui.Alert({
        "alertType": constants.ALERT_TYPE_ERROR,
        "message": 'This file type is not supported',
      }, {
        "iconPosition": constants.ALERT_ICON_POSITION_LEFT
      });
      return;
    }

    if (imgFile.size > 10 * 1024 * 1024) {
      voltmx.ui.Alert({
        "alertType": constants.ALERT_TYPE_ERROR,
        "message": 'Image file should be less than 10MB',
      }, {
        "iconPosition": constants.ALERT_ICON_POSITION_LEFT
      });
      return;
    }
    var reader = new FileReader();
    reader.addEventListener("load", function () {
      const base64Encode = reader.result.substring(reader.result.indexOf(";base64,")+";base64,".length);
      target.base64 = base64Encode;
      if(callback) {
        callback(base64Encode, imgFile.type);
      }
    }, false);
    reader.readAsDataURL(imgFile);
  });
}

function getImageFile(target, callback) {
  const device = voltmx.os.deviceInfo().name.toLowerCase();
  if(device =='iphone' || device == 'android') {
    getImageFileMobile(target, callback)
  } else {
    getImageFileWeb(target, callback)
  }
}

function convertStringToBase64(str) {
  var b64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
  var o1, o2, o3, h1, h2, h3, h4, bits, i = 0, ac = 0, enc='', tmp_arr = [];

  do{ //Pack three octets into four hexets
    o1 = str.charCodeAt(i++) & 0xff;
    o2 = str.charCodeAt(i++) & 0xff;
    o3 = str.charCodeAt(i++) & 0xff;

    bits = o1<<16 | o2<<8 | o3;

    h1 = bits>>18 & 0x3f;
    h2 = bits>>12 & 0x3f;
    h3 = bits>>6 & 0x3f;
    h4 = bits & 0x3f;

    tmp_arr[ac++] = b64.charAt(h1) + b64.charAt(h2) + b64.charAt(h3) + b64.charAt(h4);
  } while(i < str.length);

  enc = tmp_arr.join('');

  switch(str.length % 3) {
    case 1: enc = enc.slice(0, -2) + '==';
      break;
    case 2: enc = enc.slice(0, -1) + '=';
      break;
    default: break;
  }

  return enc;
};


function createImageHTMLString(base64Content) {
  const image = `<img src="data:image/png;base64, ${base64Content}"/>`;
  const device = voltmx.os.deviceInfo().name.toLowerCase();
  if(device =='iphone' || device == 'android') {
    return convertStringToBase64(image);
  } else {
    return voltmx.convertToBase64(image);
  }
}

function extractImageData(pictureData) {
  let decodedStr = '';
  if (!pictureData) {
    return "";
  }
  const device = voltmx.os.deviceInfo().name.toLowerCase();
  if(device =='iphone' || device == 'android') {
    const rawBytes = voltmx.convertToRawBytes(pictureData);
    if(rawBytes) {
      decodedStr = rawBytes.text;
    }
  } else {
    decodedStr = window.atob(pictureData);
  }

  if (decodedStr.indexOf && decodedStr.indexOf(";base64,") != -1) {
    return decodedStr.substring(decodedStr.indexOf(";base64,")+";base64,".length, decodedStr.length-3);
  } else {
    return "";
  }
}

function getImageData(object, idField, idValue, imageName, container) {
  const record = {};
  record[idField] = idValue;
  const options = {
    binaryAttrName: imageName,
    queryParams: {
      unid: idValue,
      name: imageName,
    }
  };
  getBinaryContent(object, record, function(data) {
    voltmx.print("binary content is : " + JSON.stringify(data));
    container.base64 = data;
  },
  function(error) {
    voltmx.print("failed to get binary data : " + JSON.stringify(error));
  }, options);
}

// Image conversion to base64 by calling getbinarycontext service for mobiles ..
function getImageDataMobiles(object, idField, idValue, imageName, callback) {
  const record = {};
  record[idField] = idValue;
  const options = {
    binaryAttrName: imageName,
    queryParams: {
      unid: idValue,
      name: imageName,
    }
  };
  getBinaryContent(object, record, function(data) {
    voltmx.print("binary content is : " + JSON.stringify(data));
    callback(data);
  },
                   function(error) {
    voltmx.print("failed to get binary data : " + JSON.stringify(error));
  }, options);
}

// {"details":{"message":"Invalid session/session expired: f531d33a-f022-4ef5-84af-a299ee1242b0","errcode":0,"errmsg":"Invalid session/session expired: f531d33a-f022-4ef5-84af-a299ee1242b0"},"mfcode":"Auth-55","opstatus":104,"message":"Session/Token got invalidated in the backend.Please login."}

function handleSessionError(err, errorCallback) {
  switch (err.opstatus) {
    case 104:
      redirectToLogin();
      break;
    case 403:
      voltmx.ui.Alert({
        "alertType": constants.ALERT_TYPE_ERROR,
        "message": JAC.ERR_MSG.ACCESS_DENIED,
      }, {
        "iconPosition": constants.ALERT_ICON_POSITION_LEFT
      });
      redirectToLogin();
      break;
    default:
      errorCallback(err);
  }
}

function redirectToLogin() {
  voltmx.application.dismissLoadingScreen();
  const { loginFormId } = GlobalState.loginContext;
  const ntf = new voltmx.mvc.Navigation(loginFormId);
  ntf.navigate({
    disableSSOCheck: true,
  });
}

function getObject(objectName, filter, successCallback, errorCallback) {
  try {
    const objSvc = voltmx.sdk.getCurrentInstance().getObjectService(JAC.OBJECT_SERVICE);
    const dataObject = new kony.sdk.dto.DataObject(objectName);
    if (filter) {
      dataObject.odataUrl = `$filter=${filter}`;
    }
    const options = {
      "dataObject": dataObject,
    };
    objSvc.fetch(options, successCallback, (err) => {
      handleSessionError(err, errorCallback);
    });
  } catch (e) {

  }
}

function clean (obj) {
  if (!obj) {
    return;
  }

  const fields = ['Name', 'Directions', 'Ingredients'];
  var escapeField = (str) => {
    if (isNullorEmpty(str)) {
      return str;
    }
    const tags = {
        '&': ' ',
        '<': ' ',
        '>': ' ',
    };
    return str.replace(/[&<>]/g, function(tag) {
        return tags[tag] || tag;
    });
  }
  for(let i=0; i<fields.length; i++) {
    const field = fields[i];
    obj[field] = escapeField(obj[field]);
  }
};


/*NEEDSWORK
function saveUsername(username) {
  voltmx.store.setItem(STORE_USERNAME_KEY, username);
}

function getProfile() {
  const data = voltmx.store.getItem(STORE_PROFILE_KEY);
  const profile = JSON.parse(data ? data : '{}');
  return profile;
}

function saveProfile(profile) {
  voltmx.store.setItem(STORE_PROFILE_KEY, JSON.stringify(profile));
}
*/
function createObject(objectName, record, successCallback, errorCallback) {
  objectOperation(objectName, 'create', record, successCallback, errorCallback);
}

function updateObject(objectName, record, successCallback, errorCallback) {
  objectOperation(objectName, 'update', record, successCallback, errorCallback);
}

function deleteObject(objectName, record, successCallback, errorCallback) {
  objectOperation(objectName, 'delete', record, successCallback, errorCallback);
}

function getBinaryContent(objectName, record, successCallback, errorCallback, options) {
  objectOperation(objectName, 'getBinary', record, successCallback, errorCallback, options);
}

function objectOperation(objectName, action, record, successCallback, errorCallback, options) {
  try {
    const objSvc = voltmx.sdk.getCurrentInstance().getObjectService(JAC.OBJECT_SERVICE);
    const dataObject = new kony.sdk.dto.DataObject(objectName);
    Object.keys(record).forEach((k) => {
      dataObject.addField(k, record[k]);
    });
    options = options || {};
    options['dataObject'] = dataObject;
    switch (action) {
      case 'create':
        objSvc.create(options, successCallback, (err) => {
          handleSessionError(err, errorCallback);
        });
        break;
      case 'update':
        objSvc.update(options, successCallback, (err) => {
          handleSessionError(err, errorCallback);
        });
        break;
      case 'delete':
        objSvc.deleteRecord(options, successCallback, (err) => {
          handleSessionError(err, errorCallback);
        });
        break;
      case 'getBinary':
        objSvc.getBinaryContent(options, successCallback, (err) => {
          handleSessionError(err, errorCallback);
        });
        break;
    }
  } catch (e) {
    redirectToLogin();
  }
}

/**
      * @function : isNullorEmpty
      * @description  : Checking value is null, empty or not.
      * @param : value
      * @returns {boolean} true/false : return boolean value
      */
function isNullorEmpty(value) {
  if (((typeof(value) === "undefined") || (value === null) || (value === "null") || (value === "") || (value === undefined) || (value === " ") || (value === "{}") || (value === '')||(value.length===0))) {
    return true;
  } else {
    return false;
  }
}

/**
      * @function : isSplitToList
      * @description  : Return list based on split type
      * @param : data, splitVal
      * @returns {boolean} true/false : return the splitted list
      */
function isSplitToList(data, splitVal){
  return data.split(splitVal);
}

/**
      * @function : filterSearchResults
      * @description  : Checking the pattern in object and return search results.
      * @param : object, searchvalue
      * @returns {boolean} true/false : return booelan value 
      */
function filterSearchResults(obj, pattern){
  try {
    if(!isNullorEmpty(obj.Ingredients)){
      if(obj.lblName.toLowerCase().search(pattern) !== -1 || obj.Ingredients.toLowerCase().search(pattern) !== -1){
        return true;
      }else{
        return false;
      }
    }else{
      if(obj.lblName.toLowerCase().search(pattern) !== -1)
        return true;
      else
        return false;
    }
  } catch (e) {
     voltmx.print("Exception Occured: " + JSON.stringify(e));
  }
}

 /**
  * Display an error message
  *
  * msg: The message to display
 */
 function showError(msg) {
  voltmx.ui.Alert({
    "alertType": constants.ALERT_TYPE_ERROR,
    "message": msg
  }, {
    "iconPosition": constants.ALERT_ICON_POSITION_LEFT
  });
}
