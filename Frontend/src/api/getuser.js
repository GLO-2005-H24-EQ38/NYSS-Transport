import Cookies from "js-cookie";
import { URL_API } from '/src/api/url.js'

export const getUser = async () => {
    let token, fetchURL;
    if (Cookies.get('commuterToken') === undefined || Cookies.get('commuterToken') === null) {
        fetchURL = URL_API +'user/admin';
        token = Cookies.get('adminToken');
    }
    else {
        fetchURL = URL_API + 'user';
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