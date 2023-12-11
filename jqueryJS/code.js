window.onload = function()
{
/*$(document).ready(
    function () 
    {
     $("#wyjatkowy + div").css("color", "blue");
     $("div").click(
        function()
        {
        $(this).css("font-weight", "bold");    
        }
     );
     $("ol li:nth-child(2)").css("border", "1px soli black");
     $("#wyjatkowy").css("position", "absolute").css("left", 200);
    
     $("#wyjatkowy :checkbox").click(
        function()
        {
           var ilosc= $("wyjatkowy :checked").lenght;

           $("div:last").text("aktulanie jest zaznaczonych" + ilosc + "odpowiedzi")
        }
        )
        $("#valueRange").change(function()
        {
         $("#valueFromRange").attr("value", $(this).val());
        }
         ); //jquery do atrybutu data-
         $("#AB input:eq(0)").data("value", "blala"); //!zmiana zawartosci atrybutu data-
        $("#AB input:eq(0)").data("value");
        //!przyciski do video
        $("#playpausebutton").click(function()
            {
              var videoElement= $("#testvideo")[0];

              if(videoElement.paused)
              {
               videoElement.play();
               $("#playpausebutton").html("pause");
              }
              else
              {
               videoElement.pause();
               $("#playpausebutton").html("play");
            }

         });
    
       $("#testvideo")[0].controls=true;
       //$("#testvideo")[0].autoplay=true;
       //$("#testvideo")[0].loop=true;

    })*/
    function dragstart(event)
    {
      event.dataTransfer.setData('id', event.target.id);
    
    }
    function dragimg(event)
    {
      event.preventDefault();
    }
    function drop(event)
    {
      event.preventDefault();
      event.dataTransfer.getData('id', event.target.id);
    }
   
   };
       //vanila js do atrybutu data-
       //var value=document.getElementById("AB").childNodes[1].getAttribute("data-value");

      /*document.getElementById("playpausebutton").click(function()
      {
         document.getElementById("testvideo").play();
      }*/
   