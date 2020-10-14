$(window).on('load',function(){

  var aa = {}
var screenwith = screen.width

  $.ajax({
       url:  '/policy/',
       type: "GET",
       dataType: "json",
       //data:{"screenwith":"screenwith"},
       //data:{"parent_id":"parent_id"},
        success: function(response){
          if (screenwith < 1370){
            var screenmedia =4
            var screenmedias =5
            var widgets = document.getElementById("post_widget_datas ")

            widgets.style.height="280px";

            var widgets = document.getElementById("post_widget_data ")
            widgets.style.height="280px";

          }
          else{
            var screenmedia = 6
            var screenmedias =5
            var widgets = document.getElementById("post_widget_datas ")
            widgets.style.height="345px";

            var widgets = document.getElementById("post_widget_data ")
            widgets.style.height="345px";

          }


           for(var i=0;i<response.results.length;i++){
            //for(var i=0;i<3;i++){
            $('#menu2nhw').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey; padding-right:10px;"><i class="fa fa-file-pdf-o" style="font-size:36px;color:#FF6347; border: 1px solid #ddd;
                                          border-radius: 4px;
                                          padding: 5px;
                                          width: auto; border-color: #f7b7c2;"></i></td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><span style=" text-align: justify;overflow: hidden;
  text-overflow: ellipsis;">${response.results[i]['policy_name']}</span></span><p>30 April 2020</p></td></tr>`)

              if(i % 2 == 0){
                $('#publicities').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey"><img src="http://192.168.0.5:8000/static/images/instructionred.png" class="rounded-circle" alt="Cinque Terre" width="50" height="50"></td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><span style="  overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 1; /* number of lines to show */
   -webkit-box-orient: vertical;">${response.results[i]['policy_name']}</span></span><p>30 April 2020</p></td></tr>`)
   if (i <screenmedias)
   {
     $('#enews').append(`<tr><td class="alert alert-success"style="border-top-left-radius:10px;border-top-right-radius:10px; ">

        <strong>${response.results[i]['policy_name']}</strong>
   </td></tr>`)

   }

                if (i <screenmedia)
                {
                  // $('#enews').append(`<p class="alert alert-error">
                  //
                  //    <strong>Latest Update On Covid-19</strong>
                  // </p>`)
                $('#nhqemsg').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey; padding-right:10px;"><i class="fa fa-file-pdf-o" style="font-size:12px;color:#FF6347; border: 1px solid #ddd;
                                          border-radius: 4px;
                                          padding: 5px;
                                          width: auto; border-color: #f7b7c2;"></i></td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><p style=" text-align: justify;white-space: nowrap;
                                        width: 250px;
                                        overflow: hidden;
                                        text-overflow: ellipsis;
                                        color:#000;
                                        color:black;
                                         font-family:WhitneyHTF-Book ;
                                        font-size:16px;
                                        ">${response.results[i]['policy_name']}</p></span></td><td><a href="#"><img src="http://192.168.0.5:8000/static/images/downloads_icon.png" height="22px"></a></td><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td></tr>`)
              }
            }
              else
              { if ((i <screenmedias) || (i <screenmedias))
                {
                  $('#enews').append(`<tr><td class="alert alert-info"style="border-top-left-radius:10px;border-top-right-radius:10px; ">

                     <strong> ${response.results[i]['policy_name']}</strong>
                </td></tr>`)
                $('#nhqemsg').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey; padding-right:10px;"><i class="fa fa-file-pdf-o" style="font-size:12px;color:#FF6347; border: 1px solid #ddd; padding-right:2%
                                          border-radius: 4px;
                                          padding: 5px;
                                          width: auto; border-color: #f7b7c2;"></i></td>
                                          <td style="border-bottom:1px dotted grey; color:#000" width="100%">
                                          <p style=" text-align: justify;  white-space: nowrap;
                    width: 200px;
                    overflow: hidden;
                    text-overflow: ellipsis;
                    color:#000;
                    color:black;
                     font-family:WhitneyHTF-Book ;
                    font-size:16px;

                    ">${response.results[i]['policy_name']}</p></span></td><td><a href="#"><img src="http://192.168.0.5:8000/static/images/downloads_icon.png" height="22px"></a></td><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td></tr>`)
              }
                $('#publicities').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey;"><img src=http://192.168.0.5:8000/static/images/img-1-4.jpg" class="rounded-circle" alt="Cinque Terre" width="50" height="50"></td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><span style=" text-align: justify; overflow: hidden;
               text-overflow: ellipsis;
               display: -webkit-box;
               -webkit-line-clamp: 1; /* number of lines to show */
               -webkit-box-orient: vertical;">${response.results[i]['policy_name']}</span></span><p>30 April 2020</p></td></tr>`)
                            //alert("ok")
              }

                    $('#menu2egs').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey; padding-right:10px;"><i class="fa fa-file-pdf-o" style="font-size:36px;color:#FF6347; border: 1px solid #ddd;
                                                border-radius: 4px;
                                                padding: 5px;
                                                width: auto; border-color: #f7b7c2;"></i></td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><span style=" text-align: justify;">${response.results[i]['policy_name']}</span></span><p>30 April 2020</p></td></tr>`)

                    $('#menu2nhwvngs').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey; padding-right:10px;"><i class="fa fa-file-pdf-o" style="font-size:36px;color:#FF6347; border: 1px solid #ddd;
                                                border-radius: 4px;
                                                padding: 5px;
                                                width: auto; border-color: #f7b7c2;"></i></td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><span style=" text-align: justify;">${response.results[i]['policy_name']}</span></span><p>30 April 2020</p></td></tr>`)
                         //publicities").append(`${response.results[i]['file']}</td><td>${response.results.[i]['policy_name']}</td></tr>`)
              }
              $('#nhqemsg').append(`<tr ><td colspan="4" style="padding-right:50px;"></td></tr>`)

              // $('#nhqemsg').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey; padding-right:387px; " colspan="4"><button onclick="myFunction()" class="thbg-color" style="background: #9f4545; background-color: #9f4545;
              //   border: none;
              //   color: white;
              //   padding: 8px 20px;
              //   text-align: center;
              //   text-decoration: none;
              //   display: inline-block;
              //   font-size: 16px;
              //   margin: 0px 2px;
              //   border-radius:10px;
              //
              //   cursor: pointer;" id="myBtn">Read more</button></td></tr>`)

        }


      })


  ////////////////////////////publication//////////////
              $.ajax({
                  url:  '/publication/',
                  type: "GET",
                  dataType: "json",
                  //data:{"parent_id":"parent_id"},
                   success: function(response){

                      for(var i=0;i<response.results.length;i++){
                        if(i % 2 == 0){
                           $('#publication').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey; padding-right:10px;"><img src="http://192.168.0.5:8000/static/images/man.png" class="rounded-circle" alt="Cinque Terre" width="50" height="50"> </td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><span style=" text-align: justify; overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 1; /* number of lines to show */
   -webkit-box-orient: vertical;">${response.results[i]['ppublication_name']}</span> <p> 30 April 2020</p></td></tr>`)
                         }
                         else{
                          $('#publication').append(`<tr style="border-bottom:1px dotted grey;padding-right:10px;"><td style="border-bottom:1px dotted grey"><img src=http://192.168.0.5:8000/static/images/man2.jpg" class="rounded-circle" alt="Cinque Terre" width="50" height="50"> </td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><span style=" text-align: justify; overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 1; /* number of lines to show */
   -webkit-box-orient: vertical;">${response.results[i]['ppublication_name']} </span> <p>30 April 2020</p></td></tr>`)

                         }
                          //$("#publicities").append(`${response.results[i]['file']}</td><td>${response.results.[i]['policy_name']}</td></tr>`)
                      }
                      //alert(JSON.stringify(response.results))  public_obj
                   }
               })

  /////////////////////////////////////////////////////Social media//////////////


              $.ajax({
                  url:  '/social_media/',
                  type: "GET",
                  dataType: "json",
                  //data:{"parent_id":"parent_id"},
                   success: function(response){

                    for(var i=0;i<response.length;i++){
                      //alert(response)

                      $('#socialmenu_bar').append(` <li class="col-sm-2" style="color:#000"><a href="${response[i]['url_link']}" style="color:#000;">${response[i]['menu_name']}</a><br/><hr>
                        </li>` )
                    }

                   }
               })

              ////////////////////////////////////Othersites///
               $.ajax({
                url:  '/menu_details/',
                type: "GET",
                dataType: "json",
                data:{"parent_id":"parent_id"},
                success: function(response){
                  //alert(JSON.stringify(response))
                   for(var i=0;i<response.length;i++){
                     var ee = '.text-center_'+i
                     $('#othersiters_bar').append(` <li class="col-sm-2" style="color:#000; font-weight:bold">${response[i]['menu_name']}<hr>
                        <ul class="menu-inner otext-center_${i}"</ul></li>` )
                         var ee = '.otext-center_'+i

                         for (var j=0;j<response[i]['othersiteParent_menu'].length;j++)
                         {
                          $(ee).append(`
                          <li><a href="/application/applicationobj_list/${response[i]['menu_name']}/${response[i]['othersiteParent_menu'][j]['menu_name']}/">${response[i]['othersiteParent_menu'][j]['menu_name']}</a></li>
                        `)

                         }

                      //$('#post_widget_data').append(`<button class="tablink" onclick="openPage('${response[i]['menu_name']}', this, 'red')">${response[i]['menu_name']}</button>`)
                   //   for (var j=0;j<response[i]['application_menu'].length;j++)


                   }

                }



              })
               $.ajax({
                  url:  '/sendjson/',
                  type: "GET",
                  dataType: "json",
                  //data:{"parent_id":"parent_id"},
                   success: function(response){
                   // alert(JSON.stringify(response))

                   }
                 })

  ///////////////////////////////////Acknowledge/////////////////////////



////////////////////////////////////Policy graph////////////////






  ///////////////////////////////////

  $.ajax({
                  url:  '/policy/',
                  type: "GET",
                  dataType: "json",
                  //data:{"parent_id":"parent_id"},
                   success: function(response){

                   }
               })

  ///////////////////////////////////////////////////
              $.ajax({
                url:  '/menu_detail/',
                type: "GET",
                dataType: "json",
                data:{"parent_id":"parent_id"},
                success: function(response){
                  //alert(JSON.stringify(response))
                   for(var i=0;i<response.length;i++){
                     var ee = '.text-center_'+i
                     $('#menu_bar').append(` <li class="col-lg-12" style=" background-color:#a4cffc12;"><a style="">${response[i]['menu_name']}<hr></a>
                        <ul class="menu-inner text-center text-centere_${i}"></ul></li>` )
                        var ee = '.text-centere_'+i
                        //alert(JSON.stringify(response[i]['application_menu']))
                        for (var j=0;j<response[i]['application_menu'].length;j++)
                        {
                          $(ee).append(`
                          <li class=" col-sm-4 ackdetail" style=" "><a  style="color:#000; font-weight:bold; " href="/application/applicationobj_list/${response[i]['menu_name']}/${response[i]['application_menu'][j]['menu_name']}/">${response[i]['application_menu'][j]['menu_name']}</a></li>
                        `)
                        }


                   //   for (var j=0;j<response[i]['application_menu'].length;j++)

                      //$('#menu_bar').append('</ul></li>')
                   }

                }



              })

    ////////////////////////////////////////////////////////////////

    $.ajax({
            url:  '/commander/',
            type: "GET",
            dataType: "json",
            data:{"parent_id":"parent_id"},
            success: function(response){

              var index = 0;
              var arrayLength = response.length;
              var tempArray = [];



              for (var i=0;i<response.results.length;i++)
                	{

                    //$('.defencezone').append('<img src="http://192.168.0.6:8000/static/images/downloads_icon.png" height="22px">')




                  }


                }



        })

    //////////////////////////////////?Lates NewsMenuuobjSerializer

                        $.ajax({
                            url:  '/news_detail/',
                            type: "GET",
                            dataType: "json",

                            success: function(response){
                                //$('#news_listss').empty()

                                var news_list = []

                                for(var i=0;i<=response.results.length;i++){
                                 news_list.push(response.results[i]['news_heading'])

                                      if( i < 10)
                                      {
                                        $('#news_listss').append(`${response.results[i]['news_heading']};`)
                                      }
                                      else if ((i > 1) && (i<3)){

                                        $('#news_listss').append(`<br>${response.results[i]['news_heading']};`)


                                      }











                                }


                               // alert(JSON.stringify(response))news_details

                            }

                        })
    ////////////////////////////////////////////
    ///////////////////////////////////////Other Sites//////////

    //////////////////////////////////////////////////////////////

 // openPage('NHQ', this, 'orange')


///////////////////////////////////////////////////////////////////////////////////////


})

