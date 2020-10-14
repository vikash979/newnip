$(window).on('load',function(){
alert("ok")
  var aa = {}

  $.ajax({
       url:  '/application/policy/',
       type: "GET",
       dataType: "json",
       //data:{"parent_id":"parent_id"},
        success: function(response){
           for(var i=0;i<response.results.length;i++){
            //for(var i=0;i<3;i++){
            $('#menu2nhw').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey; padding-right:10px;"><i class="fa fa-file-pdf-o" style="font-size:36px;color:#FF6347; border: 1px solid #ddd;
                                          border-radius: 4px;
                                          padding: 5px;
                                          width: auto; border-color: #f7b7c2;"></i></td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><span style=" text-align: justify;overflow: hidden;
  text-overflow: ellipsis;">${response.results[i]['policy_name']}</span></span><p>30 April 2020</p></td></tr>`)
              if(i % 2 == 0){
                $('#publicities').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey"><img src="http://192.168.0.6:8088/static/images/instructionred.png" class="rounded-circle" alt="Cinque Terre" width="50" height="50"></td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><span style="  overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 1; /* number of lines to show */
   -webkit-box-orient: vertical;">${response.results[i]['policy_name']}</span></span><p>30 April 2020</p></td></tr>`)
                if (i <3)
                {
                $('#nhqemsg').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey; padding-right:10px;"><i class="fa fa-file-pdf-o" style="font-size:36px;color:#FF6347; border: 1px solid #ddd;
                                          border-radius: 4px;
                                          padding: 5px;
                                          width: auto; border-color: #f7b7c2;"></i></td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><p style=" text-align: justify;white-space: nowrap;
                                        width: 200px;
                                        overflow: hidden;
                                        text-overflow: ellipsis;
                                        ">${response.results[i]['policy_name']}</p></span><p>30 April 2020</p></td><td><a href="#"><img src="http://192.168.0.6:8088/static/images/downloads_icon.png" height="50px"></a></td></tr>`)
              }
            }
              else
              { if (i <3)
                {
                $('#nhqemsg').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey; padding-right:10px;"><i class="fa fa-file-pdf-o" style="font-size:36px;color:#FF6347; border: 1px solid #ddd; padding-right:2%
                                          border-radius: 4px;
                                          padding: 5px;
                                          width: auto; border-color: #f7b7c2;"></i></td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><p style=" text-align: justify;  white-space: nowrap;
  width: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
  ">${response.results[i]['policy_name']}</p></span><p>30 April 2020</p></td><td><a href="#"><img src="http://192.168.0.6:8088/static/images/downloads_icon.png" height="50px"></a></td></tr>`)
              }
                $('#publicities').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey;"><img src="http://192.168.0.6:8088/static/images/instructionsblue.png" class="rounded-circle" alt="Cinque Terre" width="50" height="50"></td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><span style=" text-align: justify; overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 1; /* number of lines to show */
   -webkit-box-orient: vertical;">${response.results[i]['policy_name']}</span></span><p>30 April 2020</p></td></tr>`)
                //alert("ok")
              }

              $('#menu2eg').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey; padding-right:10px;"><i class="fa fa-file-pdf-o" style="font-size:36px;color:#FF6347; border: 1px solid #ddd;
                                          border-radius: 4px;
                                          padding: 5px;
                                          width: auto; border-color: #f7b7c2;"></i></td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><span style=" text-align: justify;">${response.results[i]['policy_name']}</span></span><p>30 April 2020</p></td></tr>`)

              $('#menu2nhwvng').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey; padding-right:10px;"><i class="fa fa-file-pdf-o" style="font-size:36px;color:#FF6347; border: 1px solid #ddd;
                                          border-radius: 4px;
                                          padding: 5px;
                                          width: auto; border-color: #f7b7c2;"></i></td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><span style=" text-align: justify;">${response.results[i]['policy_name']}</span></span><p>30 April 2020</p></td></tr>`)
                   //publicities").append(`${response.results[i]['file']}</td><td>${response.results.[i]['policy_name']}</td></tr>`)
              }
        }
      })


  ////////////////////////////publication//////////////
              $.ajax({
                  url:  '/application/publication/',
                  type: "GET",
                  dataType: "json",
                  //data:{"parent_id":"parent_id"},
                   success: function(response){

                      for(var i=0;i<response.results.length;i++){
                        if(i % 2 == 0){
                           $('#publication').append(`<tr style="border-bottom:1px dotted grey"><td style="border-bottom:1px dotted grey; padding-right:10px;"><img src="http://192.168.0.6:8088/static/images/man.png" class="rounded-circle" alt="Cinque Terre" width="50" height="50"> </td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><span style=" text-align: justify; overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 1; /* number of lines to show */
   -webkit-box-orient: vertical;">${response.results[i]['ppublication_name']}</span> <p> 30 April 2020</p></td></tr>`)
                         }
                         else{
                          $('#publication').append(`<tr style="border-bottom:1px dotted grey;padding-right:10px;"><td style="border-bottom:1px dotted grey"><img src="http://192.168.0.6:8088/static/images/man2.jpg" class="rounded-circle" alt="Cinque Terre" width="50" height="50"> </td><td style="border-bottom:1px dotted grey; color:#000" width="100%"><span style=" text-align: justify; overflow: hidden;
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
                  url:  '/socialmedia/social_media/',
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
                url:  '/othersiters/menu_details/',
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
                  url:  '/acknowledge/sendjson/',
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
                  url:  '/application/policy/',
                  type: "GET",
                  dataType: "json",
                  //data:{"parent_id":"parent_id"},
                   success: function(response){

                   }
               })

  ///////////////////////////////////////////////////
              $.ajax({
                url:  '/application/menu_detail/',
                type: "GET",
                dataType: "json",
                data:{"parent_id":"parent_id"},
                success: function(response){
                  //alert(JSON.stringify(response))
                   for(var i=0;i<response.length;i++){
                     var ee = '.text-center_'+i
                     $('#menu_bar').append(` <li class="col-sm-2" style="color:#000">${response[i]['menu_name']}<hr>
                        <ul class="menu-inner text-center_${i}"</ul></li>` )
                        var ee = '.text-center_'+i
                        //alert(JSON.stringify(response[i]['application_menu']))
                        for (var j=0;j<response[i]['application_menu'].length;j++)
                        {
                          $(ee).append(`
                          <li><a href="/application/applicationobj_list/${response[i]['menu_name']}/${response[i]['application_menu'][j]['menu_name']}/">${response[i]['application_menu'][j]['menu_name']}</a></li>
                        `)
                        }


                   //   for (var j=0;j<response[i]['application_menu'].length;j++)

                      //$('#menu_bar').append('</ul></li>')
                   }

                }



              })

    ////////////////////////////////////////////////////////////////

    $.ajax({
            url:  '/application/commander/',
            type: "GET",
            dataType: "json",
            data:{"parent_id":"parent_id"},
            success: function(response){

              var index = 0;
    var arrayLength = response.length;
    var tempArray = [];


              //alert(JSON.stringify(response.results))
              $("#defence_zone").empty()
              $("#defence_zone").append(`<h4 class="title"><center>
                   Know Your Officers</center>
                </h4> `)
              $("#firstthumbnail").append(`<ul class="thumbnails" id="thmbnl" data-aos="zoom-out-right" data-aos-easing="linear"></ul>`)
              $('#seconditem').append(`<ul class="thumbnails" id="secthmbnl" data-aos="zoom-in-left"
     data-aos-easing="ease-out-cubic"
     data-aos-duration="2000"></ul>`)
              for (var i=0;i<response.results.length;i++)
                	{
                    $("#defence_zone").append(`<div class="col-lg-3"><div class="team-column style-2">
                      <img src="${response.results[i]['file']}" class="img-fluid circle"  />  <div class="player-name">
                         <div class="desination-2">${response.results[i]['wing_commander_rank']}</div>
                         <h5 >${response.results[i]['wing_commander_name']}</h5>
                         <span class="player-number">${response.results[i]['wing_zone']}</span>
                      </div></div></div>`)
                    if (i < 4)
                    {
                     $("#secthmbnl").append(`<li class=" col-md-3">
                                      <div class="team-column style-2"><img src="${response.results[i]['file']}" class="img-fluid circle" width="254px" height="270px" /><div class="player-name"><div class="desination-2">${response.results[i]['wing_commander_rank']}</div><h5 data-aos="flip-left"
     data-aos-easing="ease-out-cubic"
     data-aos-duration="2000">${response.results[i]['wing_commander_name']}</h5>
                           <span class="player-number">${response.results[i]['wing_zone']}</span></div></div></li>`)


                    }
                    else{

                       $('#thmbnl').append(`<li class=" col-md-3" data-aos="flip-right">
                                      <div class="team-column style-2"  data-aos="zoom-out-right"
     data-aos-easing="ease-out-cubic"
     data-aos-duration="2000"><img src="${response.results[i]['file']}" class="img-fluid circle" width="254px" height="270px" data-aos="flip-up" data-aos-easing="linear" /><div class="player-name" data-aos="flip-left"  data-aos-easing="ease-in-cubic"
     data-aos-duration="2000"><div class="desination-2"  data-aos="zoom-out-right"
     data-aos-easing="ease-out-cubic"
     data-aos-duration="2000">${response.results[i]['wing_commander_rank']}</div><h5 data-aos="zoom-in-left"
     data-aos-easing="ease-out-cubic"
     data-aos-duration="2000">${response.results[i]['wing_commander_name']}</h5>
                           <span class="player-number" data-aos="zoom-out-up"
     data-aos-easing="ease-out-cubic"
     data-aos-duration="2000">${response.results[i]['wing_zone']}</span></div></div></li>`)


    }

                  }


                }



        })

    //////////////////////////////////?Lates NewsMenuuobjSerializer
                        $.ajax({
                            url:  '/application/news_detail/',
                            type: "GET",
                            dataType: "json",

                            success: function(response){
                                $('#news_listss').empty()


                                for(var i=0;i<=response.results.length;i++){

                                        $('#news_listss').append(`<td style="color: #ffcb05; font-weight:bold; font-size:18px;">${response.results[i]['news_heading']}</td>`)



                                             //$('#news_details').append( `<tr><td><i class="fa fa-file-pdf-o" style="color: red"></i><a  href="${response.results[i]['id']}" style="color:#fff" target="_blank">${response.results[i]['news_heading']}</a></td><td></td></tr>`)
                                           //$('#news_listss').append(`<td style="color: red">${response.results[i]['news_heading']}, &nbsp; </td>`)


                                            if(i % 2 == 0){

                                              $('#lastest_obj').append(`<tr class="even" style="border-bottom-color: coral; border-bottom:1px dotted grey;"><td style="color:#ffcb05"><div class="col-lg-12">${response.results[i]['news_heading']}, &nbsp;<br/> </div><hr/></td></tr>`)
                  // rows.className = "even";

                                               }else{
                                                   $('#lastest_obj').append(`<tr class="odd"><td style="color:#ffcb05; border-bottom:1px dotted blue;"><div class="col-lg-12">${response.results[i]['news_heading']}, &nbsp;<br/> </div><hr/></td></tr>`)
                                                // rows.className = "odd";

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

var url = "/acknowledge/ackpolicy/?menutype="+ valu
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
