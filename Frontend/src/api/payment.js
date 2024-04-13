import Cookies from "js-cookie";
export const addPaymentMethod = async (paymentMethod) => {
    const response = await fetch('http://localhost:8080/user/payment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': Cookies.get('commuterToken')
        },
        body: JSON.stringify(paymentMethod),
    });
    console.log(response);
    return await response.json();
}

export const getPaymentMethod = async () => {
    const response = await fetch('http://localhost:8080/user/payment', {
        method: 'GET',
        headers: {
            'Authorization': Cookies.get('commuterToken')
        }
    });
    console.log(response);
    return await response.json();
}

export const deletePaymentMethod = async () => {
    const response = await fetch('http://localhost:8080/user/payment', {
        method: 'DELETE',
        headers: {
            'Authorization': Cookies.get('commuterToken')
        }
    });
    console.log(response);
}