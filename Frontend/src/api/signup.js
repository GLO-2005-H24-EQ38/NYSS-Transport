import { URL_API } from '/src/api/url.js'

export const signUp = async (user) => {
  const response = await fetch(URL_API + "user/signup", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    },
    body: JSON.stringify(user),
  });


  if (response.status === 400) {
    const element = document.getElementById('errorSignUp');
    element.innerText = "Please fill all fields correctly";
  } else if (response.status === 409) {
    const element = document.getElementById('errorSignUp');
    element.innerText = "User already exists with this email";
  }
  await response.json();
  return response;
}


