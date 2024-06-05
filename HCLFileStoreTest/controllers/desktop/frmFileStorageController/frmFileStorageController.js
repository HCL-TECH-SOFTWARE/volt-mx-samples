define({ 
  //Type your controller code here 
  _fileStoreObj : null,
  self: null,
  /* First Function invoked after navigation*/
  onNavigate : function(){
    this.applyBindings();
  },
  
  applyBindings : function(){
    this.view.preShow = this.onPreShow.bind(this);
    this.view.postShow = this.onPostShow.bind(this);
    //this.view.btnUpload.onClick = this.onFileUpload.bind(this);
    this.view.btnList.onClick = this.onListFiles.bind(this);
    this.view.btnDownload.onClick = this.onDownloadFile.bind(this);

  },
  
  /* Method callback on pre show of the form  */
  onPreShow : function(){
    self = this;
    var serviceName = "fosFilestorage";
    var serviceType = "online";
    var currObj = voltmx.sdk.getCurrentInstance();
    objSvc = currObj.getObjectService(serviceName, {
      "access": serviceType
    });
    fileStorage = objSvc.getFileStorage();
    this._fileStoreObj = fileStorage;
    if (fileStorage === null) {
      alert("File Storage Init Failed !");
      this.setStatus("File Storage Init Failed !");
    } else {
      gvFSInitOk = true;
      this.setStatus("File Storage Init successfull !");
    }
  },
  
  /* Method callback on post show of the form  */
  onPostShow : function(){
    if (gvFSInitOk)
    {
      self.onListFiles();
    }
  },
  
  onListFiles : function() {
    self = this;
    //this.view.txtStatus.text = "";
    var headers = {};
    headers["Content-Type"] = "application/json";
    filter = "file_namespace eq namespaceFS042424 and security_key eq "+gvFSKey;

    this._fileStoreObj.listFiles(filter,
                          headers,
                          function(res) {
      voltmx.print("Results of query = " + JSON.stringify(res));
      var value = "";
      var records = res.records;
      for(var i=(records.length - 1); i > -1; i--){
        value += "Id:"+records[i].file_id+" - "+records[i].file_name +", " + (records[i].size/(1024*1024)).toFixed(2) + "M \n";
      } 
      self.view.txtAreaFileList.text =  value;
    },
    function(err) {
      voltmx.print("Query Error " + JSON.stringify(err));
      self.addStatus("Query Error " + JSON.stringify(err));
      alert("Query Error " + JSON.stringify(err));
    },
                          null);
  },

  setStatus: function (inMsg)
  {
    this.view.txtStatus.text = inMsg;
  },

  addStatus: function (inMsg)
  {
    this.view.txtStatus.text = inMsg +"\n\n"+this.view.txtStatus.text;
  },

  onFSFileUpload: function(){
    self = this;
    this.view.txtStatus.text = "";
    kony.application.showLoadingScreen(null, null, constants.LOADING_SCREEN_POSITION_FULL_SCREEN, true, true, {});

    var config = {
      selectMultipleFiles: true,
      filter: []
/*
      filter: ["application/pdf", "application/msword", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", 
               "application/vnd.ms-outlook", 
               "application/vnd.ms-excel", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "image/png", "image/jpeg"]
*/
      };
    kony.io.FileSystem.browse(config, this.onFSFileSelectCallback.bind(this));
    kony.application.dismissLoadingScreen();
  },
  
  checkFileSize: function(fileList)
  {
    kony.application.showLoadingScreen(null, null, constants.LOADING_SCREEN_POSITION_FULL_SCREEN, true, true, {});

    var newList = [];
    for (var i=0; i<fileList.length; i++)
    {
      if (fileList[i].size < (600*1024*1024))
        newList.push(fileList[i]);
      else
      {
        if (gvAllowBigFile)
        {
          newList.push(fileList[i]);
          gvAllowBigFile = false;
        }
        else
        {
          alert(fileList[i].name + " is greater than 4MB, size = "+fileList[i].size+". Ignored!");
          self.addStatus(fileList[i].name + " is greater than 4MB, size = "+fileList[i].size+". Ignored!");
        }
      }
    }

    kony.application.dismissLoadingScreen();
    return newList;
  },

  
  onFSFileSelectCallback : function(event, fileList){
    kony.application.dismissLoadingScreen();

    let newList = this.checkFileSize(fileList);
    if (newList.length < 1)
    {
      alert("No file to upload!");
      self.addStatus("No file to upload!");      
    }
    else
    {
      for (let i=0; i<newList.length; i++)
      {
        this.FSUpload1File(newList[i]);
      }
    }
  }, 


  FSUpload1File : function(newList)
  {
    kony.application.showLoadingScreen(null, null, constants.LOADING_SCREEN_POSITION_FULL_SCREEN, true, true, {});

    var headers = {};
    headers["Content-Type"] = "application/json";

    //fileMap = {};
    //fileMap["rawBytes"] = kony.convertToBase64(cameraWidget.rawBytes);

    //var fileMap = {};
    //fileMap["filePath"] = "/Users/ncl/Desktop/FileStorage.png";

    self.addStatus("Uploading "+newList.file.name);

    var metadata = {};
    metadata["file_name"] = newList.file.name;
    metadata["security_key"] = gvFSKey;
    metadata["file_namespace"] = "namespaceFS042424";
    metadata["size"] = newList.file.size;
    var fileObj = newList;
    fileObj["prop"] = "";

    var uploadParams = {};
    uploadParams["headers"] = headers;
    uploadParams["metadata"] = metadata;
    uploadParams["fileObject"] = newList.file;

    this._fileStoreObj.upload("UploadInputTypeLocalFilePath",
                              uploadParams,
                              function(res) {
      kony.print("Upload successful for " + metadata["file_name"] + " : " + JSON.stringify(res));
      self.addStatus(newList.file.name + " File Upload successful." + JSON.stringify(res));
      self.onListFiles();
      self.view.forceLayout();
    },
      function(err) {
        kony.print("Upload Error " + JSON.stringify(err));
        alert(newList.file.name + " File Upload Failed");
        self.addStatus(newList.file.name + " File Upload Failed");
        if (err.userInfo.errmsg.search("Duplicate") > -1)
        {
          self.addStatus("Error! Possible duplicate file:"+newList.file.name);
          alert("Error! Possible duplicate file:"+newList.file.name);
        }
    },
                              null);

    kony.application.dismissLoadingScreen();
  },

  deleteFileById: function() {
    self = this;
    this.view.txtStatus.text = "";
    selectedFileId = this.view.txtFileId.text;
    this.addStatus("Deleting file Id = "+this.view.txtFileId.text);

    headers = {};
    headers["Content-Type"] = "application/json";

    deleteParams = {};
    deleteParams["security_key"] = gvFSKey;
    deleteParams["file_namespace"] = "namespaceFS042424";

    fileStorage.deleteById(selectedFileId,
                           deleteParams,
                           headers,
                           function(res) {
      self.addStatus("Deletion Successful  : " + JSON.stringify(res));
      self.onListFiles();
      self.view.forceLayout();
    },
                           function(err) {
      self.addStatus("Deletion Error : " + JSON.stringify(err));
      alert("Deletion Error : " + JSON.stringify(err));
    },
                           null);
  },

  onDownloadFile: function() {

    //var fileMap = {};
    //fileMap["filePath"] = "/Users/dainguyen/Downloads/";
    this.addStatus("Downloading file Id = "+this.view.txtFileId.text);
    self = this;
    selectedFileId = this.view.txtFileId.text;
    //selectedFileName = "Zip.jpg";
    headers = {};
    headers["Content-Type"] = "application/json";
    //headers["responseType"] = "blob";
    metadata = {};
    metadata["file_id"] = selectedFileId;
    metadata["security_key"] = gvFSKey;
    metadata["file_namespace"] = "namespaceFS042424";

    downloadParams = {};
    //downloadParams = {"headers": headers, "metadata":metadata};
    downloadParams["headers"] = headers;
    downloadParams["metadata"] = metadata;
    //alert("Before filestorage download");

    fileStorage.download(downloadParams,
                         function(res) {
      //alert("Download success : " + JSON.stringify(res));
      voltmx.print("Res "+ JSON.stringify(res));
      voltmx.print("Res.fileObject: "+ res.fileObject);
      voltmx.print("Res.fileObject: "+ JSON.stringify(res.fileObject));

      //var binarydata = kony.convertToRawBytes(res.fileObject);
      //var myB64Data = myFileReader(res.fileObject);

      //self.downloadown(res.fileObject, res.file_name);
      { // Others
        var filetype = res.file_name.split('.').pop();
        var file = new File([res.fileObject], res.file_name, { lastModified: new Date().getTime(), type: filetype });
        var filename = res.file_name;
        var a = document.createElement("a"),
            url = URL.createObjectURL(file);
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        setTimeout(function() {
          document.body.removeChild(a);
          window.URL.revokeObjectURL(url);
        }, 0);
      }
    },
                         function(err) {
      self.addStatus("Download Error " + JSON.stringify(err));
      alert("Download Error " + JSON.stringify(err));
    }, {
      forceDownload: true
    });
  },

  
 });