
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

    constructor(name,email,address,tel,password,dateOfBirth,company) {
        this.name = name;
        this.email = email;
        this.address = address;
        this.tel = tel;
        this.password = password;
        this.dateOfBirth = dateOfBirth;
        this.company = company;

    }


}