// ═══════════════════════════════════════════════════════════════════
//   MONA LISA OVERDRIVE - Visitor Counter (Firebase Realtime DB)
//   Replace the firebaseConfig below with your own from the console.
// ═══════════════════════════════════════════════════════════════════

const firebaseConfig = {
  apiKey: "AIzaSyA7QY02cZy-QtEefGsSc1x_uEHo4lhcvlw",
  authDomain: "monalisaoverdrivesite.firebaseapp.com",
  databaseURL: "https://monalisaoverdrivesite-default-rtdb.firebaseio.com",
  projectId: "monalisaoverdrivesite",
  storageBucket: "monalisaoverdrivesite.firebasestorage.app",
  messagingSenderId: "249552515724",
  appId: "1:249552515724:web:6811b80e48844aa82101a9"
};

// ─── Firebase SDK (loaded via CDN in overrides/main.html) ───────────

function initVisitorCounter() {
  const countEl = document.getElementById('visit-count');
  if (!countEl) return;

  // Import Firebase modules
  Promise.all([
    import('https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js'),
    import('https://www.gstatic.com/firebasejs/10.12.0/firebase-database.js')
  ]).then(([{ initializeApp }, { getDatabase, ref, runTransaction, onValue }]) => {

    const app = initializeApp(firebaseConfig);
    const db = getDatabase(app);
    const counterRef = ref(db, 'visitorCount');

    // Increment counter once per session
    if (!sessionStorage.getItem('mlo_visited')) {
      sessionStorage.setItem('mlo_visited', '1');
      runTransaction(counterRef, (current) => (current || 0) + 1);
    }

    // Display the count with animated digits
    onValue(counterRef, (snapshot) => {
      const count = snapshot.val() || 0;
      animateCounter(countEl, count);
    });

  }).catch(err => {
    console.warn('Visitor counter unavailable:', err);
    countEl.textContent = '??????';
  });
}

function animateCounter(el, count) {
  const str = String(count).padStart(6, '0');
  el.innerHTML = str.split('').map(d => `<span class="digit">${d}</span>`).join('');

  // Flicker each digit in with a slight delay
  const digits = el.querySelectorAll('.digit');
  digits.forEach((d, i) => {
    d.style.opacity = '0';
    setTimeout(() => {
      d.style.transition = 'opacity 0.1s';
      d.style.opacity = '1';
    }, i * 80);
  });
}

// Run after page load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initVisitorCounter);
} else {
  initVisitorCounter();
}
