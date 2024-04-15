import {URL_API} from '@/api/url.js'
import Cookies from 'js-cookie'

export const buyAccess = async (cvc, query) => {
    const response = await fetch(URL_API + 'user/access/checkout', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': Cookies.get('commuterToken'),
            'Access-Control-Allow-Origin': '*',

            'cvc': cvc
        },
        body: JSON.stringify(query)
    });
    await response.json()

    return response;
}

export const getTransactions = async () => {
    const response = await fetch(URL_API + 'user/access', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': Cookies.get('commuterToken'),
            'Access-Control-Allow-Origin': '*'
        }
    });

    const data = await response.json()
    return data;


}