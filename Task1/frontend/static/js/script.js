$(document).ready(function(){
    $("a").on('click', function(event) {
      if (this.hash !== "") {
        event.preventDefault();
        var hash = this.hash;
        console.log($(hash).offset().top+"-"+$('#header').outerHeight()+"+50="+($(hash).offset().top - $('#header').outerHeight()+50))
        $('html, body').animate({
          scrollTop: $(hash).offset().top - $('#header').outerHeight()-150
        }, 800, function(){
          window.location.hash = hash;
        });
      }
    });
  });

  