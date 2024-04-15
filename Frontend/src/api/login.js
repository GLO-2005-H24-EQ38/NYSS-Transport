import { URL_API } from '/src/api/url.js';
import Cookies from 'js-cookie'

export const loginCommuter = async (email, password) => {
    const errorMsg = document.getElementById("error");
    errorMsg.innerText = "";
    const response = await fetch(URL_API + 'user/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify({"email": email, "password": password}),
    });
    console.log(response.status);
    const token = await response.json();
    if (response.status !== 200) {
    errorMsg.innerText = "Invalid Email or Password";
    } else {
        errorMsg.innerText = "Login Successful";
        errorMsg.style.color = "green";
    }
    console.log(token);
    return token;
}

export const loginAdmin = async (email, password, adminCode) => {
    const errorMsg = document.getElementById("error");
    const response = await fetch( URL_API + 'user/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"email": email, "password": password, "adminCode": adminCode})
    });
    if (response.status !== 200) {
    errorMsg.innerText = "Invalid Email or Password or Admin Code";
    } else {
        errorMsg.innerText = "Login Successful";
        errorMsg.style.color = "green";
    }
    const token = await response.json();
    console.log(token);
    return token;
}


export const checkCommuterOnline = async () => {
    const response = await fetch(URL_API + 'user/online', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': Cookies.get('commuterToken'),
            'Access-Control-Allow-Origin': '*',
        }});

    return response;
}


export const checkAdminOnline = async () => {
    const response = await fetch(URL_API + 'admin/online', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': Cookies.get('commuterToken'),
            'Access-Control-Allow-Origin': '*',
        }});

    return response

}