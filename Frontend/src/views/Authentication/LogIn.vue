<script>
import {loginAdmin, loginCommuter} from "@/api/login.js";
import Cookies from 'js-cookie';
export default {
  name: "LogIn",
  data() {
    return {
      loginOption: 'commuter',
      email: '',
      password: '',
      adminCode: null,
    }
  },
  methods: {
    // TODO A revoir avec userCookie
    async login() {
      if (this.loginOption === 'commuter') {
        const res = await loginCommuter(this.email, this.password);
        console.log("Login Commuter")
        if(res.token)
          Cookies.set('commuterToken', res.token, { expires: 7});
          Cookies.remove('adminToken');

          this.$router.push('/');
      } else {
        const res = await loginAdmin(this.email, this.password, this.adminCode);
        console.log("Login Admin")
        if(res.token)
          Cookies.set('adminToken', res.token, { expires: 7 });
          Cookies.remove('commuterToken');
          this.$router.push('/admin');
      }
    }
  }
}
</script>

<template>
  <body class="backgroundQuebec" style="display: flex; justify-content: center; align-items: center">
  <div class="login-container">
    <h3 style="margin-bottom: 1rem; display: flex; justify-content: center; font-weight: bold">Login</h3>
    <div class="btn-group btn-group-toggle" data-toggle="buttons" style="width: 100%; justify-content: space-around; margin: 1rem">
      <label>
        <input type="radio" name="options" v-model="loginOption" value="commuter" autocomplete="off" checked> Commuter
      </label>
      <label>
        <input type="radio" name="options" v-model="loginOption" value="admin" autocomplete="off"> Admin
      </label>
    </div>
    <form class="fill-up-form" @submit.prevent="login">
      <div class="input-group mb-lg-4">
        <span class="input-group-text" id="basic-addon1"><i class="bi bi-envelope"></i></span>
        <input type="email" class="form-control" placeholder="Email Address" aria-label="Email Address"
             v-model="email"  aria-describedby="basic-addon1">
      </div>
      <div class="input-group mb-lg-4">
          <span class="input-group-text" id="basic-addon1"><i class="bi bi-lock-fill"></i>
</span>
        <input type="password" class="form-control" placeholder="Password" aria-label="Password"
             v-model="password"  aria-describedby="basic-addon1">
      </div>
      <div v-if="loginOption === 'admin'" class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1"><i class="bi bi-key-fill"></i>
</span>
        <input type="text" class="form-control" placeholder="Admin Code" aria-label="Admin Code"
              v-model="adminCode" aria-describedby="basic-addon1">
      </div>
      <span style="font-size: small; color: red" id="error"></span>
      <div style="font-size: small">
        Don't have an account ? <a href="/signup">Sign up here</a>
      </div>
      <div style="display: flex; justify-content: center; margin-top: 2rem;flex-direction: column">
        <button class="button" style="display: flex; justify-content: center; width: 100%">Login</button>
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

.login-container {
  padding: 2rem;
  border-radius: 0.75rem;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: whitesmoke
}
</style>