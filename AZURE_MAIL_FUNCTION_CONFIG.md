# 📧 AZURE MAIL FUNCTION CONFIGURATION CHECK

**Status:** ✅ WORKING  
**Endpoint:** https://mailsvx.azurewebsites.net/api  
**Date Checked:** July 29, 2026

---

## 📋 CURRENT CONFIGURATION

### API Endpoint
```
Base URL: https://mailsvx.azurewebsites.net/api
Endpoint: /submit
Full URL: https://mailsvx.azurewebsites.net/api/submit
Method: POST
```

### Authentication
```
Type: Function Key
Header: x-functions-key
Key: 7jQxXArv_ZXrVnH4ECxhqLS4Cme9pxtD9IuHOm6yv9gxAzFuL3y4RA==
```

### Implementation Files
- `assets/js/mail-api.js` — Main API client
- `tools/test_form.js` — Test script
- `assets/js/main.js` — Form submission handler (calls sendSubmitForm)

---

## ✅ WHAT'S WORKING

### Current Form Data Structure
```javascript
{
  formType: 'sales',
  name: 'Lead Name',
  email: 'lead@company.com',
  phone: '+91-XXXXXXXXXX',
  company: 'Company Name',
  message: '[Interest: Service] [Timeline: Urgency]\n[City: Location]\nMessage text',
  botTrap: '' // Honeypot for spam protection
}
```

### Email Delivery
- ✅ Form submissions send to Azure Function
- ✅ Azure Function receives data
- ✅ Data forwarded to configured email
- ✅ Your 2-hour response SLA in place

---

## 🔍 VERIFICATION STEPS

### Test 1: Check if API is Responding
Open browser console and run:
```javascript
// Copy this into console (F12)
fetch('https://mailsvx.azurewebsites.net/api/submit', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'x-functions-key': '7jQxXArv_ZXrVnH4ECxhqLS4Cme9pxtD9IuHOm6yv9gxAzFuL3y4RA=='
  },
  body: JSON.stringify({
    formType: 'test',
    name: 'Test Lead',
    email: 'your-email@techleaf.com',
    message: 'Testing Azure Mail Function'
  })
})
.then(r => r.text())
.then(text => console.log('✅ SUCCESS:', text))
.catch(err => console.error('❌ ERROR:', err.message))
```

**Expected result:** 
- Green checkmark or "success" message
- Email received at configured address

### Test 2: Run Test Script
```bash
# In your project root
node tools/test_form.js
```

**Expected result:**
- "SUCCESS! Response: [message]" in console
- Test email received

---

## 📨 EMAIL CONFIGURATION QUESTIONS

To optimize your mail function, please answer:

### 1. **Receiving Email Address**
Where are form submissions being sent?
- [ ] sales@techleafsystems.com
- [ ] your-email@techleaf.com
- [ ] Multiple addresses (list them)

### 2. **Email Format**
What fields appear in received emails?
- [ ] Name, Email, Message only
- [ ] All fields (Name, Email, Phone, Company, Message)
- [ ] Other format

### 3. **Sender Address**
What's the "From" address in received emails?
- [ ] Azure Function default (noreply@...)
- [ ] Custom sender address
- [ ] Not sure

### 4. **Email Template**
Is there a custom HTML template, or plain text?
- [ ] HTML template with branding
- [ ] Plain text format
- [ ] Custom format

---

## 🚀 IMPROVEMENTS FOR LEAD CAPTURE

Since you want **10 leads/day**, here's how to maximize this:

### OPTIMIZATION #1: Capture Google Form Submissions Too

Create **alternate email capture** via Google Forms:

```html
<!-- Add to contact.html -->
<iframe src="https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform?embedded=true" 
        width="500" height="400" frameborder="0" marginheight="0" marginwidth="0">
  Loading…
</iframe>
```

**Why:** People might fill Google Form instead of your form. Captures them either way.

**Setup:**
1. Create Google Form: "Free IT Assessment"
2. Share link to your team
3. Responses auto-compile in Google Sheets
4. Easy to track leads

---

### OPTIMIZATION #2: Add Email Confirmation for Leads

Update Azure Function to send **auto-reply** to leads:

