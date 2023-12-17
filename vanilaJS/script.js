/* 
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/ClientSide/javascript.js to edit this template
 */





//div.innerHTML = "nowa treść";

/* pojedynczy obiekt
 * var osoba = {
    imie: "Ula",
    nazwisko: "Krawczyk",
    pobierzInformacje: function()
    {
        return this.imie + " " + this.nazwisko;
    },
    toString: function()
    {
        return this.imie + " " + this.nazwisko;
    }
};

  alert(osoba.imie);
   div.innerHTML = osoba;*/
//klasa
/*function osoba (imie, nazwisko, wiek)
{
    this.name = imie;
    this.surname = nazwisko;
    this.age = wiek; 
    //this.specifiedValue = 12; gdy działąmy z wewnątrz
    this.toString = function()
    {
        return this.name + " " + this.surname + " " + this.age;
    };
}
   
   var x = new osoba("ula", "Krawczyk", 16);
   var y = new osoba("ula", "kwiecińska", 17);
   var z = new osoba( "ula", "brzydula", 20);
   
   osoba.prototype.specifiedValue = 12; //gdy działamy na klase z zwenątrz
   div.innerHTML = x + "<br>" + y + "<br>" + z;
   
   var produkty = [
       
      "PHP",
      "JavaScript",
      "Mysgl"
   ];
   
   //produkty.push("PRO"); aby dodoać element na koeniec listy to lub to nizej
   
   produkty[produkty.length] = "PRO";
   //alert(produkty[3]);*/
/*var kursyProgramowania =[
    "C++",
    "Java",
    "C#",
    "Pascal"
];
   var rezultat = document.getElementById("rezultat");
   
   var kursyProgramowania = document.getElementById("kursyProgramowania").getElementsByTagName("li");
   //var liArray = ul.getElementsByTagName("li");
   
   
 var i = 0;
 
 while(i < kursyProgramowania.length)
 {
     rezultat.innerHTML += kursyProgramowania[i].innerHTML +"blalal" + "<br>";
     i++;
     
 }*/

 /*var kursyProgramowania = document.querySelector("#kursyProgramowania li");

 alert(kursyProgramowania.innerHTML);

 var kursyTworzeniaStrornWWW = document.getElementById("kursyTworzeniaStornWWW");
 /*for( var i=0; i<kursyTworzeniaStrornWWW.length; i++)
 {
    kursyTworzeniaStrornWWW[i].style.color = "red";
 }*/

//kursyTworzeniaStrornWWW.setAttribute("class", "zmienKolor");

