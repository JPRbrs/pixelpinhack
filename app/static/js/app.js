$(document).ready(function() {
    $("#button").mouseenter(function(){
	$("#button").fadeTo('fast', 0.5);
    });
    $("#button").mouseleave(function(){
	$("#button").fadeTo('fast', 1);
    });
});

var ractive = new Ractive({
    el: '#container',
    template: '#template',
    data: { name: 'Javi!!' }
});
