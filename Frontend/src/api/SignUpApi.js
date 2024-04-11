
const URL = 'http://127.0.0.1:8080/';

export const signUp = async (user) => {
  const response = await fetch(URL + "user/signup", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(user),
  });
  return await response.json();
}


