$(window).on('load',function(){
   //$('.typewrite').attr(`data-type`,`[ "Webinar on Artificial Intelligence from 07 - 09 Oct 20. Webinar details and registration link available at available here, .", "01 Sep 2020 : ENC EDN 17 of 2020 available for download", "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."]`)

  $.ajax({
     url:  '/news_detail/',
     type: "GET",
     dataType: "json",
      success: function(response){
        //alert(response.results.length)
        var news = []

        for (i =0; i <response.results.length; i++)
        {

          news.push(response.results[i]['news_heading'])

        }
        //alert(news)

      //  $('.typewrite').attr(`data-type`,`[ "Webinar on Artificial Intelligence from 07 - 09 Oct 20. Webinar details and registration link available at available here, .", "01 Sep 2020 : ENC EDN 17 of 2020 available for download", "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."]`);
        //alert(JSON.stringify(news))
        //console.log($('.typewrite').attr(`data-type`,`[ "Webinar on Artificial Intelligence from 07 - 09 Oct 20. Webinar details and registration link available at available here, .", "01 Sep 2020 : ENC EDN 17 of 2020 available for download", "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."]`))


        //aler
        newsstring()

        //alert(typeof(`[ "Webinar on Artificial Intelligence from 07 - 09 Oct 20. Webinar details and registration link available at available here, .", "01 Sep 2020 : ENC EDN 17 of 2020 available for download", "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."]`))
        //
      }
    })
    function newsstring()
    {
      $('.typewrite').attr(`data-type`,`[ "Webinar on Artificial Intelligence from 07 - 09 Oct 20. Webinar details and registration link available at available here, .", "01 Sep 2020 : ENC EDN 17 of 2020 available for download", "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."]`)
    }
$('.typewrite').attr(`data-type`,`[ "Webinar on Artificial Intelligence from 07 - 09 Oct 20. Webinar details and registration link available at available here, .", "01 Sep 2020 : ENC EDN 17 of 2020 available for download", "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."]`)
  ////////////////////////////////////////////////navigation Menu//////////////
    $.ajax({
       url:  '/mainnav/',
       type: "GET",
       dataType: "json",
        success: function(response){

          for (i =0; i <response.length; i++)
          {
            var menuurl = response[i]['menu_url']
            if (menuurl == null)
            {
              menuurl  = "#"
            }
            else{
              menuurl = menuurl
            }

            $('#exo-menu').append(`<li class="drop-down"><a href="${menuurl}" style="font-family:WhitneyHTF-Book ; font-weight:bold"> ${response[i]['menu_name']}</a>
              <ul class="drop-down-ul animated fadeIn" style="font-family:WhitneyHTF-Book ; " id="childmenu_${i}">


              </ul>
            <li>`)
             var childid = "childmenu_"+i
             var childmenu = "#"+childid
             /////////////////Application////////////
             if (childid == 'childmenu_0')
             {
               var  application = response[i]['navMenu']
               for (app = 0;app < application.length; app++ )
               {
                 $(childmenu).append(`<li class="flyout-right"><a href="https://cnsforum.indiannavy.mil:43899/Pages/Home.aspx" target="_blank" style="font-weight: 700;
                 font-size: 16px;font-family:WhitneyHTF-Book ;">${application[app]['menu_name']}</a>

                 </li>`)
               }
               $(childmenu).append(`<li class="flyout-right"><a href="https://cnsforum.indiannavy.mil:43899/Pages/Home.aspx" target="_blank" style="font-weight: 700;
               font-size: 16px;font-family:WhitneyHTF-Book ;">Others</a>
               </li>`)
             }
            //Knowledge
             if (childid == 'childmenu_1')
             {
               //alert(JSON.stringify(response[i]['navMenu']))
               var  kowledge = response[i]['navMenu']
              for (ack = 0;ack < kowledge.length; ack++ )
              {
                $(childmenu).append(`<li class="flyout-right"><a href="https://cnsforum.indiannavy.mil:43899/Pages/Home.aspx" target="_blank" style="font-weight: 700;
                font-size: 16px;font-family:WhitneyHTF-Book ;">${kowledge[ack]['menu_name']}</a>
                </li>`)
              }
              $(childmenu).append(`<li class="flyout-right"><a href="https://cnsforum.indiannavy.mil:43899/Pages/Home.aspx" target="_blank" style="font-weight: 700;
              font-size: 16px;font-family:WhitneyHTF-Book ;">Others</a>

              </li>`)

            }
            //Information
             if (childid == 'childmenu_2')
             {
               var  information = response[i]['navMenu']
               for (info = 0;info < information.length; info++ )
               {
                 $(childmenu).append(`<li class="flyout-right"><a href="https://cnsforum.indiannavy.mil:43899/Pages/Home.aspx" target="_blank" style="font-weight: 700;
                 font-size: 16px;font-family:WhitneyHTF-Book ;">${information[info]['menu_name']}</a>

                 </li>`)
               }
               $(childmenu).append(`<li class="flyout-right"><a href="https://cnsforum.indiannavy.mil:43899/Pages/Home.aspx" target="_blank" style="font-weight: 700;
               font-size: 16px;font-family:WhitneyHTF-Book ;">Others</a>
               </li>`)

             }


             //other Navy Sites
              if (childid == 'childmenu_3')
              {
                var  othernavy = response[i]['navMenu']
                for (other = 0;other < othernavy.length; other++ )
                {
                  $(childmenu).append(`<li class="flyout-right"><a href="https://cnsforum.indiannavy.mil:43899/Pages/Home.aspx" target="_blank" style="font-weight: 700;
                  font-size: 16px;font-family:WhitneyHTF-Book ;">${othernavy[other]['menu_name']}</a>

                  </li>`)
                }
                $(childmenu).append(`<li class="flyout-right"><a href="https://cnsforum.indiannavy.mil:43899/Pages/Home.aspx" target="_blank" style="font-weight: 700;
                font-size: 16px;font-family:WhitneyHTF-Book ;">Others</a>
                </li>`)

              }
          }


        }
    })

    //////////////////////////////emessage///////////////////////

})
