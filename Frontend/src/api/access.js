import Cookies from "js-cookie";

export const getAllAccess = async () => {
    const response = await fetch('http://localhost:8080/user/access/search', {
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