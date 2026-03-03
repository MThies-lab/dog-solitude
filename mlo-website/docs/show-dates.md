# Show Dates

---

## Upcoming Shows

<div id="upcoming-shows">

<div class="event-card" data-date="2026-04-18" data-show-id="show-1">
<div class="event-date">April 18th, 2026</div>
<div class="event-venue">Eagles Dare w/ Bridge to Breakdown</div>
<div class="event-details">

**DEBUT PERFORMANCE**

Experience Mona Lisa Overdrive as no one ever has! This is where the journey begins.

**Click for full details**

</div>

<div class="event-card-expanded" id="show-1-expanded">
<div class="show-details-content">

<h3>DEBUT PERFORMANCE</h3>
<p>Experience Mona Lisa Overdrive as no one ever has! This is where the journey begins.</p>

<p>Come open your eyes in the overdrive with our very own band-branded beer brewed right here in Wilmington, NC at Front St Brewery.</p>

<div class="show-details-box">
<p><strong>Venue:</strong> Eagles Dare<br>
<strong>Location:</strong> Wilmington, NC<br>
<strong>Doors:</strong> 8:00 PM<br>
<strong>Show:</strong> 9:00 PM<br>
<strong>Support:</strong> Bridge to Breakdown</p>

<p><strong>Special:</strong> MLO-branded beer available exclusively at this show, brewed by Front St Brewery</p>
</div>

<!--
HOW TO ADD GOOGLE MAPS:
1. Go to Google Maps (https://maps.google.com)
2. Search for the venue (e.g., "Eagles Dare Wilmington NC")
3. Click "Share" button
4. Click "Embed a map" tab
5. Copy the iframe code
6. Replace the src URL in the iframe below with your copied URL
7. Keep the styling attributes (border-radius, margin, etc.)
-->

<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3281.234567890123!2d-77.94567890000001!3d34.235678900000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMzTCsDE0JzA4LjQiTiA3N8KwNTYnNDQuNCJX!5e0!3m2!1sen!2sus!4v1234567890123!5m2!1sen!2sus" width="100%" height="300" style="border:0; border-radius: 8px; margin: 20px 0; box-shadow: 0 0 15px var(--glow-purple);" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>

<h3>What to Expect</h3>
<p>This is not just our first show—it's the beginning of something bigger. An immersive audiovisual experience that blends synthwave, vaporwave, and electronic elements into a neon-soaked journey through sound and light.</p>

<p>Join us as we open our eyes in the overdrive for the first time together.</p>

<div class="show-details-cta">
<a href="#" class="cta-button">Get Tickets</a>
<a href="https://facebook.com" class="cta-button" target="_blank">Facebook Event</a>
<a href="https://maps.google.com/?q=Eagles+Dare+Wilmington+NC" class="cta-button" target="_blank">Get Directions</a>
</div>

</div>
</div>

</div>

<p id="no-upcoming" style="display: none;" class="no-shows-message">No upcoming shows at the moment. Check back soon for new dates!</p>

</div>

---

## Past Shows

<div id="past-shows">

<p id="no-past" class="no-shows-message">Past performances will appear here after they've happened.</p>

</div>

---

## Stay Updated

More dates coming soon. The overdrive is just getting started.

Follow us on social media to stay in the loop about upcoming performances and new releases.

<script>
// Accordion/Expand functionality for show cards
document.addEventListener('click', function(e) {
    const card = e.target.closest('.event-card[data-show-id]');
    if (card) {
        const showId = card.getAttribute('data-show-id');
        const expanded = document.getElementById(showId + '-expanded');

        if (expanded) {
            // Toggle the expanded state
            const isActive = expanded.classList.contains('active');

            // Close all other expanded cards
            document.querySelectorAll('.event-card-expanded.active').forEach(el => {
                if (el !== expanded) {
                    el.classList.remove('active');
                }
            });

            // Toggle this card
            if (isActive) {
                expanded.classList.remove('active');
            } else {
                expanded.classList.add('active');
                // Smooth scroll to show the expanded content
                setTimeout(() => {
                    expanded.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }, 100);
            }
        }
    }
});

// Auto-move shows from Upcoming to Past when date passes
(function() {
    function checkAndMoveShows() {
        const today = new Date();
        today.setHours(0, 0, 0, 0); // Start of today

        const upcomingContainer = document.getElementById('upcoming-shows');
        const pastContainer = document.getElementById('past-shows');
        const upcomingShows = upcomingContainer.querySelectorAll('.event-card[data-date]');
        const noUpcoming = document.getElementById('no-upcoming');
        const noPast = document.getElementById('no-past');

        let hasUpcoming = false;
        let hasPast = false;

        upcomingShows.forEach(show => {
            const showDate = new Date(show.getAttribute('data-date'));
            showDate.setHours(23, 59, 59, 999); // End of show day

            if (showDate < today) {
                // Move to past shows (insert at top)
                if (pastContainer.firstChild && pastContainer.firstChild.classList && pastContainer.firstChild.classList.contains('event-card')) {
                    pastContainer.insertBefore(show, pastContainer.firstChild);
                } else {
                    pastContainer.insertBefore(show, noPast);
                }
                hasPast = true;
            } else {
                hasUpcoming = true;
            }
        });

        // Show/hide "no shows" messages
        noUpcoming.style.display = hasUpcoming ? 'none' : 'block';
        noPast.style.display = hasPast ? 'none' : 'block';
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
})();
</script>