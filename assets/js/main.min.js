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

  initAppleWatchHeroMosaic();
    // Hide WhatsApp widget while hero slider is in view
  initHideWhatsAppOnSlider();

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
    btn.addEventListener('click', () => {
      const currentPanel = panels[currentStep];
      const inputs = currentPanel.querySelectorAll('input, select, textarea');
      let isValid = true;
      for (const input of inputs) {
        if (!input.checkValidity()) {
          input.reportValidity();
          isValid = false;
          break;
        }
      }
      if (isValid) {
        showStep(currentStep + 1);
      }
    });
  });
  form.querySelectorAll('[data-prev]').forEach(btn => {
    btn.addEventListener('click', () => showStep(currentStep - 1));
  });

  form.addEventListener('submit', async function (e) {
    e.preventDefault();
    
    const submitBtn = form.querySelector('[type="submit"]');
    
    // Create or get error message element
    let errorEl = form.querySelector('.form-error-msg');
    if (!errorEl) {
      errorEl = document.createElement('div');
      errorEl.className = 'form-error-msg';
      errorEl.style.color = '#ef4444';
      errorEl.style.padding = '12px 16px';
      errorEl.style.marginBottom = '16px';
      errorEl.style.borderRadius = '8px';
      errorEl.style.backgroundColor = '#fee2e2';
      errorEl.style.border = '1px solid #f87171';
      errorEl.style.display = 'none';
      errorEl.style.fontSize = '0.9rem';
      errorEl.style.fontWeight = '500';
      errorEl.style.width = '100%';
      submitBtn.parentNode.insertBefore(errorEl, submitBtn);
    }
    
    errorEl.style.display = 'none';

    const formData = new FormData(form);
    const name = formData.get('name') ? formData.get('name').trim() : '';
    const email = formData.get('email') ? formData.get('email').trim() : '';
    const phone = formData.get('phone') ? formData.get('phone').trim() : '';
    
    if (!name || (!email && !phone)) {
      errorEl.textContent = 'Please provide your name and either an email or phone number so we can reach you.';
      errorEl.style.display = 'block';
      return;
    }

    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Sending…';
    submitBtn.disabled = true;

    try {
      const data = {
        formType: 'sales',
        botTrap: formData.get('_bot_trap') || '',
        name: name,
        email: email,
        phone: phone,
        company: formData.get('company') || '',
        budget: '', // or extract if added later
        message: `[Interest: ${formData.get('service') || 'None'}] [Timeline: ${formData.get('timeline') || 'None'}]\n${formData.get('message') || ''}`
      };

      const city = formData.get('city');
      if (city) {
        data.message = `[City: ${city}]\n${data.message}`;
      }

      await window.sendSubmitForm(data);

      window.location.href = "thank-you.html";
    } catch (err) {
      console.error(err);
      errorEl.textContent = 'There was a problem sending your request. Please check your connection and try again, or call us directly.';
      errorEl.style.display = 'block';
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
      
      // Track form failures in Google Analytics
      if (typeof gtag === 'function') {
        gtag('event', 'form_error', {
          'event_category': 'form_submission',
          'event_label': err.message || 'unknown_error',
          'value': 1
        });
      }
    }
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

  // GA4 Event Tracking wrapped in DOMContentLoaded
  document.addEventListener('DOMContentLoaded', function() {
    // Generic button click tracking has been removed.
    // We only track actual form submissions and direct contact links (WhatsApp/Phone/Email) as leads.

    // Track contact links (tel:, mailto:, wa.me)
    document.querySelectorAll('a[href^="tel:"], a[href^="mailto:"], a[href*="wa.me"]').forEach(link => {
      link.addEventListener('click', function(e) {
        if (typeof gtag === 'function') {
          let type = 'Contact Link';
          if (this.href.startsWith('tel:')) type = 'Phone Call';
          else if (this.href.startsWith('mailto:')) type = 'Email Click';
          else if (this.href.includes('wa.me')) type = 'WhatsApp Chat';
          gtag('event', 'generate_lead', {
            'event_category': 'contact_link',
            'event_label': type,
            'value': 1
          });
        }
      });
    });

    // Track form submissions globally
    document.addEventListener('submit', function(e) {
      if (typeof gtag === 'function') {
        gtag('event', 'generate_lead', {
          'event_category': 'form_submission',
          'event_label': e.target.id || 'contact_form',
          'value': 50
        });
      }
    });
  });

// Form Step 1 Validation
document.addEventListener('click', function(e) {
  if (e.target.matches('[data-next]')) {
    const currentPanel = e.target.closest('.form-panel');
    if (currentPanel && currentPanel.id === 'step1') {
      const selectedService = currentPanel.querySelector('input[type="radio"]:checked');
      if (!selectedService) {
        alert('Please select a service before proceeding.');
        e.stopImmediatePropagation();
        e.preventDefault();
      }
    }
  }
}, true); // use capture phase to intercept before other listeners


function initAppleWatchHeroMosaic() {
    const grid = document.getElementById('heroMosaicGrid') || document.querySelector('.hero-mosaic-grid');
    if (!grid) return;
  
    const items = Array.from(grid.querySelectorAll('.hero-mosaic-item'));
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  
    const tileData = items.map(item => {
      const styleStr = item.getAttribute('style') || '';
      const matchX = styleStr.match(/--tile-x:\s*([^;]+)/);
      const matchY = styleStr.match(/--tile-y:\s*([^;]+)/);
      const tileX = matchX ? parseFloat(matchX[1]) : 0;
      const tileY = matchY ? parseFloat(matchY[1]) : 0;
      
      // Create random idle offset timing
      const floatDelay = Math.random() * -5;
      const floatDur = 4 + Math.random() * 2;
      if (!reducedMotion) {
        item.style.animation = `idleFloat ${floatDur}s ease-in-out ${floatDelay}s infinite alternate`;
      }
      
      return { item, tileX, tileY };
    });
  
    // Inject idle animation keyframes
    if (!document.getElementById('mosaic-idle-keyframes')) {
      const style = document.createElement('style');
      style.id = 'mosaic-idle-keyframes';
      style.innerHTML = `@keyframes idleFloat { 0% { transform: translate(calc(var(--tile-x) + var(--hover-x)), 
calc(var(--tile-y) + var(--hover-y) - 3px)); } 100% { transform: translate(calc(var(--tile-x) + var(--hover-x)), 
calc(var(--tile-y) + var(--hover-y) + 3px)); } }`;
      document.head.appendChild(style);
    }
  
    let pointerX = 0;
    let pointerY = 0;
    let frameId = null;
  
    function updateTiles() {
      frameId = null;
  
      if (reducedMotion) return;
  
      const gridRect = grid.getBoundingClientRect();
      if (gridRect.width === 0) return;
  
      const gridCenterX = gridRect.left + gridRect.width / 2;
      const gridCenterY = gridRect.top + gridRect.height / 2;
  
      let nearestIndex = -1;
      let nearestDistance = Infinity;
  
      const measuredTiles = tileData.map((data, index) => {
        const tileCenterX = gridCenterX + data.tileX;
        const tileCenterY = gridCenterY + data.tileY;
        const dx = pointerX - tileCenterX;
        const dy = pointerY - tileCenterY;
        const distance = Math.hypot(dx, dy);
  
        if (distance < nearestDistance) {
          nearestDistance = distance;
          nearestIndex = index;
        }
        return { data, dx, dy, distance };
      });
  
      const activationRadius = 190;
      const influenceRadius = 260;
      const maximumRepulsion = 16;
      const maximumScale = 1.25;
      const hasActive = nearestIndex >= 0 && nearestDistance <= activationRadius;
  
      grid.classList.toggle('has-active', hasActive);
  
      // Subtle Grid Parallax
      const parallaxX = ((pointerX / window.innerWidth) - 0.5) * -16;
      const parallaxY = ((pointerY / window.innerHeight) - 0.5) * -16;
      // Don't override scale from CSS, use CSS variable for parallax offset
      grid.style.transform = `translateY(-50%) translate(${parallaxX}px, ${parallaxY}px)`;
  
      measuredTiles.forEach((measured, index) => {
        const { data, dx, dy, distance } = measured;
        const safeDistance = Math.max(distance, 1);
        const influence = Math.max(0, 1 - safeDistance / influenceRadius);
  
        let offsetX = 0;
        let offsetY = 0;
        let scale = 1;
        let isActive = false;
  
        if (hasActive && index === nearestIndex) {
          isActive = true;
          scale = maximumScale;
          const push = (safeDistance / activationRadius) * 4;
          offsetX = -(dx / safeDistance) * push;
          offsetY = -(dy / safeDistance) * push;
        } else if (influence > 0) {
          const repulsion = maximumRepulsion * influence;
          offsetX = -(dx / safeDistance) * repulsion;
          offsetY = -(dy / safeDistance) * repulsion;
          scale = 1 + (0.02 * influence);
        }
  
        offsetX = Math.round(offsetX * 10) / 10;
        offsetY = Math.round(offsetY * 10) / 10;
        scale = Math.round(scale * 1000) / 1000;
  
        data.item.classList.toggle('is-active', isActive);
        
        // Update variables instead of direct transform string
        data.item.style.setProperty('--hover-x', `${offsetX}px`);
        data.item.style.setProperty('--hover-y', `${offsetY}px`);
        
        const card = data.item.querySelector('.hero-mosaic-card');
        if (card) card.style.setProperty('--hover-scale', scale);
        
        // Pause idle float slightly if active to avoid jitter
        if (isActive) {
          data.item.style.animationPlayState = 'paused';
        } else {
          data.item.style.animationPlayState = 'running';
        }
      });
    }
  
    const handlePointer = (e) => {
      pointerX = e.touches ? e.touches[0].clientX : e.clientX;
      pointerY = e.touches ? e.touches[0].clientY : e.clientY;
      
      // Check if pointer is inside mosaic area roughly to optimize
      if (!frameId) {
        frameId = requestAnimationFrame(updateTiles);
      }
    };
  
    document.addEventListener('pointermove', handlePointer);
    document.addEventListener('mousemove', handlePointer);
    document.addEventListener('touchmove', handlePointer, { passive: true });
  
    const resetHover = () => {
      grid.classList.remove('has-active');
      grid.style.transform = `translateY(-50%)`;
      tileData.forEach((data) => {
        data.item.classList.remove('is-active');
        data.item.style.setProperty('--hover-x', '0px');
        data.item.style.setProperty('--hover-y', '0px');
        data.item.style.animationPlayState = 'running';
        const card = data.item.querySelector('.hero-mosaic-card');
        if (card) card.style.setProperty('--hover-scale', 1);
      });
    };
  
    document.addEventListener('pointerleave', resetHover);
    document.addEventListener('mouseleave', resetHover);
  }



