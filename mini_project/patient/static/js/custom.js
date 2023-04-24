// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


// client section owl carousel
$(".client_owl-carousel").owlCarousel({
    loop: true,
    margin: 0,
    dots: false,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 2
        }
    }
});



/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}
/**booking **/
$(document).ready(function() {
	// Get the bookings data from the local storage
	var bookings = JSON.parse(localStorage.getItem('bookings'));
	if(bookings != null) {
		// Loop through each booking and add it to the table
		for(var i=0; i<bookings.length; i++) {
			var booking = bookings[i];
			var statusClass = booking.status == 'Confirmed' ? 'table-success' : 'table-warning';
			var token = booking.token == '' ? '-' : booking.token;
			var row = '<tr class="' + statusClass + '">';
			row += '<td>' + booking.id + '</td>';
			row += '<td>' + booking.doctor + '</td>';
			row += '<td>' + booking.date + '</td>';
			row += '<td>' + booking.time + '</td>';
			row += '<td>' + booking.status + '</td>';
			row += '<td>' + token + '</td>';
			row += '</tr>';
			$('#booking-list').append(row);
		}
	}
});

/*newexistingpopup*/ 
