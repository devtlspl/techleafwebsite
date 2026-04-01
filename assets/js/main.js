/* TechLeaf Systems — Main JS */

// Mobile Nav Toggle
document.addEventListener('DOMContentLoaded', function () {
  const hamburger = document.getElementById('hamburger');
  const mobileNav = document.getElementById('mobile-nav');
  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', () => {
      mobileNav.classList.toggle('open');
    });
  }

  // Multi-step Form
  initMultiStepForm();

  // Hide WhatsApp widget while hero slider is in view
  initHideWhatsAppOnSlider();

  // Auto-rotate hero slider every 7s
  initHeroSliderAutoplay();

  // Service option selector
  document.querySelectorAll('.service-option').forEach(opt => {
    opt.addEventListener('click', function () {
      this.closest('.service-selector').querySelectorAll('.service-option').forEach(o => o.classList.remove('selected'));
      this.classList.add('selected');
      this.querySelector('input[type="radio"]') && (this.querySelector('input[type="radio"]').checked = true);
    });
  });

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href === '#') return;
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        if (mobileNav) mobileNav.classList.remove('open');
      }
    });
  });

  // Active nav link highlight
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav a, .mobile-nav a').forEach(link => {
    const linkPath = link.getAttribute('href').split('/').pop();
    if (linkPath === currentPath) link.classList.add('active');
  });
});

function initMultiStepForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;

  const panels = form.querySelectorAll('.form-panel');
  const stepDots = form.querySelectorAll('.form-step-dot');
  const stepLines = form.querySelectorAll('.form-step-line');
  let currentStep = 0;

  function showStep(n) {
    panels.forEach((p, i) => p.classList.toggle('active', i === n));
    stepDots.forEach((d, i) => {
      d.classList.toggle('active', i === n);
      d.classList.toggle('done', i < n);
    });
    stepLines.forEach((l, i) => l.classList.toggle('done', i < n));
    currentStep = n;
  }

  showStep(0);

  form.querySelectorAll('[data-next]').forEach(btn => {
    btn.addEventListener('click', () => showStep(currentStep + 1));
  });
  form.querySelectorAll('[data-prev]').forEach(btn => {
    btn.addEventListener('click', () => showStep(currentStep - 1));
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    const submitBtn = form.querySelector('[type="submit"]');
    submitBtn.textContent = 'Sending…';
    submitBtn.disabled = true;

    setTimeout(() => {
      form.innerHTML = `
        <div style="text-align:center;padding:2.5rem 1rem;">
          <div style="width:64px;height:64px;background:rgba(26,122,74,.12);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 1.25rem;">
            <svg viewBox="0 0 24 24" fill="none" stroke="#1a7a4a" stroke-width="2.5" width="32" height="32"><polyline points="20 6 9 17 4 12"/></svg>
          </div>
          <h3 style="color:#1a202c;margin-bottom:.5rem;">Request Received!</h3>
          <p style="color:#718096;font-size:.95rem;">Our team will respond within <strong>2 business hours</strong>. For urgent matters, call us directly at <a href="tel:04431396714" style="color:#1a7a4a;font-weight:600;">044-3139 6714</a>.</p>
        </div>`;
    }, 1200);
  });
}

// Intersection Observer for simple fade-in animation
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.why-card, .service-card, .case-study-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(16px)';
    el.style.transition = 'opacity .4s ease, transform .4s ease';
    observer.observe(el);
  });
}

function initHideWhatsAppOnSlider() {
  const slider = document.querySelector('.video-strip');
  if (!slider || !('IntersectionObserver' in window)) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        document.body.classList.toggle('hide-whatsapp', entry.isIntersecting);
      });
    },
    { threshold: 0.2 }
  );

  observer.observe(slider);
}

function initHeroSliderAutoplay() {
  const slides = Array.from(document.querySelectorAll('input[name="slider"]'));
  if (!slides.length) return;

  let current = slides.findIndex(s => s.checked);
  if (current < 0) current = 0;
  slides[current].checked = true;

  const intervalMs = 7000;
  let timer = setInterval(nextSlide, intervalMs);

  function nextSlide() {
    current = (current + 1) % slides.length;
    slides[current].checked = true;
  }

  // Reset timer on manual dot click
  slides.forEach((slide, index) => {
    slide.addEventListener('change', () => {
      current = index;
      clearInterval(timer);
      timer = setInterval(nextSlide, intervalMs);
    });
  });
}
