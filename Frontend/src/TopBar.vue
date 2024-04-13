<script>
import Cookies from 'js-cookie'

export default {
  name: 'TopBar',
  methods: {
    logout() {
      Cookies.remove('commuterToken');
      Cookies.remove('adminToken');
      this.$router.push('/login');
    }
  }
}
</script>

<template>
  <nav class="navbar navbar-dark nav-bar-container" style="height: 10%; padding: 0">
    <div class="nav-container">
      <div class="logo" style="flex: 1">
        <img style="object-fit: contain;  width: 10rem;" src="./assets/NYSS-White.png" />
      </div>
    </div>
    <div v-if="this.$route.path === '/'" class="nav-container"
         style="margin-left:2rem; flex: 2; justify-content: center">
      <div class="input-group rounded">
        <input type="search" class="form-control rounded" placeholder="Search" aria-label="Search"
               aria-describedby="search-addon" />
        <span style="background-color: transparent" class="input-group-text border-0" id="search-addon">
          <i class="bi bi-search" style="cursor:pointer; color: white"></i>
        </span>
      </div>
    </div>
    <div class="nav-container" style="flex:1; justify-content: right">
      <div class="nav-options" v-if="this.$route.path !== '/admin'"
           @click="this.$router.push('/')">
        Home
      </div>
      <div class="nav-options" v-if="this.$route.path !== '/admin'"
           @click="this.$router.push('/user')" >
        Profile
      </div>
      <div class="nav-options" v-if="this.$route.path !== '/login' && this.$route.path !== '/signup'"
           @click="logout()" >
        Logout
      </div>
    </div>
  </nav>

</template>

<style scoped>

div {
  font-family: "Calibri Light", fantasy;
  color: white;
  font-weight: bold;
}

.nav-bar-container {
  background-color: #01356a;
  color: #00529e;
}

.nav-container {
  display: flex;
  flex-direction: row;
}

#profile {

}

button {
  background-color: #01356a;
  border-radius: 2rem;
  border: none;
  outline: none;
  cursor: pointer;
  color: white;
}

button:hover {
  text-decoration: underline;
}

.nav-options {
  cursor: pointer;
  margin: 1rem ;
}

.nav-options:hover {
  text-decoration: underline;
}

</style>