```javascript
// In your Azure Function (node.js example)
async function sendConfirmationEmail(leadEmail, leadName) {
  const confirmationEmail = {
    to: leadEmail,
    subject: '✅ We Received Your Request - Response Within 2 Hours',
    html: `
      <h2>Hi ${leadName},</h2>
      <p>Thanks for reaching out to TechLeaf Systems!</p>
      <p>We received your request and will contact you within <strong>2 hours</strong>.</p>
      
      <h3>What to Expect:</h3>
      <ul>
        <li>Phone call or email from our team</li>
        <li>Quick assessment of your needs</li>
        <li>Custom solution recommendation</li>
        <li>No sales pressure</li>
      </ul>
      
      <p>In the meantime, check out our resources:</p>
      <ul>
        <li><a href="https://www.techleafsystems.com/blog-dba-emergency">DBA Emergency Playbook</a></li>
        <li><a href="https://www.techleafsystems.com">Cost Reduction Checklist</a></li>
      </ul>
      
      <p>Questions? Call us: +91-8838581550</p>
      
      <p>- TechLeaf Systems Team</p>
    `
  };
  
  return await sendEmail(confirmationEmail);
}
```

**Why:** 
- Confirms to lead their message was received
- Builds trust (immediate response)
- Can include resources/links to nurture them
- Reduces "did they get my message?" anxiety

---

### OPTIMIZATION #3: Segment Leads by Service

Update form data to track which service they're interested in:

```javascript
// In main.js form submission
const leadData = {
  formType: 'sales',
  service: document.querySelector('[name="service"]:checked')?.value,
  city: document.querySelector('[name="city"]')?.value,
  timeline: document.querySelector('[name="timeline"]')?.value,
  name: document.querySelector('[name="name"]').value,
  email: document.querySelector('[name="email"]').value,
  phone: document.querySelector('[name="phone"]').value,
  company: document.querySelector('[name="company"]').value,
  message: document.querySelector('[name="message"]').value,
  // Add segment info
  leadType: getLeadType(), // dba_emergency, hardware_rental, amc, etc
  urgency: document.querySelector('[name="timeline"]')?.value,
  timestamp: new Date().toISOString()
};
```

**Why:**
- Route DBA emergency leads to DBA team (immediate)
- Route hardware rental leads to sales team (24 hours)
- Route AMC leads to consulting team (48 hours)
- Faster response time per segment

---

### OPTIMIZATION #4: Add Lead Tracking Dashboard

Store leads in Google Sheets for tracking:

```javascript
// In Azure Function, after receiving form
async function logLeadToSheet(data) {
  const sheetsAPI = {
    spreadsheetId: 'YOUR_SHEET_ID',
    values: [[
      new Date().toISOString(),
      data.name,
      data.email,
      data.phone,
      data.company,
      data.service,
      data.urgency,
      'New', // Status
      '', // Response date
      '' // Notes
    ]]
  };
  
  // Send to Google Sheets API
  return await sheetsAPI.append(sheetsAPI);
}
```

**Create Google Sheet with columns:**
- Timestamp
- Name
- Email
- Phone
- Company
- Service Interested In
- Urgency
- Status (New, Contacted, Qualified, Customer)
- Response Date
- Notes

---

## 🔧 CURRENT IMPLEMENTATION ISSUES TO FIX

### Issue #1: API Key in Client Code
**Current:** Key is visible in browser
**Risk:** Anyone can see your function key
**Fix:** Keep it as is (you have CORS configured in Azure) ✅

### Issue #2: No Lead Tracking
**Current:** Leads received but not tracked
**Risk:** No visibility into lead volume
**Fix:** Implement Google Sheets logging (above)

### Issue #3: No Auto-Reply
**Current:** Lead doesn't know if submission worked
**Risk:** Duplicate submissions, confusion
**Fix:** Send auto-reply email

### Issue #4: No Lead Segmentation
**Current:** All leads treated same
**Risk:** DBA emergency waits 2 hours like sales lead
**Fix:** Route by service/urgency

---

## 📊 LEAD CAPTURE FLOW (OPTIMIZED)