/*var x= document.createElement("p");
 x.style.color= "red";
 x.style.className = "test";
 x.innerHTML= "<p id='testowy2'> text<p>";

 var body= document.querySelector("body");
 body.appendChild(x);// remove(x); nie ma wsparcia ta metoda?

 var testowy2=document.getElementById("testowy2");
 testowy2.style.color= "blue";

 x.parentNode.removeChild(x);// usunięcie dziecka*/


    var test = document.getElementById("test"); 
    function pomniejsz()
    {
    //test.style.fontSize= "30px";
    test.className = "buttonSmaller";
    }
 
    function powieksz()
    {
    //test.style.fontSize = "40px";
    test.className = "buttonBiger";
    }

   var biger = document.getElementById("biger");
   var smaler = document.getElementById("smaller");

    //smaler.onclick = pomniejsz;
   smaler.addEventListener("click", pomniejsz);
     //biger.onclick = powieksz;
    biger.addEventListener("click", powieksz)

    //smaler.onclick = function() {pomniejsz(test)};
    //biger.onclick =function() {powieksz(test)};




    function createEvent (obj, eventName, functionToInvoke)
    {
    if(document.addEventListener)
     obj.addEventListener(eventName, functionToInvoke);
    else
     obj.attachEvent("on" + eventName, functionToInvoke);
    }


    function removeEvent (obj, eventName, functionToInvoke)
    {
    if(document.removeEventListener)
     obj.removeEventListener(eventName, functionToInvoke);
    else
     obj.detachEvent("on" + eventName, functionToInvoke);
    }

     function powiekszCzcionke()
    {
    var fontSize = parseInt(window.getComputedStyle(this).fontSize);
    this.style.fontSize =  (++fontSize) + "px";
    }
    var dodaj = document.getElementById("dodaj");
    var stop= document.getElementById("stop");

   createEvent(dodaj, "mouseover", powiekszCzcionke);
   createEvent(stop, "click", function()
    {
      removeEvent(dodaj, "mouseover", powiekszCzcionke);
    }); 

    /*dodaj.addEventListener("mouseover", powiekszCzcionke);
    stop.addEventListener("click", function()
    {
    dodaj.removeEventListener("mouseover", powiekszCzcionke);
    });
    function execute (event, str)
    {
     
        var temp = document.getElementById("temp");
        temp.innerHTML = event.clientX + " " + str;

        var hint= document.getElementById("hint");

        hint.style.display = "block";

        hint.style.left= event.clientX + 10 + "px";
        hint.style.top= event.clientY + 10 + "px";
    }
    var textTest = document.getElementById("textTest");

    textTest.onmousemove = function(event)
    {
        execute (event, this.tagName);
    };




       /* var email= document.getElementById("email");
      var submitFormButton = document.querySelector("#newsletter input[type='submit']");

      submitFormButton.onclick = function(e)

      {
      var add= document.getElementById("add");
      e.preventDefault();

      add.innerHTML= email.value;

      if(email.value === "mail")
      this.parentNode.submit();
     };
     submitFormButton.oncontextmenu = function(e)
     {
      e.returnValue = false;
      }*/
      //! to top button
     var toTopButton = document.getElementById("toTopButton");
     toTopButton.onclick= function()
      {
     window.scrollBy(0, -1 * window.scrollY);
     };

     window.onscroll = function()
     {  
     var yscroolAxis= window.scrollY;
     if(yscroolAxis > 300)
     toTopButton.style.display = "block";
     else 
     toTopButton.style.display = "none";
     };

     //! serce podążające za myszką 
     function moveThis(e, obj)
     {
      obj.style.left= e.clientX - obj.width /2 + "px";
      obj.style.top = e.clientY + window.scrollY - obj.height / 2 + "px";
      }
     var serce= document.querySelector("#serce");
     serce.onmousedown= function()
     {
      var temp = this;
      document.onmousemove= function(e)
      {
      moveThis(e, temp);
     };
      }
      serce.onmouseup = function()
     {
      document.onmousemove= false;
      }
     serce.ondragstart = function(e)
      {
      e.preventDefault();
     };

       /*window.onload= function()
     {
     function moveThis(e, obj)
     {
       obj.style.left= e.clientX - obj.width /2 + "px";
      obj.style.top= e.clientY -obj.height /2 + "px";
      }
 
      var serce= document.querySelector("#serce");

      function dodaj(e)
     {
      var temp = serce;
      moveThis(e, temp);
      };
      serce.addEventListener("mousedown", function()
     {
   
     document.addEventListener("mousemove",dodaj) 
      });
      serce.addEventListener("mouseup",function()
     {
      document.removeEventListener("mousemove", dodaj);
      });

      serce.ondragstart = function(e)
     {
      e.preventDefault();
      };
     };*/


      //!stoper z zmienna globalna
     /**  var timeOutStoper;
     function stopwatch(uchwytStopera,liczba)
     {
     uchwytStopera.innerHTML= liczba--;
      if (liczba < 0)
      return;
      timeOutStoper= setTimeout(function()
      {
      stopwatch(uchwytStopera, liczba);
      }, 1000);
       return timeOutStoper;
     }

     var startStoper = document.getElementById("startStoper");
     var stopStoper = document.getElementById("stopStoper");


     var uchwytStopera = document.getElementById("uchwytStopera");

     startStoper.onclick= function()
     {
     var initialValue = document.getElementById("initialValue").value;
     uchwytStopera.innerHTML= initialValue;

      if(timeOutStoper)
     clearTimeout(timeOutStoper);

      timeOutStoper = stopwatch(uchwytStopera, initialValue);
      };
      stopStoper.onclick = function ()
      {
      clearTimeout(timeOutStoper);
      };*/

      //!stoper funkcja konstrukcyjna (lepsza metoda)


      function Stopwatch(uchwytStopera)
      {
        this.uchwytStopera = uchwytStopera;
        this.initialValue;
        this.TimeoutRef = undefined;
        this.start = function(initialValue)
        {
          this.initialValue = initialValue;
          if(this.TimeoutRef)
            clearTimeout(this.TimeoutRef);



          this.startStoper();        // ?lub tak(jak przy dwóch osobnych funkcjach niezaleznych) = this.startStoper(this.initialValue);
        };

        this.startStoper= function()                // ?lub tak = this.startStoper= function(liczba)
        {
          if(this.initialValue < 0)
          return;
          this.uchwytStopera.innerHTML = this.initialValue--;    // ?lub tak = this.uchwytStopera.innerHTML = liczba;

          var self = this;                                     //!w funkcji niżej nei mozemy sie odwołąc do this.startStoper należy stworzyć var
          

          this.TimeoutRef = setTimeout(function()
            {
                self.startStoper();
            }, 1000)                                    //!setTimeout(function{} ,1000 )
            
        };
        this.stop = function()
        {
            clearTimeout(this.TimeoutRef);
            continueStoper.disabled= false;
        };
        this.continue = function()
        {
          if(this.TimeoutRef)
          clearTimeout(this.TimeoutRef); 

          this.startStoper();
        };
      }

        var startStoper = document.getElementById("startStoper");
        var stopStoper = document.getElementById("stopStoper");
        var continueStoper = document.getElementById("continue");



        var uchwytStopera = document.getElementById("uchwytStopera");

        var stoper =  new Stopwatch(uchwytStopera);
        
      startStoper.onclick = function()
      {
        var initialValue = document.getElementById("initialValue").value;
        stoper.start(initialValue);
      };

      stopStoper.onclick = function()
      {
        stoper.stop();
      };

      continueStoper.onclick = function()
      {
        stoper.continue();
      };

      //!galeria obrazków z miniaturkami
