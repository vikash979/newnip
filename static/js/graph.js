
$(window).on('load',function(){

var currentLocation = window.location.href;
var knowtype = currentLocation.split("=")
var knowobj = knowtype[1].split("&")
var menutype = knowobj[0]

if (menutype == 'Navy%20Instruction')
{
 menutype = 'Navy Instruction' 
}
else if (menutype == 'Navy%20Orders')
{
 menutype = 'Navy Orders' 
}
else{
 menutype = menutype 
}


//////////////////////////////////Pie Graph/ Start Below//////////////////////////////////////////////////////
 $.ajax({
                  url:  '/graphview/',
                  type: "GET",
                  dataType: "json",
                  data:{"menubar":menutype},
                   success: function(response){
                    //alert(JSON.stringify(response))
                    var pied = response['asd']
                    var pieCounts = []
                    for(var i=0;i < response['asd'].length;i++){
                      
                      Object.keys(response['asd'][i]).forEach(function(key) {
                        //console.table('Key : ' + key + ', Value : ' + data[key])
                           var pie_obj = [key,response['asd'][i][key]]
                           pieCounts.push(pie_obj)

                        })

                    }


                    /////////////////////////////Bar Graph for loop
                    var barknowledge = []
                    var barCount = []
                    for(var i=0;i < response['barhraph'].length;i++){
                      barknowledge.push(response['barhraph'][i]['name'])
                      barCount.push(response['barhraph'][i]['y'])
                    }
                   

                   
                   //alert(JSON.stringify(pieCounts))

                    Highcharts.setOptions({
                        colors: [ '#033b8f', '#75a537', '#24CBE5', '#6f4e37', '#FF9655', '#c19a6b', '#a3a5a7','#7d5a5a', '#ffc785','#8fbbaf','#cb9b42'],
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


                        renderTo: 'cgraphhh',
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
                        text: 'Knowledge'+ menutype+ '  Uses Graph',


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
                            text: 'Number of '+ menutype,
                            fontWeight:'bold',

                        }
                        //max: 4,
                        //categories: categories.map(title => title )
                      },
                      xAxis: {
                        min: 0,
                       // max: 4,

                       fontWeight:'40px',
                        categories: barknowledge.map(title => title, fontWeight =>'bold', fontSize=>24 ),

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
                        data: barCount
                      }]
                      });
                   // Make monochrome colors
                      var pieColors = (function () {
                          var colors = [ '#033b8f', '#75a537', '#24CBE5', '#6f4e37', '#FF9655', '#c19a6b', '#a3a5a7','#baffc9'],
                              base = Highcharts.getOptions().colors[0],
                              i;

                          for (i = 0; i < 10; i += 1) {
                              // Start out with a darkened base color (negative brighten), and end
                              // up with a much brighter color
                              //colors.push(Highcharts.color(base).brighten((i - 3) / 7).get());
                          }
                          //alert(colors)
                          return colors;
                      }());



///////////////////////////////////////////////////////////////////////////////////////////////////



                      Highcharts.chart('containerii', {
                          chart: {
                              plotBackgroundColor: null,
                              plotBorderWidth: null,
                              plotShadow: false,
                              type: 'pie',
                              shadow: {
                                          color: 'rgba(0, 0, 0, 0.1)',
                                          offsetX: 1,
                                          offsetY: 1,
                                          opacity: '1.8',
                                          borderRadius:100,
                                          //backgroundColor:'#033b8f',
                                          width:6,
                                      },
                          },
                          title: {
                              text: 'Knowledge' + menutype + ' Detail'
                          },
                          tooltip: {
                              pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
                          },
                          accessibility: {
                              point: {
                                  valueSuffix: '%'
                              }
                          },
                          plotOptions: {
                              pie: {
                                  allowPointSelect: true,
                                  cursor: 'pointer',
                                  dataLabels: {
                                      enabled: true,
                                      format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                                  }
                              }
                          },
                          series: [{
                              name: 'Brands',
                              colorByPoint: true,
                              data: pied
                          }]
                      });



                   }
                 })

 ///////////////////////////////////End Of New Graph///////////////

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

                         

                          //policyfileobj(dashboard,'Policy')
                          //alert(JSON.stringify(response[i]['ascsubmenu_count']))


                        }


                        if (response[i]['menu_name'] =='Publication')
                        {
                          var pie_obj = [response[i]['menu_name'],response[i]['pie_count']]
                          pieCount.push(pie_obj)
                          //arrCount.push(response[i]['ask_submenues'].length)

                          //var obj_length = response[i]['ask_submenues'].length

                         
                        }

                        if (response[i]['menu_name'] =='Navy Orders')
                        {
                          var pie_obj = [response[i]['menu_name'],response[i]['pie_count']]
                          pieCount.push(pie_obj)
                          
                        }


                        if (response[i]['menu_name'] =='Navy Instruction')
                        {
                          var pie_obj = [response[i]['menu_name'],response[i]['pie_count']]
                          pieCount.push(pie_obj)
                         
                        }
                        if (response[i]['menu_name'] =='GuideLines')
                        {
                          var pie_obj = [response[i]['menu_name'],response[i]['pie_count']]
                          pieCount.push(pie_obj)
                        }

                        if (response[i]['menu_name'] =='Standards')
                        {
                          var pie_obj = [response[i]['menu_name'],response[i]['pie_count']]
                          pieCount.push(pie_obj)
                         
                        }

                    }

//alert(JSON.stringify(pieCount))
                   var dataa  = arr
                   var labels  = graph_lenght


var data = graph_lenght;

var categories = arr;

//var arr  = ['Corona Policy Letter', 'AOCP Policy Letter', 'DACP Policy Letter', 'Karnatka Policy Letter', 'DOCP Policy letter', 'Orissa Policy Letter']
//var categories = arr;
//alert(categories)
//alert(categories)

/////////////////////////////////////////////////////colors: ['#f39c12', '#033b8f', '#ED561B', '#DDDF00', '#24CBE5', '#64E572', '#FF9655', '#FFF263', '#6AF9C4'],




    ////////////////////////////////
   





  }
 })


 

})

function megamyFunction(valu, idd)
{
  alert(idd)
  var url = "/ackpolicy/?menutype="+ valu+ "&mainId=" + idd
   window.location.href = url;

}
