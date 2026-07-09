const MAIL_API_BASE = "https://mailsvx.azurewebsites.net/api";

// Replace this with your full 'default' Host Key from the Azure Portal
const FUNCTION_KEY = "7jQxXArv_ZXrVnH4ECxhqLS4Cme9pxtD9IuHOm6yv9gxAzFuL3y4RA==";

/**
 * Sends data to a specified endpoint of the Mailsvx API
 */
async function sendMailApi(endpoint, data) {
  const headers = {
    "Content-Type": "application/json"
  };
  
  if (FUNCTION_KEY) {
    headers["x-functions-key"] = FUNCTION_KEY;
  }

  const response = await fetch(`${MAIL_API_BASE}/${endpoint}`, {
    method: "POST",
    headers: headers,
    body: JSON.stringify(data)
  });

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || `Unable to send form to /${endpoint}`);
  }

  return response.text();
}

/**
 * For all forms sending to /api/submit
 */
export async function sendSubmitForm(data) {
  return await sendMailApi("submit", data);
}

/**
 * Make it globally available if not using JS modules
 */
window.sendSubmitForm = sendSubmitForm;