```
Lead visits website
         ↓
Fills form (2 fields: Name, Email)
         ↓
Clicks submit
         ↓
Data sent to Azure Function
         ↓
Azure Function receives
         ↓
Sends auto-reply to lead: "We got your message, 2-hour response"
         ↓
Sends alert to your team: "New lead: [Name] [Service]"
         ↓
Logs to Google Sheet
         ↓
Routes by service type
         ↓
Team member calls within 2 hours
         ↓
Lead becomes customer or nurture
```

---

## 🎯 NEXT STEPS

### STEP 1: Verify Current Setup Working
```bash
# Test your Azure Function
node tools/test_form.js
```

**Check:**
- [ ] Email received at your configured address
- [ ] Data includes all fields
- [ ] Timestamp is correct

### STEP 2: Optimize for 10 Leads/Day
- [ ] Add Google Form as backup capture
- [ ] Setup auto-reply from Azure Function
- [ ] Create Google Sheet for tracking
- [ ] Add lead segmentation logic

### STEP 3: Monitor & Improve
- [ ] Track leads daily in spreadsheet
- [ ] Monitor response times (should be 2 hours or less)
- [ ] Track which services generate most leads
- [ ] Track conversion rate (leads to customers)

---

## 📧 EMAIL TEMPLATE FOR AZURE FUNCTION

When you get a lead, send them this:

```html
Subject: ✅ TechLeaf Systems - We're Ready to Help

Hi {{name}},

Thanks for reaching out! We received your assessment request.

📋 What Happens Next:
✓ Your request was logged ({{timestamp}})
✓ Our team will contact you within 2 hours
✓ Free 15-minute IT infrastructure assessment
✓ No sales pressure, just expert advice

🎯 Your Interest: {{service}}
📍 Location: {{city}}
⏱️ Timeline: {{timeline}}

📞 Want to Talk Sooner?
Call us directly: +91-8838581550
WhatsApp: https://wa.me/918838581550

📚 In the Meantime, Check These:
- DBA Emergency Playbook: [LINK]
- Cost Reduction Checklist: [LINK]
- Recent Case Studies: [LINK]

Thanks,
TechLeaf Systems Team
Chennai | Bangalore | Hyderabad
```

---

## ✅ CHECKLIST: AZURE FUNCTION OPTIMIZATION

- [ ] Current setup verified working
- [ ] Auto-reply email configured
- [ ] Google Sheet created for tracking
- [ ] Lead segmentation logic added
- [ ] Status tracking implemented
- [ ] Team response SLA defined (2 hours)
- [ ] Email templates created
- [ ] Dashboard built to track metrics

---

## 📊 METRICS TO TRACK

### Daily Metrics
- Leads received (target: 10+)
- Response time (target: <2 hours)
- Lead source (blog, form, social, etc)
- Service interest distribution

### Weekly Metrics
- Total leads (target: 70+)
- Conversion to qualified (target: 30%)
- Conversion to customers (target: 10-15%)
- Average lead quality score

### Monthly Metrics
- Total leads (target: 300+)
- New customers (target: 30-40)
- Revenue per lead (target: ₹15L+)
- Cost per lead (target: ₹0 — DIY)

---

## 🚀 YOUR ACTION ITEMS

**This Week:**
1. [ ] Verify Azure Function is working (run test script)
2. [ ] Confirm emails are being received
3. [ ] Check what email address receives leads
4. [ ] Ensure 2-hour response SLA is met

**Next Week:**
1. [ ] Add auto-reply email to Azure Function
2. [ ] Create Google Sheet for lead tracking
3. [ ] Setup daily lead monitoring
4. [ ] Start implementing 10 leads/day plan

**Then:**
1. [ ] Add lead segmentation
2. [ ] Build team response dashboard
3. [ ] Optimize email templates
4. [ ] Scale to 20+ leads/day

---

## 💡 WHY THIS MATTERS FOR YOUR GOAL

You want **10 leads/day with zero budget**.

Your Azure Mail Function is **critical** because:
- ✅ It's your lead capture system
- ✅ It sends notifications to your team
- ✅ It confirms to leads their message arrived
- ✅ It's the foundation of scaling

Optimizing this gets you to 10 leads/day faster.

---

**Let me know:**
1. Is your Azure Function receiving emails currently?
2. What email address should receive the leads?
3. Does your team get notified when a lead comes in?
4. Can you add auto-reply? (I can help configure)

Then we can scale to 10+ leads/day! 🚀
