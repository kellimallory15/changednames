document.addBookingListener('DOMContentLoaded', function() {
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    const monthYearSpan = document.querySelector('.month-year');
    const datesDiv = document.querySelector('.dates');

    const months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ];

    let currentDate = new Date();

    function updateCalendar() {
        const month = currentDate.getMonth();
        const year = currentDate.getFullYear();

        // Fetch bookings from Django backend using AJAX
        fetch('/calendar.html/?month=${month}&year=${year}')
            .then(response => response.json())
            .then(data => {
                // Clear previous dates
                datesDiv.innerHTML = '';

                // Get booked dates from response
                let bookedDates = data.booked_dates || []

                const lastDay =  new Date(year, month, 0).getDate();
                for (let i = 1; i <= lastDay; i++) {
                    const dateDiv = document.createElement('div');
                    dateDiv.classList.add('date');

                    // If date is booked, add a class to reflect this
                    if (bookedDates.includes(i)) {
                        dateDiv.classList.add('booked');
                    }

                    dateDiv.textContent = i;
                    datesDiv.appendChild(dateDiv);
                }
            })


        // Set month and year in the header
        monthYearSpan.textContent = `${months[month]} ${year}`;

        // Clear previous dates
        datesDiv.innerHTML = '';

        // Calculate the number of days in the current month
        const lastDay = new Date(year, month + 1, 0).getDate();

        // Populate dates
        for (let i = 1; i <= lastDay; i++) {
            const dateDiv = document.createElement('div');
            dateDiv.classList.add('date');
            dateDiv.textContent = i;
            datesDiv.appendChild(dateDiv);
        }
    }

    prevButton.addBookingListener('click', function() {
        // Decrement the month
        currentDate.setMonth(currentDate.getMonth() - 1);
        updateCalendar();
    });

    nextButton.addBookingListener('click', function() {
        // Increment the month
        currentDate.setMonth(currentDate.getMonth() + 1);
        updateCalendar();
    });

    // Initial render
    updateCalendar();
});
