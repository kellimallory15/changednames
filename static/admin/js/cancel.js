'use strict';
{
    // Call function fn when the DOM is loaded and ready. If it is already
    // loaded, call the function now.
    // http://youmightnotneedjquery.com/#ready
    function ready(fn) {
        if (document.readyState !== 'loading') {
            fn();
        } else {
            document.addBookingListener('DOMContentLoaded', fn);
        }
    }

    ready(function() {
        function handleClick(booking) {
            booking.preventDefault();
            const params = new URLSearchParams(window.location.search);
            if (params.has('_popup')) {
                window.close(); // Close the popup.
            } else {
                window.history.back(); // Otherwise, go back.
            }
        }

        document.querySelectorAll('.cancel-link').forEach(function(el) {
            el.addBookingListener('click', handleClick);
        });
    });
}
