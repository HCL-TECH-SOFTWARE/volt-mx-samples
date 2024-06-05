
function myFileReader(inFileObject)
{
  let reader = new FileReader(); 
  reader.readAsText(inFileObject); 
  //reader.readAsBinaryString(myblob); 
  //reader.readAsArrayBuffer(myblob);
  var base64data = null;
  var bWaitForResult = true;
  reader.onloadend = function() 
  { 
    base64data = reader.result;
    bWaitForResult = false;
    alert("reader.onloadend:"+bWaitForResult);
  };

  while (bWaitForResult)
  {
    try {
      kony.timer.schedule("myFileReaderTimer001", function() {
        alert("bWaitForResult:"+bWaitForResult+", base64data:"+base64data);
      }
                          , 2, false);
    } catch (timerexc)
    {
      kony.print(timerexc.message);
    }
  }
  return base64data;
}