window.onload= function()
{
      var mainImage = document.querySelector("#mainImage");
      var image = new Image(); //?stworzenie obrazka

      mainImage.appendChild(image); //?dodanie do mainImage obrazka

      var thumbnail = document.getElementsByClassName("photo");
      var currentThumbnail = thumbnail[0];

      image.src = currentThumbnail.getAttribute("src");
      currentThumbnail.className += " current"; //?dodajemy klase do konca stringa
      

      for (var i = 0; i < thumbnail.length; i ++)
      {
        thumbnail[i].onmouseover = function()
        {
          currentThumbnail.className = currentThumbnail.className.replace(" current", "");
          currentThumbnail= this;
          currentThumbnail.className += " current";

          image.src = this.getAttribute("src");

          setTimeout(function() {
            image.classList.add("transition");
            var computedStyle = window.getComputedStyle(image);
            image.style.opacity = computedStyle.getPropertyValue('opacity');
            image.classList.remove("transition");
          }, 100); 

          /*image.classList.add("transition");
          var computedStyle = window.getComputedStyle(image);
          image.style.opacity = computedStyle.getPropertyValue('opacity');
          image.addEventListener("transitionend", function() 
          {
           this.classList.add = "transition";
          })
          
          
          image.classList.remove("transition");*/
          
        };
        
    }
  }
    /*image.classList.add("transition")
      for(var i=0; i<thumbnail.length; i++)
      {
        thumbnail[i].onmouseover = function()
        {
          currentThumbnail.className = currentThumbnail.className.replace("current", "");
          currentThumbnail= this;
          currentThumbnail.className += " current";


        }
      }*/


      // var imageGalery = document.querySelector("#imageGalery");



