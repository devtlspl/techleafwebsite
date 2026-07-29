# 🧪 LOCAL TESTING GUIDE

**Server Status:** ✅ RUNNING  
**Local URL:** `http://localhost:8000`  
**Server Port:** 8000  
**Testing Time:** 15-20 minutes

---

## ✅ SERVER IS RUNNING

Your local development server is now running on:

```
http://localhost:8000
```

Access your website:
- **Homepage:** http://localhost:8000/index.html
- **Contact Page:** http://localhost:8000/contact.html
- **About Page:** http://localhost:8000/about.html

---

## 🧪 WHAT TO TEST

### TEST 1: Homepage Loads (2 min)

1. Open browser: `http://localhost:8000`
2. Check:
   - [ ] Logo loads
   - [ ] Navigation menu works
   - [ ] Hero section displays
   - [ ] Page scrolls smoothly
   - [ ] WhatsApp button visible

**Expected:** Page loads without errors ✅

---

### TEST 2: Contact Form Works (3 min)

1. Go to: `http://localhost:8000/contact.html`
2. Fill form with:
   - **Name:** Test Lead
   - **Email:** your-email@gmail.com
3. Click: "✅ Get Free Assessment (2-Hour Response)"
4. Check browser console (F12) for response

**Expected:** Form submits, shows success/error message ✅

---

### TEST 3: Azure Mail Function Integration (3 min)

1. Open browser console: `F12`
2. Go to: `http://localhost:8000/contact.html`
3. Click console tab
4. Paste this test code:

```javascript
// TEST: Direct Azure Mail Function Call
fetch('https://mailsvx.azurewebsites.net/api/submit', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'x-functions-key': '7jQxXArv_ZXrVnH4ECxhqLS4Cme9pxtD9IuHOm6yv9gxAzFuL3y4RA=='
  },
  body: JSON.stringify({
    formType: 'sales',
    name: 'Local Test - ' + new Date().toLocaleString(),
    email: 'test@techleafsystems.com',
    phone: '+91-8838581550',
    company: 'TechLeaf Test',
    message: 'Testing from localhost:8000',
    botTrap: ''
  })
})
.then(response => {
  console.log('📨 Response Status:', response.status);
  return response.text();
})
.then(text => {
  console.log('✅ SUCCESS! Azure responded:');
  console.log(text);
})
.catch(error => {
  console.error('❌ ERROR occurred:');
  console.error(error.message);
});
```

5. Press Enter
6. Check console output

**Expected output:**
```
📨 Response Status: 200
✅ SUCCESS! Azure responded:
[success message from Azure]
```

---

### TEST 4: Check Email Received (5 min)

1. After running test code above
2. Open your email: `sales@techleafsystems.com`
3. Check for new email:
   - **From:** Azure Function (noreply@...)
   - **To:** sales@techleafsystems.com
   - **Subject:** Contains form data
   - **Body:** Should have: name, email, message

**Expected:** Email received within 30 seconds ✅

---

### TEST 5: Cookie Banner (2 min)

1. Go to: `http://localhost:8000/contact.html`
2. Scroll to bottom
3. Check:
   - [ ] Cookie banner appears at bottom
   - [ ] "Accept & Continue" button visible
   - [ ] "Decline Tracking" button visible
4. Click "Accept & Continue"
5. Check console (F12 → Storage → Cookies):
   - [ ] Cookie "techleaf_analytics_consent" set to "accepted"

**Expected:** Banner disappears, cookie set ✅

---

### TEST 6: Simplified Contact Form (3 min)

1. Go to: `http://localhost:8000/contact.html`
2. Check form fields:
   - [ ] "Your Full Name" field exists
   - [ ] "Your Business Email" field exists
   - [ ] No other fields visible
   - [ ] Submit button says "✅ Get Free Assessment"

**Expected:** Only 2 fields visible ✅

---

### TEST 7: Mobile Responsiveness (2 min)

1. Go to: `http://localhost:8000`
2. Open developer tools: `F12`
3. Click device toggle (phone icon)
4. Check:
   - [ ] Layout adapts to mobile width
   - [ ] Navigation hamburger appears
   - [ ] Form is readable on mobile
   - [ ] Buttons are clickable

**Expected:** Mobile layout works ✅

---

## 📊 TESTING CHECKLIST

### Core Functionality
- [ ] Homepage loads without errors
- [ ] Contact form is simplified (2 fields)
- [ ] Form submission works
- [ ] Mail function receives data
- [ ] Email is delivered

