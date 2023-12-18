window.onload = init;
XMLMainElement = null;
function init()
    {
     document.getElementById("suggestBoxField").style.left = document.getElementById("wojewodztwo").offsetLeft + "px";
     document.getElementById("suggestBoxField").style.top = document.getElementById("wojewodztwo").offsetTop + document.getElementById("wojewodztwo").offsetHeight + "px";
    
     suggestBox();
    }

function ajaxInit()
{
    
    var XHR = null;
  
    XHR=  new XMLHttpRequest(); 
    return XHR;
}
function suggestBox()
{
 
    var XHR = ajaxInit();
    if (XHR != null)//jeżeli XHR istnieje(różny od nulla) 
    {    
        XHR.open("GET", "wojewodztwa.xml" + "?random=" + Math.random(), true);// pobieramy przy pomocy get plik i otwieramy połączenie asynchroniczne 
        
        XHR.onreadystatechange = function()
        {  
            if(XHR.readyState == 4) //status 4 czyli wszystko wczytane
            { 
                
                if (XHR.status == 200) //200 oznacza brak błędu kod 200
                {
                    XMLMainElement = XHR.responseXML.documentElement; //pobieramy odpowiedz typu xml główny element wojewodztwa(root)
                    
                }
                else
                {
                    alert("wystąpił błąd" + XHR.status); 
                }
            }
            XHR.send(null);
        }
    }
}

  
  