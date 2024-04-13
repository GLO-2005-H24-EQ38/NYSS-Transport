import Cookies from "js-cookie";

export const getUser = async () => {
    const response = await fetch('http://localhost:8080/user', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': Cookies.get('commuterToken')
        }
    });
    console.log(response.status);
    return await response.json();
}