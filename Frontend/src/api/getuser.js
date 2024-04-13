import Cookies from "js-cookie";

export const getUser = async () => {
    let token, fetchURL;
    if (Cookies.get('commuterToken') === undefined || Cookies.get('commuterToken') === null) {
        fetchURL = 'http://localhost:8080/user/admin';
        token = Cookies.get('adminToken');
    }
    else {
        fetchURL = 'http://localhost:8080/user';
        token = Cookies.get('commuterToken');
    }
    const response = await fetch(fetchURL, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': token
        }
    });
    console.log(response.status);
    return await response.json();
}