function openPage(pageName,elmnt,color) {



  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");

  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }
  document.getElementById(pageName).style.display = "block";
  elmnt.style.backgroundColor = color;
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();


function openPagee(pageName,elmnt,color) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontents");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }
  document.getElementById(pageName).style.display = "block";
  elmnt.style.backgroundColor = color;


  }



function megamyFunction(valu)
{

//   var ids = $(':checkbox:checked').map(function() {
//     return this.id;
//   }).get();

//   var favorite = [];
//               $.each($("input[name='megafol']:checked"), function(){

//                 favorite.push($(this).val());

//             });

var url = "/ackpolicy/?menutype="+ valu
 window.location.href = url;



}

$('#carousel-example-generic').carousel({

  interval: 3000,
  pause: null
})
        var touchSensitivity = 5;
$(".carousel").on("touchstart", function (event) {
    var xClick = event.originalEvent.touches[0].pageX;
    $(this).one("touchmove", function (event) {
        var xMove = event.originalEvent.touches[0].pageX;
        if (Math.floor(xClick - xMove) > touchSensitivity) {
            $(this).carousel('next');
        } else if (Math.floor(xClick - xMove) < -(touchSensitivity)) {
            $(this).carousel('prev');
        }
    });
    $(".carousel").on("touchend", function () {
        $(this).off("touchmove");
    });
});


$('.header2').mouseover(function()
{
  alert("ok")
})
