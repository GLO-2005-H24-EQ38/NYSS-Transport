import Cookies from "js-cookie";
import {URL_API} from '/src/api/url.js'

export const addPaymentMethod = async (paymentMethod) => {
    const response = await fetch(URL_API + 'user/payment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': Cookies.get('commuterToken'),
            'Access-Control-Allow-Origin': '*'

        },
        body: JSON.stringify(paymentMethod),
    });
    console.log(response);
    if (response.status === 400) {
        let error = document.getElementById('errorAddPayment');
        error.innerText = "Invalid Card Information";
    }
    await response.json();
    return response;
}

export const getPaymentMethod = async () => {
    const response = await fetch(URL_API + 'user/payment', {
        method: 'GET',
        headers: {
            'Authorization': Cookies.get('commuterToken'),
            'Access-Control-Allow-Origin': '*'
        }
    });
    if (response.status === 200) {
        return await response.json();
    } else {
        return 0;
    }
}

export const deletePaymentMethod = async () => {
    const response = await fetch(URL_API + 'user/payment', {
        method: 'DELETE',
        headers: {
            'Authorization': Cookies.get('commuterToken'),
            'Access-Control-Allow-Origin': '*'
        }
    });
    console.log(response);
}