### User Experience
- [ ] Page loads in <3 seconds
- [ ] Form is easy to use
- [ ] Success message shows after submit
- [ ] Mobile view works
- [ ] Links all work

### Lead Capture
- [ ] Cookie banner works
- [ ] Analytics consent captured
- [ ] Form data structure correct
- [ ] Mail function authentication working
- [ ] Error handling working

---

## 🔍 TROUBLESHOOTING

### Problem: Form won't submit

**Solution:**
1. Check browser console (F12)
2. Look for error messages
3. Verify email format is correct
4. Try again

### Problem: Azure Mail Function returns error

**Check:**
```javascript
// Run this to test function key
console.log('Function Key: 7jQxXArv_ZXrVnH4ECxhqLS4Cme9pxtD9IuHOm6yv9gxAzFuL3y4RA==');
console.log('API Base: https://mailsvx.azurewebsites.net/api');
console.log('Endpoint: /submit');
```

If error, tell me the exact error message.

### Problem: CORS error

**This means:** Azure blocked the cross-origin request

**Solution:**
- CORS is configured in Azure
- Should work from production domain
- May fail from localhost (expected)
- Use Azure test endpoint instead

---

## ✅ EXPECTED TEST RESULTS

### If Everything Works ✅
```
✅ Form loads
✅ Form submits successfully  
✅ Azure function responds
✅ Email received
✅ Success message shows
✅ Cookie captured
→ READY FOR LEAD GENERATION
```

### If Something Breaks ❌
Tell me:
1. Which test failed
2. Exact error message
3. What you expected vs what happened

I'll fix it immediately.

---

## 🚀 AFTER TESTING

Once all tests pass (✅ ✅ ✅ ✅ ✅ ✅ ✅):

1. **Start lead generation immediately**
2. Follow: `IMMEDIATE_ACTIONS_NOW.md`
3. You'll get 3-8 leads by tomorrow

---

## 📝 TEST RESULTS TEMPLATE

Copy this and fill in your results:

```
LOCAL TESTING RESULTS
====================

TEST 1 (Homepage): ✅ / ❌ 
Notes: [what happened]

TEST 2 (Contact Form): ✅ / ❌
Notes: [what happened]

TEST 3 (Azure Mail Function): ✅ / ❌
Notes: [what happened]

TEST 4 (Email Received): ✅ / ❌
Notes: [what happened]

TEST 5 (Cookie Banner): ✅ / ❌
Notes: [what happened]

TEST 6 (Simplified Form): ✅ / ❌
Notes: [what happened]

TEST 7 (Mobile): ✅ / ❌
Notes: [what happened]

OVERALL: READY FOR PRODUCTION ✅ / NEEDS FIXES ❌

If not ready, what needs fixing?
[list any issues]
```

---

## 🎯 LOCAL SERVER COMMANDS

### Check if server is running
```powershell
# On Windows PowerShell
netstat -ano | findstr :8000
```

### Stop the server (when done testing)
```powershell
# Press Ctrl+C in the terminal running the server
# Or close the terminal window
```

### Restart the server
```powershell
# Stop it first (Ctrl+C)
# Then run again:
python -m http.server 8000
```

---

## 📂 LOCAL TEST URLS

Keep these handy for testing:

- **Homepage:** http://localhost:8000/
- **Contact:** http://localhost:8000/contact.html
- **About:** http://localhost:8000/about.html
- **Services:** http://localhost:8000/services.html
- **Careers:** http://localhost:8000/careers.html
- **Blog (when created):** http://localhost:8000/blog-dba-emergency.html

---

## ⚡ QUICK TEST (5 MIN)

If you just want to do a quick verification:

1. Open: `http://localhost:8000/contact.html`
2. Fill form with Name + Email
3. Submit
4. Check console (F12) for success message
5. Check Azure response

**Result:** ✅ Works or ❌ Error?

---

## 🎬 START TESTING NOW

1. **Open browser:**
   - http://localhost:8000

2. **Test form:**
   - Fill Name + Email
   - Submit
   - Check console

3. **Tell me result:**
   - What did you see?
   - Any errors?
   - Email received?

Then we can start the lead generation! 🚀

---

**Your local testing server is running.**

**Next:** Go to http://localhost:8000/contact.html and test the form.

**Tell me:** What happens when you submit?
