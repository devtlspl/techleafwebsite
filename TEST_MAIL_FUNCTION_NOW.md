# 🧪 TEST YOUR AZURE MAIL FUNCTION - DO THIS NOW

**Quick verification that your email system is working**

---

## ✅ QUICK TEST (2 minutes)

### Step 1: Open Browser Console
Press: `F12` (or `Ctrl+Shift+I`)

Click tab: **Console**

### Step 2: Paste This Test Code

```javascript
// TEST YOUR MAIL FUNCTION
fetch('https://mailsvx.azurewebsites.net/api/submit', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'x-functions-key': '7jQxXArv_ZXrVnH4ECxhqLS4Cme9pxtD9IuHOm6yv9gxAzFuL3y4RA=='
  },
  body: JSON.stringify({
    formType: 'test',
    name: 'Test Lead - ' + new Date().toLocaleString(),
    email: 'test@techleafsystems.com',
    phone: '+91-8838581550',
    company: 'TechLeaf Test',
    message: 'This is a test submission from the browser console',
    timestamp: new Date().toISOString()
  })
})
.then(response => {
  console.log('📨 Response Status:', response.status);
  return response.text();
})
.then(text => {
  console.log('✅ SUCCESS! Azure Function responded:');
  console.log(text);
})
.catch(error => {
  console.error('❌ ERROR! Something went wrong:');
  console.error(error.message);
})
```

### Step 3: Check Console Output

**If you see ✅ SUCCESS:**
```
📨 Response Status: 200
✅ SUCCESS! Azure Function responded:
[response message from Azure]
```
→ **Your mail function is working!** ✅

**If you see ❌ ERROR:**
```
❌ ERROR! Something went wrong:
[error message]
```
→ **There's a problem.** See "Troubleshooting" below.

### Step 4: Check Your Email

Look in email inbox for:
- From: Azure Function or noreply@...
- To: sales@techleafsystems.com or your email
- Subject: Something like "New Form Submission" or "Lead from website"

**If email received:** ✅ System is WORKING!  
**If no email:** ⚠️ Email routing may be misconfigured.

---

## 🔧 TROUBLESHOOTING

### Problem #1: Network Error
**Error:** "Failed to fetch" or CORS error

**Cause:** Azure Function is down or CORS not configured

**Fix:**
1. Check Azure portal: Is the function app running?
2. Check CORS settings: Is your domain allowed?
3. Try: `https://mailsvx.azurewebsites.net/api/submit` directly in browser

### Problem #2: 401 Unauthorized
**Error:** "401 Unauthorized" or "Invalid key"

**Cause:** Function key is wrong

**Fix:**
1. Get correct key from Azure Portal
2. Update in `assets/js/mail-api.js`
3. Update in `tools/test_form.js`
4. Update in this test

### Problem #3: 500 Internal Server Error
**Error:** "500 Internal Server Error"

**Cause:** Azure Function code has bug

**Fix:**
1. Check Azure Function logs
2. Check what data is being sent
3. Debug Azure Function code

### Problem #4: Email Not Received
**Error:** "Status 200" but no email

**Cause:** Email configuration in Azure Function wrong

**Fix:**
1. Check Azure Function code: Is it sending email?
2. Check email provider settings
3. Check spam folder
4. Check email is configured correctly

---

## 📊 WHAT SHOULD HAPPEN

### When Lead Fills Form on Website:

```
1. User enters: Name + Email
2. Clicks: "Get Free Assessment"
   ↓
3. Website sends to Azure Function
   ↓
4. Azure Function receives data
   ↓
5. Azure Function processes
   ↓
6. Sends email to: sales@techleafsystems.com (or configured email)
   ↓
7. Email contains: Name, Email, Phone, Company, Message
   ↓
8. Your team sees notification
   ↓
9. Team member calls lead within 2 hours
   ↓
10. Lead becomes customer ✅
```

---

## 🎯 VERIFY EACH STEP

### Step A: Form Submission
1. Go to: https://www.techleafsystems.com/contact.html
2. Fill form: Name + Email
3. Click: "Get Free Assessment"
4. See message: "✅ Got it! We'll contact you within 2 hours"

**Status:** ✅ Form works

### Step B: Azure Function Receives
1. Check browser Console (F12)
2. Look for "✅ SUCCESS" message
3. If present: Azure Function received data

**Status:** ✅ Function receives data

### Step C: Email Sent
1. Check your email inbox
2. Look for email from: noreply@... or Azure
3. Subject: Contains "New Lead" or "Form Submission"
4. Body: Contains name, email, message

**Status:** ✅ Email received

### Step D: Your Team Notified
1. Does your team get alerted?
2. Do they know immediately when new lead arrives?
3. Can they respond within 2 hours?

**Status:** ✅ Team notified

---

## 📧 YOUR EMAIL CONFIGURATION

### What We Know:
```
Azure Function: https://mailsvx.azurewebsites.net/api
Endpoint: /submit
Function Key: 7jQxXArv_ZXrVnH4ECxhqLS4Cme9pxtD9IuHOm6yv9gxAzFuL3y4RA==
```

### What We Need to Verify:
```
Receiving Email: [WHERE?]
Sender Email: [FROM WHERE?]
Email Provider: [WHICH ONE?]
Email Template: [CUSTOM OR DEFAULT?]
```

---

## 🚀 TO OPTIMIZE FOR 10 LEADS/DAY

### Now That We Know It Works:

**IMPROVEMENT #1: Auto-Reply to Leads**
Configure Azure Function to send auto-reply:
```
To: Lead's email
Subject: ✅ We received your request!
Body: 
  - Confirm receipt
  - Set expectations (2-hour response)
  - Share resources/links
  - Direct phone number
```

**Why:** Lead feels heard. Reduces anxiety. Increases trust.

**IMPROVEMENT #2: Lead Segmentation**
Route leads by service:
- DBA Emergency → To DBA team immediately
- Hardware Rental → To Sales team within 4 hours
- AMC → To Consulting team within 24 hours

**Why:** Faster response. Better conversion.

**IMPROVEMENT #3: Lead Tracking**
Log every lead to Google Sheet:
- Name, Email, Phone, Company
- Service, Urgency, Timestamp
- Status, Response Date, Customer Status

**Why:** Can see lead volume. Track conversion rate.

---

## ✅ YOUR CHECKLIST RIGHT NOW

- [ ] Open browser Console (F12)
- [ ] Paste test code (above)
- [ ] Check for ✅ SUCCESS message
- [ ] Check email inbox for test email
- [ ] Verify email received correctly
- [ ] Confirm subject & content are right
- [ ] Check Azure Function is working

**If all ✅:** System is ready for 10 leads/day!

---

## 🎯 NEXT STEPS

**If Everything Works:**
1. Start your 14-day DIY plan
2. Expect 5-10 leads from Day 1
3. Watch emails pour in

**If Something Broken:**
1. Try troubleshooting above
2. Share the error message
3. I'll help fix it

---

**Do this test RIGHT NOW and tell me what you see!** 🧪

What was the result?
- ✅ SUCCESS - Email received
- ❌ ERROR - Something wrong
- ⚠️ UNSURE - Not sure what happened
