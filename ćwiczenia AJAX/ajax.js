window.onload = ajaxInit;
function ajaxInit()
{
    document.getElementById('tekst').onmouseover = function(evt)
    {
         evt.relatedTarget.style.cursor='pointer';
        
    }
    var XHR = null;
    try
    {
    XHR=  new XMLHttpRequest();
    }
    catch(a)
    {
        try
    
         {
           XHR = new ActiveXObject("Msxml2.XMLHTTP");
         }
        catch(e2)
         {
            try
            {
                XHR = new ActiveXObject(Microsoft.XMLHTTP);
            }
            catch(e3)
            {
                alert("Twoja przegladarka nie obsługuje AJAX");
            }
        }
    }
    return XHR; //!poniewż to zmienna lokalna (bo w funkcji) to na koniec ją zwracamy aby móc z niej korzystac nadal, możemy także umieśćić ją przed funkcją i będzie zmienna glonalną.

}
function fileToDiv(id, URL)
{
  XHR=  ajaxInit();
  if (XHR != null)
   {
     XHR.open("GET", URL, true); //! false-synchronicznie, true-asynchronicznie
     XHR.onreadystatechance = function()
     {  
        if (XHR.readyState == 1 || XHR.readyState == 2 || XHR.readyState == 3)
        {
            document.getElementById('tekst').innerHTML = "<img src='loading.gif' alet='wczytują się dane' />"
        }
         else if (XHR.readyState == 4)
        {
            document.getElementById('tekst').innerHTML = XHR.responseText;
        }
     }
     
     XHR.send(null);
   }
}