/**
 * Exit Intent Popup
 * Captures emails when users try to leave
 * Sends directly to Azure Mail Function
 */

(function() {
  let popupShown = false;
  const POPUP_COOKIE = 'techleaf_exit_popup_shown';
  
  // Check if popup was already shown this session
  function hasShownPopup() {
    const cookie = document.cookie.split(';').find(c => c.trim().startsWith(POPUP_COOKIE));
    return !!cookie;
  }
  
  // Set cookie to prevent spam
  function setPopupCookie() {
    const date = new Date();
    date.setTime(date.getTime() + (24 * 60 * 60 * 1000)); // 24 hours
    document.cookie = `${POPUP_COOKIE}=true; expires=${date.toUTCString()}; path=/`;
  }
  
  // Create and show popup
  function showExitPopup() {
    if (popupShown || hasShownPopup()) return;
    popupShown = true;
    setPopupCookie();
    
    // Backdrop
    const backdrop = document.createElement('div');
    backdrop.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.5);
      z-index: 9998;
    `;
    
    // Popup container
    const popup = document.createElement('div');
    popup.style.cssText = `
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background: white;
      padding: 40px;
      border-radius: 12px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.3);
      z-index: 9999;
      max-width: 500px;
      width: 90%;
      font-family: 'Inter', system-ui, sans-serif;
    `;
    
    popup.innerHTML = `
      <h2 style="margin: 0 0 15px 0; font-size: 1.5rem; color: #1b5a3f;">
        🚨 Before You Go...
      </h2>
      
      <p style="margin: 0 0 10px 0; color: #374151; font-size: 0.95rem;">
        Get a <strong>FREE IT Cost Audit</strong> (Worth ₹10,000)
      </p>
      
      <p style="margin: 0 0 20px 0; color: #6b7280; font-size: 0.9rem;">
        See how much you could save on hardware, AMC, and DBA support. No sales pitch.
      </p>
      
      <div style="margin-bottom: 15px;">
        <input 
          type="email" 
          id="exit-email" 
          placeholder="your@company.com" 
          style="
            width: 100%;
            padding: 12px;
            border: 1px solid #d1d5db;
            border-radius: 6px;
            font-size: 1rem;
            box-sizing: border-box;
          "
          required
        >
      </div>
      
      <button 
        id="exit-submit" 
        style="
          width: 100%;
          padding: 12px;
          background: #22a05e;
          color: white;
          border: none;
          border-radius: 6px;
          cursor: pointer;
          font-weight: 600;
          font-size: 1rem;
          margin-bottom: 10px;
          transition: background 0.3s;
        "
        onmouseover="this.style.background='#1a7a4a'"
        onmouseout="this.style.background='#22a05e'"
      >
        ✓ Get Free Audit
      </button>
      
      <button 
        id="exit-close" 
        style="
          width: 100%;
          padding: 10px;
          background: transparent;
          color: #6b7280;
          border: 1px solid #d1d5db;
          border-radius: 6px;
          cursor: pointer;
          font-weight: 500;
          font-size: 0.95rem;
          transition: all 0.3s;
        "
        onmouseover="this.style.borderColor='#9ca3af'; this.style.color='#374151'"
        onmouseout="this.style.borderColor='#d1d5db'; this.style.color='#6b7280'"
      >
        Not interested
      </button>
    `;
    
    // Add to page
    document.body.appendChild(backdrop);
    document.body.appendChild(popup);
    
    // Button handlers
    document.getElementById('exit-submit').addEventListener('click', submitEmail);
    document.getElementById('exit-close').addEventListener('click', closePopup);
    
    // Close on backdrop click
    backdrop.addEventListener('click', closePopup);
  }
  
  function closePopup() {
    const popup = document.querySelector('[style*="position: fixed"][style*="top: 50%"]');
    const backdrop = document.querySelector('[style*="position: fixed"][style*="background: rgba(0, 0, 0, 0.5)"]');
    if (popup) popup.remove();
    if (backdrop) backdrop.remove();
  }
  
  function submitEmail() {
    const email = document.getElementById('exit-email').value;
    
    if (!email || !email.includes('@')) {
      alert('Please enter a valid email address.');
      return;
    }
    
    const submitBtn = document.getElementById('exit-submit');
    submitBtn.textContent = 'Sending...';
    submitBtn.disabled = true;
    
    // Send to Azure Function
    const data = {
      formType: 'exit_popup',
      name: 'Exit Intent Lead',
      email: email,
      phone: '',
      company: '',
      message: 'Lead from exit-intent popup - interested in FREE IT Cost Audit',
      botTrap: ''
    };
    
    // Use the mail API if available
    if (window.sendSubmitForm) {
      window.sendSubmitForm(data)
        .then(() => {
          alert('✅ Check your email! We\'ll send your free audit within 2 hours.');
          closePopup();
        })
        .catch(err => {
          console.error('Error:', err);
          alert('There was an issue. Please try the contact form instead.');
          submitBtn.textContent = '✓ Get Free Audit';
          submitBtn.disabled = false;
        });
    } else {
      // Fallback: direct fetch to Azure
      fetch('https://mailsvx.azurewebsites.net/api/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-functions-key': '7jQxXArv_ZXrVnH4ECxhqLS4Cme9pxtD9IuHOm6yv9gxAzFuL3y4RA=='
        },
        body: JSON.stringify(data)
      })
      .then(r => r.text())
      .then(() => {
        alert('✅ Check your email! We\'ll send your free audit within 2 hours.');
        closePopup();
      })
      .catch(err => {
        console.error('Error:', err);
        alert('There was an issue. Please try the contact form instead.');
        submitBtn.textContent = '✓ Get Free Audit';
        submitBtn.disabled = false;
      });
    }
  }
  
  // Detect when user tries to leave
  document.addEventListener('mouseleave', function(e) {
    // Only show when mouse moves to top of page (leaving via top)
    if (e.clientY <= 0) {
      showExitPopup();
    }
  });
  
  // Also detect keyboard (ESC key)
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      closePopup();
    }
  });
})();
