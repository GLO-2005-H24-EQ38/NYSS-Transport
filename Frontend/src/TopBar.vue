<script>
export default {
  name: "TopBar"
}
</script>

<template>
  <nav class="navbar navbar-dark nav-bar-container" style="height: 12vh; padding: 0">
     <div class="nav-container">
      <div class="logo" style="flex: 1">
        <img style="object-fit: contain;  width: 200px;" src="./assets/NYSS-White.png"/>
      </div>
    </div>
    <div v-if="this.$route.path === '/'" class="nav-container" style="margin-left:2rem; flex: 2; justify-content: center">
    <div class="input-group rounded">
  <input type="search" class="form-control rounded" placeholder="Search" aria-label="Search" aria-describedby="search-addon" />
  <span class="input-group-text border-0" id="search-addon">
    <i class="bi bi-search"></i>
  </span>
</div>
         </div>
    <div class="nav-container" style="flex:1; justify-content: right">
        <div style="margin-right: 2rem">Home</div>
        <div style="margin-right: 2rem">About</div>
        <div id="profile" v-if="this.$route.path === '/'" @click="this.$router.push('/user')" style="margin-right: 2rem">Profile</div>
      </div>
  </nav>

</template>

<style scoped>

div {
  font-family: "Calibri Light",fantasy;
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
  cursor: pointer;
}

button {
  background-color: #01356a;
  border-radius: 2rem;
  border: none;
  outline: none;
  cursor: pointer;
  color: white;
}
button:hover{
  text-decoration: underline;
}


</style>