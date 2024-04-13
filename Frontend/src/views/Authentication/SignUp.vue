<script>
import {Admin, Commuter} from "@/Objects.js";
import {signUp} from "@/api/signup.js";

export default {
  name: "SignUp",
  computed: {
    address() {
      return this.homeAddress + ', ' + this.city + ', ' + this.zipCode;
    }
  },
  data() {
    return {
      signUpOption: 'commuter',
      name: '',
      email: '',
      password: '',
      tel: null,
      dateOfBirth: null,
      city: '',
      zipCode: '',
      homeAddress: '',
      company: '',
      adminCode: null
    }
  },
  methods: {
    async createAccount() {
      if (this.signUpOption === 'commuter') {
        const commuter = new Commuter(this.name, this.email, this.address, this.tel, this.password, this.dateOfBirth)
        if(!await signUp(commuter)) {
          console.error('Failed to Sign Up Commuter')
        }
      } else {
        const admin = new Admin(this.name, this.email, this.address, this.tel, this.password, this.dateOfBirth, this.adminCode, this.company)
        if(!await signUp(admin)) {
          console.error('Failed to Sign Up Admin')
        }
      }
      this.$router.push('/login');
    }
  }
}
</script>

<template>
  <body class="backgroundQuebec" style="display: flex; justify-content: center; align-items: center">
  <div class="signup-container">
    <h3 style="margin: 1.5rem; display: flex; justify-content: center; font-weight: bold">Create Account</h3>
    <div class="btn-group btn-group-toggle" data-toggle="buttons"
         style="width: 100%; justify-content: space-around; margin: 1rem">
      <label>
        <input type="radio" name="options" v-model="signUpOption" value="commuter" autocomplete="off" checked> Commuter
      </label>
      <label>
        <input type="radio" name="options" v-model="signUpOption" value="admin" autocomplete="off"> Admin
      </label>
    </div>
    <form class="fill-up-form" @submit.prevent="createAccount">
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1"><i class="bi bi-person-fill"></i></span>
        <input type="text" class="form-control" placeholder="Full Name" aria-label="Full Name"
               aria-describedby="basic-addon1" v-model="name">
      </div>
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1"><i class="bi bi-calendar-date"></i></span>
        <input type="text" class="form-control" placeholder="Date of Birth" aria-label="Date of Birth"
               aria-describedby="basic-addon1" onfocus="(this.type='date')" onblur="(this.type='text')" v-model="dateOfBirth">
      </div>
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1"><i class="bi bi-house-fill"></i></span>
        <input type="text" class="form-control" placeholder="Address" aria-label="Address"
               aria-describedby="basic-addon1" v-model="homeAddress">
      </div>
      <div style="display: flex; justify-content: flex-start; align-items: flex-start; flex-direction: row">
        <div class="input-group mb-sm-3">
          <span class="input-group-text" id="basic-addon1"><i class="bi bi-buildings-fill"></i></span>
          <input type="text" class="form-control" placeholder="City" aria-label="City"
                 aria-describedby="basic-addon1" v-model="city">
        </div>
        <div class="input-group mb-sm-3">
          <span class="input-group-text" id="basic-addon1"><i class="bi bi-geo-alt-fill"></i></span>
          <input type="text" class="form-control" placeholder="Zip Code" aria-label="Zip Code"
                 aria-describedby="basic-addon1" v-model="zipCode">
        </div>
      </div>
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1"><i class="bi bi-telephone-fill"></i></span>
        <input type="tel" class="form-control" placeholder="Phone Number" aria-label="Phone Number"
               aria-describedby="basic-addon1" v-model="tel">
      </div>
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1"><i class="bi bi-envelope"></i></span>
        <input type="email" class="form-control" placeholder="Email Address" aria-label="Email Address"
               aria-describedby="basic-addon1" v-model="email">
      </div>
      <div class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1"><i class="bi bi-lock-fill"></i>
</span>
        <input type="password" class="form-control" placeholder="Password" aria-label="Password"
               aria-describedby="basic-addon1" v-model="password">
      </div>
      <div v-if="signUpOption==='admin'" class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1"><i class="bi bi-building-down"></i>
</span>
        <input type="text" class="form-control" placeholder="Company Name" aria-label="Company Name"
              v-model="company" aria-describedby="basic-addon1">
      </div>
      <div v-if="signUpOption==='admin'" class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1"><i class="bi bi-key-fill"></i>
</span>
        <input type="text" class="form-control" placeholder="Admin Code" aria-label="Admin Code"
              v-model="adminCode" aria-describedby="basic-addon1">
      </div>
      <div style="font-size: small">
        Already have an account ? <a href="/login">Login in here</a>
      </div>
      <div style="display: flex; justify-content: center; margin-top: 2rem">
        <button class="button" style="display: flex; justify-content: center; width: 100%">Create
          Account
        </button>
      </div>
    </form>
  </div>
  </body>
</template>

<style scoped>
.backgroundQuebec {
  background-image: url("@/assets/quebec-map.png");
  min-height: 100vh;
}

.button {
  border: none;
  border-radius: 0.5rem;
  padding: 0.5rem;
  background-color: #01356a;
  color: white;
}

.signup-container {
  margin: 1rem;
  padding: 1rem;
  border-radius: 0.75rem;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: whitesmoke
}
</style>