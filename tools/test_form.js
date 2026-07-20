const MAIL_API_BASE = "https://mailsvx.azurewebsites.net/api";
const FUNCTION_KEY = "7jQxXArv_ZXrVnH4ECxhqLS4Cme9pxtD9IuHOm6yv9gxAzFuL3y4RA==";

async function testSubmit() {
  const data = {
    formType: 'sales',
    name: 'AI Test Lead',
    email: 'test@example.com',
    message: '[Interest: AMC / FMS] [Timeline: Immediate]\nJust testing the form submission logic!'
  };

  const headers = {
    "Content-Type": "application/json"
  };
  
  if (FUNCTION_KEY) {
    headers["x-functions-key"] = FUNCTION_KEY;
  }

  try {
    const response = await fetch(`${MAIL_API_BASE}/submit`, {
      method: "POST",
      headers: headers,
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      const message = await response.text();
      console.error(`ERROR: Response ${response.status} - ${message}`);
    } else {
      const result = await response.text();
      console.log("SUCCESS! Response:", result);
    }
  } catch (err) {
    console.error("NETWORK ERROR:", err.message);
  }
}

testSubmit();
