
export class Commuter {

    constructor(name,email,address,tel,password,dateOfBirth) {
        this.name = name;
        this.email = email;
        this.address = address;
        this.tel = tel;
        this.password = password;
        this.dateOfBirth = dateOfBirth;
    }
}

export class Admin {

    constructor(name, email, address, tel, password, dateOfBirth, adminCode, company) {
        this.name = name;
        this.email = email;
        this.address = address;
        this.tel = tel;
        this.password = password;
        this.dateOfBirth = dateOfBirth;
        this.company = company;
        this.adminCode = adminCode;

    }
}

export class AddPaymentMethod {
    constructor(cardNumber, holder, expirationDate) {
        this.cardNumber = cardNumber;
        this.expirationDate = expirationDate;
        this.holder = holder;
    }
}

export class SearchAccessQuery {

    constructor(name, accessType, company, price) {
        this.name = name;
        this.accessType = accessType;
        this.company = company;
        this.price = price;
    }

}

export class BuyAccessQuery {

    constructor(accessId,quantity) {
        this.accessId = accessId;
        this.quantity = quantity;
    }

}