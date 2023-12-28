window.onload = init;
 var XMLMainElement = null;
 var licznik= 0;
 var wybrany= 0;
 var tempCode;
function init()
    {
     document.getElementById("suggestBoxField").style.left = document.getElementById("wojewodztwo").offsetLeft + "px";
     document.getElementById("suggestBoxField").style.top = document.getElementById("wojewodztwo").offsetTop 
     + document.getElementById("wojewodztwo").offsetHeight + "px";
    
     document.getElementById("wojewodztwo").onkeyup = function(evt)
     {
        showBox(evt);
        checkKey(evt);
        
    }
     
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

function showBox(evt)
{
    if (evt.keyCode != 13 && evt.keyCode != 38 && evt.keyCode != 40 && evt.keyCode !=8)
    {
        licznik = 0;
    }

    if(XMLMainElement != null)
    {
       document.getElementById("uggestBoxField").style.visibility= "hidden";
       document.getElementById("uggestBoxField").innerHTML = "";

       var wojewodztwa = XMLMainElement.getElementsByTagName("Województwo");
        
        if (document.getElementById("wojewodztwo").value != "") // gdy cos wpiszemy w pole to niech sie pojawi jak k=jest nic to nie
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
            wybraniePodpowiedzi(this.innerHTML);
           }

           tmpDiv.innerHTML = (wojewodztwa[i].getElementsByTagName("Nazwa")[0].firstChild.nodeValue)
            
           suggestBoxField.appendChild(tmpDiv);

           }
           if(document.getElementById("suggestBoxField").childNodes.lenght == 0); //ilośc podpowiedzi jaka sie pojawi jeżeli 0 to 0jak wiecej to tablica 
            document.getElementById("wojewodztwo").className = "error";
        }
    }

}
function checkKey (evt)
{
    var iloscPodpowiedzi = document.getElementById("suggestBoxField").childNodes.lenght;
    if (licznik == 0)
    {
      licznik = iloscPodpowiedzi;
      wybrany = 0;
    }

    if (evt.keyCode == 40) //! 40 numer strzałki w dół
     {   
        if(tempCode == 'gora')
            licznik++;

        document.getElementById("suggestBoxField").childNodes[licznik%iloscPodpowiedzi].className= "podpowiedzihover";

        wybrany= licznik% iloscPodpowiedzi;
        licznik ++;
        tempCode = 'dol';
     }
     else if (evt.keyCode == 38) //!numer strzałka w górę
     {
        if(tempCode == 'dol')
            licznik--;

        licznik --;
        wybrany = licznik % iloscPodpowiedzi;
        document.getElementById("suggestBoxField").childNodes[licznik%iloscPodpowiedzi].className= "podpowiedzihover";

        tempCode = 'gora';
     }
    else if (evt.keyCode == 13) //!numer enter
    {
        document.getElementById("wojewodztwo").value= document.getElementById("suggestBoxField").childNodes[wybrany].firstChild[0];
        
        wybraniePodpowiedzi(document.getElementById("suggestBoxField").childNodes[wybrany].firstChild[0]);

        licznik = 0;
        wybrany = 0;

        tempCode = 'enter';
    }
    else if (evt.keyCode == 8) //!numer backspace
    {
        
        licznik = 0;
        wybrany = 0;

        tempCode = 'backspace';
    }
}

function wybraniePodpowiedzi(wybranyRekord)
{   
    document.getElementById("tekst").innerHTML= ""; //!jeżeli wybrany rekord ma byc tylko jeden, bez dodawania poprzednich pod spodem.
    document.getElementById("suggestBoxField").style.visibility = "hidden";

    var wybraneWojewodztwo = null;

    for( var i = 0; i <XMLMainElement.getElementsByTagName("Województwo").lenght ; i ++)
     if (XMLMainElement.getElementsByTagName("Nazwa")[i].firstChild.nodeValue == wybranyRekord)
    {
        wybraneWojewodztwo = XMLMainElement.getElementsByTagName("Nazwa")[i].parentNode;
        break;
    }

    if (wybraneWojewodztwo != null)
    {
    var table = document.createElement("table");

    table.className = "daneOWojewodztwie";
    var tableBody = document.createElement("tbody");

    for (var i = 0; i< wybraneWojewodztwo.childNodes.lenght; i++)
     {
     
      if (wybraneWojewodztwo.childNodes[i].nodeType == 1)
      {
        var row = document.createElement("tr");
        var cell = document.createElement("td");
        var header = document.createTextNode(wybraneWojewodztwo.childNodes[i].nodeName+": ");

        cell.className = "cellHeader";
      cell.appendChild(header);
      row.appendChild(cell);

      cell = documnet.createElement("td");
    
      var content= document.createTextNode(wybraneWojewodztwo.childNodes[i].firstChild.nodeValue);
      cell.appendChild(content);
      row.appendChild(cell);

      tableBody.appendChild(row);
      }
     }

    table.appendChild(tableBody);

    document.getElementById("tekst").appendChild(table);
    }

}