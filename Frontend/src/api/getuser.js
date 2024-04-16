import Cookies from "js-cookie";
import { URL_API } from '/src/api/url.js'

export const getUser = async () => {
    let token, fetchURL;
    if (Cookies.get('commuterToken') === undefined || Cookies.get('commuterToken') === null) {
        fetchURL = URL_API +'admin';
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
            'Authorization': token,
            'Access-Control-Allow-Origin': '*'
        }
    });
    return await response.json();
}