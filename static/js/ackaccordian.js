function megafolder(idd,fileid)
{
  //nested_
  var ackdetail =  'Policy'
  var id_obj = idd.split("_")
  var id_ob = id_obj[1]
  if (fileid==1)
  {var nested = '#nested_'+id_ob
  }
  else
  {var nested = '#nestedmat_'+id_ob
  }
  
  var image = '#img_'+id_ob
  $.ajax({
       url:  '/policyView/'+id_ob+'/',
       type: "GET",
       dataType: "json",
       data:{"menubar":ackdetail, "file_type" : fileid},
       success: function(response){
        

         //var total = response['policy'].length + response['obj'].length-1
        
         $(nested).empty()
         for (var i=0; i<response['policy'].length;i++)
            {
             
                if (response['policy'][i]['id'] != id_ob)
                {
                  
                  $(nested).append(`<li><input type="checkbox" id="c_${response['policy'][i]['id']}" onclick="megafolders(this.id, ${fileid}); " /> <label for="c_${response['policy'][i]['id']}" class="tree_label tablinktree col-lg-12 col-sm-12 col-xs-12"><span style="border-bottom:1px dotted black;  color:#fff; ">${response['policy'][i]['submenu_name']}</span></label><ul class="nested" id="nested_${response['policy'][i]['id']}" ></ul></li>`)
                }
            
            }
            for (var j=0; j<response['obj'].length;j++)
            {
              //alert(JSON.stringify(response['obj']))
              $(nested).append(`<li><a href="http://192.168.0.5:8000${response['obj'][j]['file']}" target="_blank"><label for="c_${response['obj'][j]['id']}" class=" tablinktree col-lg-12 col-sm-12 col-xs-12"><span style="border-bottom:1px dotted black;  color:#fff; ">${response['obj'][j]['submenu_name']}+++${nested}</span></label><a/></li>`)
            }
           
        }
     })
}



function megafolders(idd, fileid, page)
{

  var ackdetail =  'Policy'
  var i;
  var id_obj = idd.split("_")
  var id_ob = id_obj[1]
  var nested = '#nested_'+id_ob
  var nestedd = 'nested_'+id_ob
  var paging = "#paginationdata_"+id_ob
  //alert(nested)
  document.getElementById(idd).focus();
  $.ajax({
       url:  '/policyView/'+id_ob+'/',
       type: "GET",
       dataType: "json",
       data:{"menubar":ackdetail, "file_type" : fileid,"page": page},
       success: function(response){
        //alert(JSON.stringify(response))
         $(nested).empty()
         for (var i=0; i<response['policy'].length;i++)
            {
             
                if (response['policy'][i]['id'] != id_ob)
                {
                  $(nested).append(`<li><input type="checkbox" id="c_${response['policy'][i]['id']}" onclick="megafolders(this.id,${fileid}); " /> <label for="c_${response['policy'][i]['id']}" class="tree_label tablinktree col-lg-12 col-sm-12 col-xs-12"><span style="border-bottom:1px dotted black;  color:#fff; ">${response['policy'][i]['submenu_name']}</span></label><ul class="nested" id="nested_${response['policy'][i]['id']}" ></ul></li>`)
                }
            
            }
            for (var j=0; j<response['obj'].length;j++)
            {

              $(nested).append(`<li><a href="http://192.168.0.5:8000${response['obj'][j]['file']}" > <label  class=" tablinktree col-lg-12 col-sm-12 col-xs-12"><span style="border-bottom:1px dotted black;  color:#fff; ">${response['obj'][j]['submenu_name']}-</span></label></a></li>`)
            }
            $(nested).append(`<div class="col-lg-6 col-sm-12 col-xs-12 pagination"  id="paginationdata_${id_ob}" style="">

                                        </div>`)
          var pagi_length =response['pagination']['numpages']+1


           if (response['pagination']['numpages'] > 0)
          {
            
            if (response['pagination']['know_user_changes'] == true)
            {
              //alert("ok")
              $(paging).append(`<a href="#">&laquo;</a>`)
              if(response['pagination']['know_previous']==true){
                $(paging).append(`<a href="javascript:void(0)" onclick="megafolders('${nestedd}','${fileid}',${response['pagination']['know_previous_page']})">prev</a>`)
              }

              for (var i=1;i<pagi_length;i++)
               {
                if (response['pagination']['current_page']==i)
                {
                    
                   $(paging).append(`<a href="javascript:void(0)" class="selected active">${i}</a>`)
                }  
                else{
                    
                   $(paging).append(`<a href="javascript:void(0)" class="paginate" id="${i}" onclick="megafolders('${nestedd}','${fileid}','${i}');">${i}</a>`)
                }
               }
               if (response['pagination']['know_next']==true)
                       {
                           $(paging).append(`<a href="javascript:void(0)" onclick="megafolders('${nestedd}','${fileid}',${response['pagination']['know_next_page_number']});">next</a>`)
                       }
                       document.getElementById(paging).focus();
            }
          }



          ///////////////////////////

           // $(paging).append(`hjhjhjhj`)
           
        }
     })
}

function filepermission(vale)
{

  var modal = document.getElementById("myModal");

  // Get the button that opens the modal
  var btn = document.getElementById("myBtn");

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];
  if ((vale == '1') || (vale == '2') || (vale == '3') || (vale == '4'))
  {
    $('#permissiontype').val(vale)
    modal.style.display = "block";
    $.ajax({
       url:  '/user_list/',
       type: "GET",
       dataType: "json",
       //data:{"menubar":ackdetail, "file_type" : fileid,"page": page},
       success: function(response){
        $('#user_ob').empty()
        $('#user_ob').append(`<option >--Select User</option>`)
        for (var i = 0; i < response.length; i++)
        {
         // alert(JSON.stringify(response[i]['username']))
         $('#user_ob').append(`<option value="${response[i]['id']}">${response[i]['username']}</option>`)
        }
       }
     })

  }
  else{
    modal.style.display = "none";
  }

  span.onclick = function() {
    modal.style.display = "none";
  }
}