$(window).on('load',function(){

        $.ajax({
                url:  '/application/commander/',
                type: "GET",
                dataType: "json",
                data:{"parent_id":"parent_id"},
                success: function(response){

                    $('#dsds').html("fdfdfdfd")


                    }
            })


})
