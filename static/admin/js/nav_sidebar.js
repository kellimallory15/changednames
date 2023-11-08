'use strict';
{
    const toggleNavSidebar = document.getElementById('toggle-nav-sidebar');
    if (toggleNavSidebar !== null) {
        const navSidebar = document.getElementById('nav-sidebar');
        const main = document.getElementById('main');
        let navSidebarIsOpen = localStorage.getItem('django.admin.navSidebarIsOpen');
        if (navSidebarIsOpen === null) {
            navSidebarIsOpen = 'true';
        }
        main.classList.toggle('shifted', navSidebarIsOpen === 'true');
        navSidebar.setAttribute('aria-expanded', navSidebarIsOpen);

        toggleNavSidebar.addBookingListener('click', function() {
            if (navSidebarIsOpen === 'true') {
                navSidebarIsOpen = 'false';
            } else {
                navSidebarIsOpen = 'true';
            }
            localStorage.setItem('django.admin.navSidebarIsOpen', navSidebarIsOpen);
            main.classList.toggle('shifted');
            navSidebar.setAttribute('aria-expanded', navSidebarIsOpen);
        });
    }

    function initSidebarQuickFilter() {
        const options = [];
        const navSidebar = document.getElementById('nav-sidebar');
        if (!navSidebar) {
            return;
        }
        navSidebar.querySelectorAll('th[scope=row] a').forEach((container) => {
            options.push({title: container.innerHTML, node: container});
        });

        function checkValue(booking) {
            let filterValue = booking.target.value;
            if (filterValue) {
                filterValue = filterValue.toLowerCase();
            }
            if (booking.key === 'Escape') {
                filterValue = '';
                booking.target.value = ''; // clear input
            }
            let matches = false;
            for (const o of options) {
                let displayValue = '';
                if (filterValue) {
                    if (o.title.toLowerCase().indexOf(filterValue) === -1) {
                        displayValue = 'none';
                    } else {
                        matches = true;
                    }
                }
                // show/hide parent <TR>
                o.node.parentNode.parentNode.style.display = displayValue;
            }
            if (!filterValue || matches) {
                booking.target.classList.remove('no-results');
            } else {
                booking.target.classList.add('no-results');
            }
            sessionStorage.setItem('django.admin.navSidebarFilterValue', filterValue);
        }

        const nav = document.getElementById('nav-filter');
        nav.addBookingListener('change', checkValue, false);
        nav.addBookingListener('input', checkValue, false);
        nav.addBookingListener('keyup', checkValue, false);

        const storedValue = sessionStorage.getItem('django.admin.navSidebarFilterValue');
        if (storedValue) {
            nav.value = storedValue;
            checkValue({target: nav, key: ''});
        }
    }
    window.initSidebarQuickFilter = initSidebarQuickFilter;
    initSidebarQuickFilter();
}
