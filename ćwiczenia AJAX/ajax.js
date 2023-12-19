window.onload = ajaxInit;
function ajaxInit()
{
    document.getElementById('tekst').onmouseover = function(evt)
    {
         evt.target.style.cursor='pointer';
        
    }
    var XHR = null;
    try
    {
        XHR=  new XMLHttpRequest();
    }
    catch(e)
    {
        try
    
         {
           XHR = new ActiveXObject("Msxml2.XMLHTTP");
         }
        catch(e2)
         {
            try
            {
                XHR = new ActiveXObject("Microsoft.XMLHTTP");
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
  XHR =  ajaxInit();

  if (XHR != null)
   { 
     XHR.open("GET", URL+"?random="+Math.random(), true); //! false-synchronicznie, true-asynchronicznie
     alert("bb");
     XHR.onreadystatechange = function()
     {  
        if (XHR.readyState == 1 || XHR.readyState == 2 || XHR.readyState == 3)
        {
            document.getElementById('tekst').innerHTML = "<img src='loading.gif' alet='wczytują się dane' />";
        }
         else if (XHR.readyState == 4)
         {
            if (XHR.status == 200)
              document.getElementById('tekst').innerHTML = XHR.responseText;
            else
              alert("Wystąpił błąd "+XHR.status+ " proszę o kontakt na...");
        }
     }
     
     XHR.send(null);
   }
}