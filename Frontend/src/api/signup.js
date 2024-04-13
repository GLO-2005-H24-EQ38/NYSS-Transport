import { URL_API } from '/src/api/url.js'

export const signUp = async (user) => {
  const response = await fetch(URL_API + "user/signup", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(user),
  });
  console.log(JSON.stringify(user))
  console.log(response);
  return await response.json();
}


