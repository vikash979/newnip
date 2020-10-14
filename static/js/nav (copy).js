
$(window).on('load',function(){


//alert(screen.width)

 $.ajax({
                  url:  '/ack_detail/',
                  type: "GET",
                  dataType: "json",
                  //data:{"parent_id":"parent_id"},
                   success: function(response){

                     //alert(JSON.stringify(response))
                    var arr = [];
                    var arrCount = []
                    policy_name = []
                    policy_count = []
                    publication_name = []
                    publication_count = []
                    graph_lenght = []
                    var pieCount  = []
                    var pie_data = []

                    for(var i=0;i < response.length;i++){
                      //alert(JSON.stringify(response[i]['pie_count']))
                      var public_data = i+1
                      var dashboard = '#dashbdcount_'+public_data

                      arr.push(response[i]['menu_name'])
                      for (var graph_id = 0; graph_id<response[i]['ask_submenudetail'].length;graph_id++)

                      {
                        //alert(JSON.stringify(response[i]['ask_submenudetail'][graph_id]))
                        if (response[i]['ask_submenudetail'][graph_id]['menu_detail'] == '1')
                        {

                         graph_lenght.push(response[i]['ask_submenudetail'][graph_id]['graph_detail'].length)
                        }
                        if (response[i]['ask_submenudetail'][graph_id]['menu_detail'] == '2')
                        {
                         graph_lenght.push(response[i]['ask_submenudetail'][graph_id]['graph_detail'].length)
                        }
                        if (response[i]['ask_submenudetail'][graph_id]['menu_detail'] == '3')
                        {
                         graph_lenght.push(response[i]['ask_submenudetail'][graph_id]['graph_detail'].length)
                        }
                         if (response[i]['ask_submenudetail'][graph_id]['menu_detail'] == '4')
                        {
                         graph_lenght.push(response[i]['ask_submenudetail'][graph_id]['graph_detail'].length)
                        }
                        if (response[i]['ask_submenudetail'][graph_id]['menu_detail'] == '5')
                        {
                         graph_lenght.push(response[i]['ask_submenudetail'][graph_id]['graph_detail'].length)
                        }
                        if (response[i]['ask_submenudetail'][graph_id]['menu_detail'] == '6')
                        {
                         graph_lenght.push(response[i]['ask_submenudetail'][graph_id]['graph_detail'].length)
                        }
                        if (response[i]['ask_submenudetail'][graph_id]['menu_detail'] == '7')
                        {
                         graph_lenght.push(response[i]['ask_submenudetail'][graph_id]['graph_detail'].length)
                        }
                        if (response[i]['ask_submenudetail'][graph_id]['menu_detail'] == '8')
                        {
                         graph_lenght.push(response[i]['ask_submenudetail'][graph_id]['graph_detail'].length)
                        }
                      }
                        if (response[i]['menu_name'] =='Policy')
                        {
                          var pie_obj = [response[i]['menu_name'],response[i]['pie_count']]
                          pieCount.push(pie_obj)
                          pie_data.push(response[i]['pie_count'])

                          $('#ack_men').append(`<div class="col-lg-4 col-sm-12 col-xs-12">
                             <aside id="sidebar" class="left-bar" style="background:#dde1d0; padding-top:0px; box-shadow: 3px 3px 5px #292929;">
                                <div class="banner-sidebar " style="border-top-left-radius: 30px; border-top-right-radius: 30px;">
                                  <span id="guide"><div class="headerinformation">

                                  <!--Content before waves-->
                                  <div class="inner-headerpolicy flex">
                                  <!--Just the logo.. Don't mind this-->

                                  <h4 style="font-weight:bold;color:#fff; font-weight:bold; height:40px; padding-top: 11px;">Policy</h4>
                                  </div>

                                  <!--Waves Container-->
                                  <div>
                                  <svg class="wavespolicy" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                                  viewBox="0 24 150 28" preserveAspectRatio="none" shape-rendering="auto">
                                  <defs>
                                  <path id="gentle-wave" d="M-160 44c30 0 58-18 88-18s 58 18 88 18 58-18 88-18 58 18 88 18 v44h-352z" />
                                  </defs>
                                  <g class="parallax">
                                  <use xlink:href="#gentle-wave" x="48" y="0" fill="rgba(255,255,255,0.7" />
                                  <use xlink:href="#gentle-wave" x="48" y="3" fill="rgba(255,255,255,0.5)" />
                                  <use xlink:href="#gentle-wave" x="48" y="5" fill="rgba(255,255,255,0.3)" />
                                  <use xlink:href="#gentle-wave" x="48" y="7" fill="#fff" />
                                  </g>
                                  </svg>
                                  </div>
                                  <!--Waves end-->

                                  </div></span>
                                  <div class="col-lg-12 col-sm-12 col-xs-12" id="dashbdcount_${public_data}" style="background-image:url(http://159.12.107.251:8000/static/images/KM-bg.png)"></div>
                                    <table><tbody id="public_obj"><tr><td></td></tr></tbody>
                                          <tr><td><button onclick="megamyFunction('${response[i]['menu_name']}')" class="thbg-color" style="background: #9f4545; background-color: #9f4545;
                                            border: none;
                                            color: white;
                                            padding: 0px 8px;margin: 5px;
                                            text-align: center;
                                            text-decoration: none;
                                            display: inline-block;
                                            font-size: 16px;

                                            border-radius:10px;
                                            cursor: pointer;" id="myBtn">Read more</button></td></tr></table>
                                 </div>
                             </aside>

                          </div>`)

                          policyfileobj(dashboard,'Policy')
                          //alert(JSON.stringify(response[i]['ascsubmenu_count']))


                        }


                        if (response[i]['menu_name'] =='Publication')
                        {
                          pie_data.push(response[i]['pie_count'])
                          var pie_obj = [response[i]['menu_name'],response[i]['pie_count']]
                          pieCount.push(pie_obj)
                          //arrCount.push(response[i]['ask_submenues'].length)

                          //var obj_length = response[i]['ask_submenues'].length

                          $('#ack_men').append(`<div class="col-lg-4 col-sm-12 col-xs-12">
                             <aside id="sidebar" class="left-bar" style="background:#dde1d0; padding-top:0px; box-shadow: 3px 3px 5px #292929;">
                                <div class="banner-sidebar " style="border-top-left-radius: 30px; border-top-right-radius: 30px;">
                                  <span id="guide"><div class="headerpublication">

                                  <!--Content before waves-->
                                  <div class="inner-headerpolicy flex">
                                  <!--Just the logo.. Don't mind this-->

                                  <h4 style="font-weight:bold;color:#fff; font-weight:bold; height:40px; padding-top: 11px;">Publication</h4>
                                  </div>

                                  <!--Waves Container-->
                                  <div>
                                  <svg class="wavespolicy" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                                  viewBox="0 24 150 28" preserveAspectRatio="none" shape-rendering="auto">
                                  <defs>
                                  <path id="gentle-wave" d="M-160 44c30 0 58-18 88-18s 58 18 88 18 58-18 88-18 58 18 88 18 v44h-352z" />
                                  </defs>
                                  <g class="parallax">
                                  <use xlink:href="#gentle-wave" x="48" y="0" fill="rgba(255,255,255,0.7" />
                                  <use xlink:href="#gentle-wave" x="48" y="3" fill="rgba(255,255,255,0.5)" />
                                  <use xlink:href="#gentle-wave" x="48" y="5" fill="rgba(255,255,255,0.3)" />
                                  <use xlink:href="#gentle-wave" x="48" y="7" fill="#fff" />
                                  </g>
                                  </svg>
                                  </div>
                                  <!--Waves end-->

                                  </div></span>
                                  <div class="col-lg-12 col-sm-12 col-xs-12" id="dashbdcount_${public_data}" style="background-image:url(http://159.12.107.251:8000/static/images/KM-bg.png)"></div>
                                    <table><tbody id="public_obj"><tr><td></td></tr></tbody>
                                          <tr><td><button onclick="megamyFunction('${response[i]['menu_name']}')" class="thbg-color" style="background: #9f4545; background-color: #9f4545;
                                            border: none;
                                            color: white;
                                            padding: 0px 8px;margin: 5px;
                                            text-align: center;
                                            text-decoration: none;
                                            display: inline-block;
                                            font-size: 16px;

                                            border-radius:10px;
                                            cursor: pointer;" id="myBtn">Read more</button></td></tr></table>




                                 </div>




                             </aside>

                          </div>`)
                          policyfileobj(dashboard,'Publication')
                        }

                        if (response[i]['menu_name'] =='Navy Orders')
                        {
                          pie_data.push(response[i]['pie_count'])
                          var pie_obj = [response[i]['menu_name'],response[i]['pie_count']]
                          pieCount.push(pie_obj)
                          $('#ack_men').append(`<div class="col-lg-4 col-sm-12 col-xs-12">
                             <aside id="sidebar" class="left-bar" style="background:#dde1d0; padding-top:0px; box-shadow: 3px 3px 5px #292929;">
                                <div class="banner-sidebar " style="border-top-left-radius: 30px; border-top-right-radius: 30px;">
                                  <span id="guide"><div class="headerpolicy">

                                  <!--Content before waves-->
                                  <div class="inner-headerpolicy flex">
                                  <!--Just the logo.. Don't mind this-->

                                  <h4 style="font-weight:bold;color:#fff; font-weight:bold; height:40px; padding-top: 11px;">${response[i]['menu_name']}</h4>
                                  </div>

                                  <!--Waves Container-->
                                  <div>
                                  <svg class="wavespolicy" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                                  viewBox="0 24 150 28" preserveAspectRatio="none" shape-rendering="auto">
                                  <defs>
                                  <path id="gentle-wave" d="M-160 44c30 0 58-18 88-18s 58 18 88 18 58-18 88-18 58 18 88 18 v44h-352z" />
                                  </defs>
                                  <g class="parallax">
                                  <use xlink:href="#gentle-wave" x="48" y="0" fill="rgba(255,255,255,0.7" />
                                  <use xlink:href="#gentle-wave" x="48" y="3" fill="rgba(255,255,255,0.5)" />
                                  <use xlink:href="#gentle-wave" x="48" y="5" fill="rgba(255,255,255,0.3)" />
                                  <use xlink:href="#gentle-wave" x="48" y="7" fill="#fff" />
                                  </g>
                                  </svg>
                                  </div>
                                  <!--Waves end-->

                                  </div></span>
                                  <div class="col-lg-12 col-sm-12 col-xs-12" id="dashbdcount_${public_data}" style="background-image:url(http://159.12.107.251:8000/static/images/KM-bg.png)"></div>
                                    <table><tbody id="public_obj"><tr><td></td></tr></tbody>
                                          <tr><td><button class="thbg-color" style="background: #9f4545; background-color: #9f4545;
                                            border: none;
                                            color: white;
                                            padding: 0px 8px;margin: 5px;
                                            text-align: center;
                                            text-decoration: none;
                                            display: inline-block;
                                            font-size: 16px;

                                            border-radius:10px;
                                            cursor: pointer;" id="myBtn" onclick="megamyFunction('${response[i]['menu_name']}')">Read more</button></td></tr></table>




                                 </div>




                             </aside>

                          </div>`)
                          policyfileobj(dashboard,'Navy Orders')
                        }


                        if (response[i]['menu_name'] =='Navy Instruction')
                        {
                          pie_data.push(response[i]['pie_count'])
                          var pie_obj = [response[i]['menu_name'],response[i]['pie_count']]
                          pieCount.push(pie_obj)
                          $('#ack_men').append(`<div class="col-lg-4 col-sm-12 col-xs-12">
                             <aside id="sidebar" class="left-bar" style="background:#dde1d0; padding-top:0px; box-shadow: 3px 3px 5px #292929;">
                                <div class="banner-sidebar " style="border-top-left-radius: 30px; border-top-right-radius: 30px;">
                                  <span id="guide"><div class="headerinformation">

                                  <!--Content before waves-->
                                  <div class="inner-headerpolicy flex">
                                  <!--Just the logo.. Don't mind this-->

                                  <h4 style="font-weight:bold;color:#fff; font-weight:bold; height:40px; padding-top: 11px;">${response[i]['menu_name']}</h4>
                                  </div>

                                  <!--Waves Container-->
                                  <div>
                                  <svg class="wavespolicy" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                                  viewBox="0 24 150 28" preserveAspectRatio="none" shape-rendering="auto">
                                  <defs>
                                  <path id="gentle-wave" d="M-160 44c30 0 58-18 88-18s 58 18 88 18 58-18 88-18 58 18 88 18 v44h-352z" />
                                  </defs>
                                  <g class="parallax">
                                  <use xlink:href="#gentle-wave" x="48" y="0" fill="rgba(255,255,255,0.7" />
                                  <use xlink:href="#gentle-wave" x="48" y="3" fill="rgba(255,255,255,0.5)" />
                                  <use xlink:href="#gentle-wave" x="48" y="5" fill="rgba(255,255,255,0.3)" />
                                  <use xlink:href="#gentle-wave" x="48" y="7" fill="#fff" />
                                  </g>
                                  </svg>
                                  </div>
                                  <!--Waves end-->

                                  </div></span>
                                    <div class="col-lg-12 col-sm-12 col-xs-12" id="dashbdcount_${public_data}" style="background-image:url(http://159.12.107.251:8000/static/images/KM-bg.png)"></div>
                                    <table><tbody id="public_obj"><tr><td></td></tr></tbody>
                                          <tr><td><button onclick="megamyFunction('${response[i]['menu_name']}')" class="thbg-color" style="background: #9f4545; background-color: #9f4545;
                                            border: none;
                                            color: white;
                                            padding: 0px 8px;margin: 5px;
                                            text-align: center;
                                            text-decoration: none;
                                            display: inline-block;
                                            font-size: 16px;

                                            border-radius:10px;
                                            cursor: pointer;" id="myBtn">Read more</button></td></tr></table>




                                 </div>




                             </aside>

                          </div>`)
                          policyfileobj(dashboard,'Navy Instruction')
                        }
                        if (response[i]['menu_name'] =='GuideLines')
                        {
                          pie_data.push(response[i]['pie_count'])
                          var pie_obj = [response[i]['menu_name'],response[i]['pie_count']]
                          pieCount.push(pie_obj)
                          $('#ack_men').append(`<div class="col-lg-4 col-sm-12 col-xs-12">
                             <aside id="sidebar" class="left-bar" style="background:#dde1d0; padding-top:0px; box-shadow: 3px 3px 5px #292929;">
                                <div class="banner-sidebar " style="border-top-left-radius: 30px; border-top-right-radius: 30px;">
                                  <span id="guide"><div class="headerpublication">

                                  <!--Content before waves-->
                                  <div class="inner-headerpolicy flex">
                                  <!--Just the logo.. Don't mind this-->

                                  <h4 style="font-weight:bold;color:#fff; font-weight:bold; height:40px; padding-top: 11px;">${response[i]['menu_name']}</h4>
                                  </div>

                                  <!--Waves Container-->
                                  <div>
                                  <svg class="wavespolicy" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                                  viewBox="0 24 150 28" preserveAspectRatio="none" shape-rendering="auto">
                                  <defs>
                                  <path id="gentle-wave" d="M-160 44c30 0 58-18 88-18s 58 18 88 18 58-18 88-18 58 18 88 18 v44h-352z" />
                                  </defs>
                                  <g class="parallax">
                                  <use xlink:href="#gentle-wave" x="48" y="0" fill="rgba(255,255,255,0.7" />
                                  <use xlink:href="#gentle-wave" x="48" y="3" fill="rgba(255,255,255,0.5)" />
                                  <use xlink:href="#gentle-wave" x="48" y="5" fill="rgba(255,255,255,0.3)" />
                                  <use xlink:href="#gentle-wave" x="48" y="7" fill="#fff" />
                                  </g>
                                  </svg>
                                  </div>
                                  <!--Waves end-->

                                  </div></span>
                                  <div class="col-lg-12 col-sm-12 col-xs-12" id="dashbdcount_${public_data}" style="background-image:url(http://159.12.107.251:8000/static/images/KM-bg.png)"></div>
                                    <table><tbody id="public_obj"><tr><td></td></tr></tbody>
                                          <tr><td><button onclick="megamyFunction('${response[i]['menu_name']}')" class="thbg-color" style="background: #9f4545; background-color: #9f4545;
                                            border: none;
                                            color: white;
                                            padding: 0px 8px;margin: 5px;
                                            text-align: center;
                                            text-decoration: none;
                                            display: inline-block;
                                            font-size: 16px;

                                            border-radius:10px;
                                            cursor: pointer;" id="myBtn">Read more</button></td></tr></table>




                                 </div>




                             </aside>

                          </div>`)
                          policyfileobj(dashboard,'GuideLines')
                        }

                        if (response[i]['menu_name'] =='Standards')
                        {
                          pie_data.push(response[i]['pie_count'])
                          var pie_obj = [response[i]['menu_name'],response[i]['pie_count']]
                          pieCount.push(pie_obj)
                          $('#ack_men').append(`<div class="col-lg-4 col-sm-12 col-xs-12">
                             <aside id="sidebar" class="left-bar" style="background:#dde1d0; padding-top:0px; box-shadow: 3px 3px 5px #292929;">
                                <div class="banner-sidebar " style="border-top-left-radius: 30px; border-top-right-radius: 30px;">
                                  <span id="guide"><div class="headerpolicy">

                                  <!--Content before waves-->
                                  <div class="inner-headerpolicy flex">
                                  <!--Just the logo.. Don't mind this-->

                                  <h4 style="font-weight:bold;color:#fff; font-weight:bold; height:40px; padding-top: 11px;">${response[i]['menu_name']}</h4>
                                  </div>

                                  <!--Waves Container-->
                                  <div>
                                  <svg class="wavespolicy" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                                  viewBox="0 24 150 28" preserveAspectRatio="none" shape-rendering="auto">
                                  <defs>
                                  <path id="gentle-wave" d="M-160 44c30 0 58-18 88-18s 58 18 88 18 58-18 88-18 58 18 88 18 v44h-352z" />
                                  </defs>
                                  <g class="parallax">
                                  <use xlink:href="#gentle-wave" x="48" y="0" fill="rgba(255,255,255,0.7" />
                                  <use xlink:href="#gentle-wave" x="48" y="3" fill="rgba(255,255,255,0.5)" />
                                  <use xlink:href="#gentle-wave" x="48" y="5" fill="rgba(255,255,255,0.3)" />
                                  <use xlink:href="#gentle-wave" x="48" y="7" fill="#fff" />
                                  </g>
                                  </svg>
                                  </div>
                                  <!--Waves end-->

                                  </div></span>
                                  <div class="col-lg-12 col-sm-12 col-xs-12" id="dashbdcount_${public_data}" style="background-image:url(http://159.12.107.251:8000/static/images/KM-bg.png)"></div>
                                    <table><tbody id="public_obj"><tr><td></td></tr></tbody>
                                          <tr><td><button onclick="megamyFunction('${response[i]['menu_name']}')" class="thbg-color" style="background: #9f4545; background-color: #9f4545;
                                            border: none;
                                            color: white;
                                            padding: 0px 8px;margin: 5px;
                                            text-align: center;
                                            text-decoration: none;
                                            display: inline-block;
                                            font-size: 16px;

                                            border-radius:10px;
                                            cursor: pointer;" id="myBtn">Read more</button></td></tr></table>




                                 </div>




                             </aside>

                          </div>`)
                          policyfileobj(dashboard,'Standards')
                        }

                    }

//alert(JSON.stringify(pieCount))
                   var dataa  = arr
                   var labels  = graph_lenght

alert(pie_data)
var data = graph_lenght;

var categories = arr;
//alert(JSON.stringify(data))


/////////////////////////////////////////////////////colors: ['#f39c12', '#033b8f', '#ED561B', '#DDDF00', '#24CBE5', '#64E572', '#FF9655', '#FFF263', '#6AF9C4'],

Highcharts.setOptions({
        colors: [ '#033b8f', '#75a537', '#24CBE5', '#6f4e37', '#FF9655', '#c19a6b', '#a3a5a7'],
        plotOptions: {
            bar: {
                colorByPoint: true
            }

        },
        fontWeight:'bold',
        fontSize:'24',

    });


    var chart = new Highcharts.Chart({
      chart: {
        //backgroundColor:'#AFDEF9',
        fontWeight:'bold',
        fontSize:'24',


        renderTo: 'ccontainer',
        shadow: {
                color: 'rgba(0, 0, 0, 0.1)',
                offsetX: 1,
                offsetY: 1,
                opacity: '1.8',
                borderRadius:100,
                //backgroundColor:'#033b8f',
                width:6,
            },
        margin: 100,
        type: 'bar',
        options3d: {
          enabled: true,
          // alpha: 6,
          // beta: 10,
          // depth: 200,
          viewDistance: 4,
          fontWeight:'bold',
          fontSize:'24',
          fitToPlot: false,
          frame: {
            bottom: {
              size: 1,
              color: 'rgba(0,0,0,0.02)'
            },
            back: {
              size: 1,
              color: 'rgba(0,0,0,0.04)'
            },
            side: {
              size: 1,
              color: 'rgba(0,0,0,0.06)'
            }
          }
        }
      },
      title: {
        text: 'Knowledge Portal Uses Graph',


      },

      subtitle: {
        text: ''
      },
       plotOptions: {
            line: {
                marker: {
                    enabled: true
                }
            }
        },
      yAxis: {
        min: 0,
        fontWeight:'bold',

            title: {
            text: 'USERS VISITED',
            fontWeight:'bold',

        }
        //max: 4,
        //categories: categories.map(title => title )
      },
      xAxis: {
        min: 0,
       // max: 4,

       fontWeight:'40px',
        categories: categories.map(title => title, fontWeight =>'bold', fontSize=>24 ),

        text_fonts:'24'

      },
      zAxis: {
        min: 0,
        //max: 4,
        //categories: categories.map(title => title )
      },
      legend: {
        enabled: false
      },
      series: [{
        name: 'User Visited',
        //colorByPoint: true,
        data: data
      }]
    });

    var chart = new Highcharts.Chart({
      chart: {
        //backgroundColor:'#AFDEF9',
        fontWeight:'bold',
        fontSize:'24',


        renderTo: 'ccontainers',
        shadow: {
                color: 'rgba(0, 0, 0, 0.1)',
                offsetX: 1,
                offsetY: 1,
                opacity: '1.8',
                borderRadius:100,
                //backgroundColor:'#033b8f',
                width:6,
            },
        margin: 100,
        type: 'pie',
        options3d: {
          enabled: true,
          // alpha: 6,
          // beta: 10,
          // depth: 200,
          viewDistance: 4,
          fontWeight:'bold',
          fontSize:'24',
          fitToPlot: false,
          frame: {
            bottom: {
              size: 1,
              color: 'rgba(0,0,0,0.02)'
            },
            back: {
              size: 1,
              color: 'rgba(0,0,0,0.04)'
            },
            side: {
              size: 1,
              color: 'rgba(0,0,0,0.06)'
            }
          }
        }
      },
      title: {
        text: 'Knowledge Portal Uses Graph',


      },

      subtitle: {
        text: ''
      },
       plotOptions: {
            line: {
                marker: {
                    enabled: true
                }
            }
        },
      yAxis: {
        min: 0,
        fontWeight:'bold',

            title: {
            text: 'USERS VISITED',
            fontWeight:'bold',

        }
        //max: 4,
        //categories: categories.map(title => title )
      },
      xAxis: {
        min: 0,
       // max: 4,

       fontWeight:'40px',
        categories: categories.map(title => title, fontWeight =>'bold', fontSize=>24 ),

        text_fonts:'24'

      },
      zAxis: {
        min: 0,
        //max: 4,
        //categories: categories.map(title => title )
      },
      legend: {
        enabled: false
      },
      series: [{
        name: 'User Visited',
        //colorByPoint: true,
        data: data
      }]
    });

    ////////////////////////////////

    Highcharts.chart('ccontainerss', {
        chart: {
            type: 'pie',
            option3d : {
              enabled: true,
              alpha:45,
              beta:0
            }
        },
        title: {
            text: 'Number Of Knowledge'
        },
        xAxis: {
            categories: arr
        },
        accessibility :
        {
          point:
          {
            valueSuffix : '%'
          }
        },

        yAxis: {
            min: 0,
            title: {
                text: 'Knowledge Portal'
            }
        },
        legend: {
            reversed: true
        },
        plotOptions: {
          pie : {
            allowPointSelect : true,
            cursor : 'pointer',
            depth :35,
            dataLabels:{
              enabled: true,
              format : '{point.name}'
            }
          },

        },
        series: [{

            // data :[['Policy', 44.0],
            // ['Publication', 15.0],
            // ['Navy Orders', 10.0],
            // ['Navy Instruction', 41.0],
            // ['Guidelines', 18.0],


          //]
          data : pieCount
        }]
    });





  }
 })


 ////////////////////////////////////////////////////


 function policyfileobj(policyId, knowmenu)
 {


    $.ajax({
      url:  '/knowpubmenu/',
      type: "GET",
      dataType: "json",
      data:{"menu":knowmenu},
       success: function(response){
         var piegraph =[]


         for (kk = 0; kk <response.data.length; kk ++ )
         {

           if (knowmenu == 'Standards')
           {
             $(policyId).append(`<div class="col-lg-12 col-sm-12 col-xs-12"  style="padding-top:3%; border-bottom:1px solid #8080802e"  ><div class="col-lg-2 col-sm-2 col-xs-2"><a href="http://159.12.107.251:8000${response.data[kk]['file']}" target='__blank'><i class="fa fa-file-pdf-o oranges" style="font-size:15px;color:#FF6347; border: 1px solid #ddd;
                                     border-radius: 4px;
                                     padding: 5px;
                                     width: auto; border-color: #f7b7c2; padding:10px; 10px  10px 10px"></i></a> </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="http://159.12.107.251:8000${response.data[kk]['file']}" target="__blank" style=" color:#000; text-align: justify; overflow: hidden;
                                           text-overflow: ellipsis;
                                           display: -webkit-box;
                                           -webkit-line-clamp: 1; /* number of lines to show */
                                           -webkit-box-orient: vertical;">${response.data[kk]['submenu_name']}</a></div></div>`)

           }
            if (knowmenu == 'Policy')

           {
             $(policyId).append(`<div class="col-lg-12 col-sm-12 col-xs-12"  style="padding-top:3%; border-bottom:1px solid #8080802e; "  ><div class="col-lg-2 col-sm-2 col-xs-2"><a href="http://159.12.107.251:8000${response.data[kk]['file']}" target='__blank'><i class="fa fa-file-pdf-o oranges" style="font-size:15px;color:#FF6347; border: 1px solid #ddd;
                                     border-radius: 4px;
                                     padding: 5px;
                                     width: auto; border-color: #f7b7c2; padding:10px; 10px  10px 10px"></i></a> </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="http://159.12.107.251:8000${response.data[kk]['file']}" target="__blank" style=" color:#000; text-align: justify; overflow: hidden;
                 text-overflow: ellipsis;
                 display: -webkit-box;
                 -webkit-line-clamp: 1; /* number of lines to show */
                 -webkit-box-orient: vertical;">${response.data[kk]['submenu_name']}</a></div></div>`)
               }
            if (knowmenu == 'Publication')
            {
              $(policyId).append(`<div class="col-lg-12 col-sm-12 col-xs-12"  style="padding-top:3%; border-bottom:1px solid #8080802e; "  ><div class="col-lg-2 col-sm-2 col-xs-2"><a href="http://159.12.107.251:8000${response.data[kk]['file']}" target='__blank'><i class="fa fa-file-pdf-o oranges" style="font-size:15px;color:#FF6347; border: 1px solid #ddd;
                                      border-radius: 4px;
                                      padding: 5px;
                                      width: auto; border-color: #f7b7c2; padding:10px; 10px  10px 10px"></i></a> </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="http://159.12.107.251:8000${response.data[kk]['file']}" target="__blank" style=" color:#000; text-align: justify; overflow: hidden;
                  text-overflow: ellipsis;
                  display: -webkit-box;
                  -webkit-line-clamp: 1; /* number of lines to show */
                  -webkit-box-orient: vertical;">${response.data[kk]['submenu_name']}</a></div></div>`)
                }
           if (knowmenu == 'Navy Orders')
           {

             $(policyId).append(`<div class="col-lg-12 col-sm-12 col-xs-12"  style="padding-top:3%; border-bottom:1px solid #8080802e; "  ><div class="col-lg-2 col-sm-2 col-xs-2"><a href="http://159.12.107.251:8000${response.data[kk]['file']}" target='__blank'><i class="fa fa-file-pdf-o oranges" style="font-size:15px;color:#FF6347; border: 1px solid #ddd;
                                     border-radius: 4px;
                                     padding: 5px;
                                     width: auto; border-color: #f7b7c2; padding:10px; 10px  10px 10px"></i></a> </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="http://159.12.107.251:8000${response.data[kk]['file']}" target="__blank" style=" color:#000; text-align: justify; overflow: hidden;
                 text-overflow: ellipsis;
                 display: -webkit-box;
                 -webkit-line-clamp: 1; /* number of lines to show */
                 -webkit-box-orient: vertical;">${response.data[kk]['submenu_name']}</a></div></div>`)
               }

            if (knowmenu == 'Navy Instruction')
            {

              $(policyId).append(`<div class="col-lg-12 col-sm-12 col-xs-12"  style="padding-top:3%; border-bottom:1px solid #8080802e; "  ><div class="col-lg-2 col-sm-2 col-xs-2"><a href="http://159.12.107.251:8000${response.data[kk]['file']}" target='__blank'><i class="fa fa-file-pdf-o oranges" style="font-size:15px;color:#FF6347; border: 1px solid #ddd;
                                      border-radius: 4px;
                                      padding: 5px;
                                      width: auto; border-color: #f7b7c2; padding:10px; 10px  10px 10px"></i></a> </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="http://159.12.107.251:8000${response.data[kk]['file']}" target="__blank" style=" color:#000; text-align: justify; overflow: hidden;
                  text-overflow: ellipsis;
                  display: -webkit-box;
                  -webkit-line-clamp: 1; /* number of lines to show */
                  -webkit-box-orient: vertical;">${response.data[kk]['submenu_name']}</a></div></div>`)
                }
            if (knowmenu == 'GuideLines')
            {

              $(policyId).append(`<div class="col-lg-12 col-sm-12 col-xs-12"  style="padding-top:3%; border-bottom:1px solid #8080802e; "  ><div class="col-lg-2 col-sm-2 col-xs-2"><a href="http://159.12.107.251:8000${response.data[kk]['file']}" target='__blank'><i class="fa fa-file-pdf-o oranges" style="font-size:15px;color:#FF6347; border: 1px solid #ddd;
                                      border-radius: 4px;
                                      padding: 5px;
                                      width: auto; border-color: #f7b7c2; padding:10px; 10px  10px 10px"></i></a> </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="http://159.12.107.251:8000${response.data[kk]['file']}" target="__blank" style=" color:#000; text-align: justify; overflow: hidden;
                  text-overflow: ellipsis;
                  display: -webkit-box;
                  -webkit-line-clamp: 1; /* number of lines to show */
                  -webkit-box-orient: vertical;">${response.data[kk]['submenu_name']}</a></div></div>`)
                }
           //





         }
       }

     })
 }

})

function megamyFunction(valu)
{
  var url = "/ackpolicy/?menutype="+ valu
   window.location.href = url;

}
