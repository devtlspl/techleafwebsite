import os

js_file = 'assets/js/main.js'

with open(js_file, 'r', encoding='utf-8') as f:
    content = f.read()

azure_logic = """
// Azure Function Submission Handler
window.sendSubmitForm = async function(data) {
  // NOTE: Adjust the '/api/sendEmail' part if your specific Azure function name is different!
  const endpoint = 'https://mailsvx.azurewebsites.net/api/sendEmail';
  
  const response = await fetch(endpoint, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
    body: JSON.stringify(data)
  });
  
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  
  return await response.json();
};
"""

if "window.sendSubmitForm" not in content:
    # Append to the very end of the file
    with open(js_file, 'a', encoding='utf-8') as f:
        f.write("\n" + azure_logic)
    print("Azure function logic appended successfully.")
else:
    print("Logic already exists!")
