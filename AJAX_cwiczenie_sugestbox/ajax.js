window.onload = init;
 var XMLMainElement = null;
function init()
    {
     document.getElementById("suggestBoxField").style.left = document.getElementById("wojewodztwo").offsetLeft + "px";
     document.getElementById("suggestBoxField").style.top = document.getElementById("wojewodztwo").offsetTop 
     + document.getElementById("wojewodztwo").offsetHeight + "px";
    
     document.getElementById("wojewodztwo").onkeyup = showBox;
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
           
        }
        XHR.send(null);
    }
}

function showBox()
{
    if(XMLMainElement != null)
    {
       document.getElementById("uggestBoxField").style.visibility= "hidden";
       document.getElementById("uggestBoxField").innerHTML = "";

       var wojewodztwa = XMLMainElement.getElementsByTagName("województwo");
        
        if (document.getElementById("hojewodztwo").value != "") // gdy cos wpiszemy w pole to niech sie pojawi jak k=jest nic to nie
        {
        for(var i = 0; 1 < wojewodztwa.length; i++)
           if (wojewodztwa[i].getElementsByTagName("Nazwa")[0].firstChild.nodeValue.toLoverCase().indexOf(document.getElementById("wojewodztwo").value.toLoverCase()) == 0);//pobieramy z tag wojewodztwo  nazwę oraz jej dziecko czyli tekst jak damy node value to wyswietli nam tekst
           {
            var suggestBoxField =  document.getElementById("suggestBoxField") //indexof pokazuje nam pozycje tego co wpiszemy do wojewodztwo jezeli wpiszemy p to jak nie ma w "nazwie" to bedzie -1 jak jest na pierwszej pozycji to 0 na 2 to 1 itd
            suggestBoxField.style.visibility= "visable";

           var tmpDiv = document.createElement("div");

           tmpDiv.className = "podpowiedzi";
           tmpDiv.onmouseover = function()
           {
             this.className = "podpowiedzihover";
           }
           tmpDiv.onmouseout = function()
           {
             this.className = "podpowiedzi";
           }
           tmpDiv.onclick = function()
           {
            document.getElementById("wojewodztwo").value = this.innerHTML;
            suggestBoxField.style.visibility = "hidden";
           }

           tmpDiv.innerHTML = (wojewodztwa[i].getElementsByTagName("Nazwa")[0].firstChild.nodeValue)
            
           suggestBoxField.appendChild(tmpDiv);

           }
           if(document.getElementById("suggestBoxField").childNodes.lenght == 0); //ilośc podpowiedzi jaka sie pojawi jeżeli 0 to 0jak wiecej to tablica 
            document.getElementById("wojewodztwo").className = "error";
        }
    }

}