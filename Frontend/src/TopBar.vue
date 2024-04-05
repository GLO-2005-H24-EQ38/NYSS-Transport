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
    <div class="nav-container" style="flex:1; justify-content: right">
        <div style="margin-right: 2rem">Home</div>
        <div style="margin-right: 2rem">About</div>
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