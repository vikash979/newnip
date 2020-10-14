$(document).ready(function () {

    /* Main Menu DropDown */

    $('ul.lvl0 li').children('.sub').hide();

    function makeTall() {
        $(this).children('.sub').slideDown(200);
        $(this).children('a').toggleClass('active');

    }
    function makeShort() {

        $(this).children('.sub').hide();
        $(this).children('a').toggleClass('active');
    }
    var config1 = {
        over: makeTall, // function = onMouseOver callback (REQUIRED)    
        timeout: 500, // number = milliseconds delay before onMouseOut    
        out: makeShort // function = onMouseOut callback (REQUIRED)    
    };
    $('ul.lvl0 li').hoverIntent(config1);


    /* 4th Level DropDown */

    function showFour() {
        $(this).children('.lvl3').slideDown(200);


    }

    function hideFour() {

        $(this).children('.lvl3').slideUp(200);

    }
    var config2 = {
        over: showFour, // function = onMouseOver callback (REQUIRED)    
        timeout: 0, // number = milliseconds delay before onMouseOut    
        out: hideFour // function = onMouseOut callback (REQUIRED)    
    };
    $('ul.lvl2 li').hoverIntent(config2);






});