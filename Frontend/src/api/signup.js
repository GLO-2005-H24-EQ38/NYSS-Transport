export const URL = 'http://localhost:8080/';

export const signUp = async (user) => {
  const response = await fetch(URL + "user/signup", {
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


