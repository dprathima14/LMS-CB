// Keep track of our instantiated slideshows in case
// we need to manipulate them later
window.slideshows = [];

var Slideshow = function ($e, options) {

	window.slideshows.push(this);

	options = options || {};

 	typeof options == "string" && (options = $.parseJSON(options));

	this.settings = $.extend(
		{
			breakpoints : [
				950,
				800,
				550
			]
		},
		options
	);

	this.settings.breakpoints.sort(
		function (a, b) {
			return a - b;
		}
	);

	this.i = $(window.slideshows).index(this);

	this.e = $e;

	this.currentIndex = 0;

	this.visibleCount = 4;

	this.init();

}


Slideshow.prototype.init = function () {
	var root = this;
	
	
	// Next and previous buttons

	$(".next", this.e).click(
		function (e) {
			e.preventDefault();
			root.advance();
		}
	);

	$(".prev", this.e).click(
		function (e) {
			e.preventDefault();
			root.goback();
		}
	);


	$(window).on(
		"resize",
		function () {
			root.setVisibleCount();
			root.nudgePositionToFitEnd();
			root.manageControlsVisibility();
		}
	);
	
	this.setVisibleCount();
	this.nudgePositionToFitEnd();
	this.manageControlsVisibility();

}

Slideshow.prototype.advance = function () {

	if (this.currentIndex < $(".items > ul > li", this.e).length - this.visibleCount) {
		this.currentIndex++;
		this.goToSlideAtCurrentIndex();
		this.manageControlsVisibility()
	}

}

Slideshow.prototype.goback = function () {

	if (this.currentIndex > 0) {
		this.currentIndex--;
		this.goToSlideAtCurrentIndex();	
		this.manageControlsVisibility()
	}

}

Slideshow.prototype.goToSlideAtCurrentIndex = function () {
	var root = this;

	$(".items > ul > li", this.e).css(
		{
			transform : "translateX(-" + 100 * this.currentIndex + "%)"
		}
	)

}


Slideshow.prototype.nudgePositionToFitEnd = function () {

	if (this.visibleCount <= $(".items > ul > li", this.e).length && this.currentIndex > $(".items > ul > li", this.e).length - this.visibleCount) {
		
		this.currentIndex = $(".items > ul > li", this.e).length - this.visibleCount;

		this.goToSlideAtCurrentIndex();
		
		this.manageControlsVisibility()

	}

}


Slideshow.prototype.manageControlsVisibility = function () {

	// At beginning if currentIndex is 0.
	if (this.currentIndex == 0) {
		this.e.addClass("atBeg");
	} else {
		this.e.removeClass("atBeg");
	}
	
	if (this.currentIndex >= $(".items > ul > li", this.e).length - this.visibleCount || this.visibleCount >= $(".items > ul > li", this.e).length) {
		this.e.addClass("atEnd");
	} else {
		this.e.removeClass("atEnd");
	}

}


Slideshow.prototype.setVisibleCount = function () {
		
	if ($(window).width() <= this.settings.breakpoints[0]) this.visibleCount = 1;
	else if ($(window).width() <= this.settings.breakpoints[1]) this.visibleCount = 2;
	else if ($(window).width() <= this.settings.breakpoints[2]) this.visibleCount = 3;
	else this.visibleCount = 4;
}


$.fn.slideshow = function (options) {

    return this.each(
    	function() {

			new Slideshow(
				$(this),
				options || $(this).data("slideshow-options")
			);

		}
	);

};


$(
	function () {
		$("[data-slideshow]").each(
			function () {
				$(this).slideshow();
			}
		);		
	}
);


// enabling smooth scroll
$(document).ready(function(event) {
    $('.scroll-down').click(function() {
        var linkHref = $(this).attr('href');
        $('html, body').animate({
            scrollTop: $(linkHref).offset().top
        }, 1000);
        return false;
    });
});