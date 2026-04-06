// Auto-move shows from Upcoming to Past when date passes
document.addEventListener('DOMContentLoaded', function() {
    function checkAndMoveShows() {
        const today = new Date();
        today.setHours(0, 0, 0, 0); // Start of today

        const upcomingContainer = document.getElementById('upcoming-shows');
        const pastContainer = document.getElementById('past-shows');

        if (!upcomingContainer || !pastContainer) {
            return;
        }

        const upcomingShows = upcomingContainer.querySelectorAll('.event-card[data-date]');

        upcomingShows.forEach(show => {
            const showDate = new Date(show.getAttribute('data-date'));
            showDate.setHours(23, 59, 59, 999); // End of show day

            if (showDate < today) {
                // Move to past shows (insert at top)
                pastContainer.insertBefore(show, pastContainer.firstChild);
            }
        });
    }

    // Run on page load
    checkAndMoveShows();

    // Check once per day at midnight
    const now = new Date();
    const tomorrow = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1);
    const timeUntilMidnight = tomorrow - now;

    setTimeout(function() {
        checkAndMoveShows();
        // Then check every 24 hours
        setInterval(checkAndMoveShows, 24 * 60 * 60 * 1000);
    }, timeUntilMidnight);
});
