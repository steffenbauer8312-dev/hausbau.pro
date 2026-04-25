/* hausbau.pro — main.js */

(function () {
  // Mobile nav toggle
  var navToggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');

  if (navToggle && nav) {
    navToggle.addEventListener('click', function () {
      nav.classList.toggle('open');
      var isOpen = nav.classList.contains('open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // Close nav when clicking a link
    nav.querySelectorAll('.nav__link, .btn--header').forEach(function (link) {
      link.addEventListener('click', function () {
        nav.classList.remove('open');
      });
    });
  }

  // Lead form — Formspree submission + success display
  var leadForm = document.getElementById('leadForm');
  var formSuccess = document.getElementById('formSuccess');

  if (leadForm && formSuccess) {
    leadForm.addEventListener('submit', function (e) {
      // Let Formspree handle the actual submission
      // The success message will be shown by Formspree's redirect or we show it manually
      var submitBtn = leadForm.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Wird gesendet…';
      }

      // For Formspree, we don't preventDefault — let it submit normally.
      // For demo/testing without Formspree, handle it here:
      var action = leadForm.getAttribute('action');
      if (action && action.includes('formspree.io') && !action.includes('YOUR_FORM_ID')) {
        // Formspree is configured — let native submission through
        return;
      }

      // Demo fallback: prevent and show success
      e.preventDefault();
      leadForm.style.display = 'none';
      formSuccess.classList.add('visible');

      // In production with a real backend, you'd POST via fetch() here
      console.log('Lead captured:', {
        name: document.getElementById('name').value,
        phone: document.getElementById('phone').value,
        plz: document.getElementById('plz').value,
        service: document.getElementById('service').value,
        message: document.getElementById('message').value,
        timeline: document.getElementById('timeline').value,
      });
    });
  }

  // Smooth scroll for anchor links (fallback for browsers without CSS smooth scroll)
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var targetId = this.getAttribute('href').slice(1);
      if (!targetId) return;
      var target = document.getElementById(targetId);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // Header shadow on scroll
  var header = document.querySelector('.header');
  if (header) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 10) {
        header.style.boxShadow = '0 2px 12px rgba(0,0,0,0.10)';
      } else {
        header.style.boxShadow = '0 1px 3px rgba(0,0,0,0.08)';
      }
    });
  }
})();
