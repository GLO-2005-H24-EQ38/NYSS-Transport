import Cookies from "js-cookie";
import { URL_API } from '/src/api/url.js'

export const getAllAccess = async () => {
    const response = await fetch(URL_API + 'user/access/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': Cookies.get('commuterToken')
        },
        body: JSON.stringify({})
    });
    if (response.status === 200) {
        return await response.json();
    }
    else {
        return 0;
    }
}


export const searchAccess = async (access) => {
    const response = await fetch(URL_API + 'user/access/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': Cookies.get('commuterToken')
        },
        body: JSON.stringify(access)
    });
    if (response.status === 200) {
        return await response.json();
    }
    else {
        return 0;
    }
}