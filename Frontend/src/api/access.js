import Cookies from "js-cookie";
import {URL_API} from '/src/api/url.js'

export const getAllAccess = async () => {
    const response = await fetch(URL_API + 'user/access/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': Cookies.get('commuterToken'),
            'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify({})
    });


    if (response.status === 200) {
        return await response.json();
    } else {
        return 0;
    }
}

export const getAccess = async (SearchAccessQuery) => {
    const response = await fetch(URL_API + 'user/access/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': Cookies.get('commuterToken'),
            'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify(SearchAccessQuery)
    });
    if (response.status === 200) {
        return await response.json();
    } else {
        return 0;
    }
}

export const addAccess = async (query) => {
    const response = await fetch(URL_API + 'admin/access', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': Cookies.get('adminToken'),
            'Access-Control-Allow-Origin': '*'

        },
        body: JSON.stringify(query)
    });
    if (response.status === 400) {
        let error = document.getElementById('errorAddAccess');
        error.innerText = "Please fill all fields correctly";
    }
    await response.json();
    return response;
}

