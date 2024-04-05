<script>
export default {
  name: "LogIn"
}
</script>

<template>
  <body class="backgroundQuebec"style="display: flex; justify-content: center; align-items: center">
    <div class="login-container">
      <h3 style="margin-bottom: 1rem; display: flex; justify-content: center; font-weight: bold">Login</h3>
      <form class="fill-up-form">
        <div class="input-group mb-lg-4">
          <span class="input-group-text" id="basic-addon1"><i class="bi bi-envelope"></i></span>
          <input type="email" class="form-control" placeholder="Email Address" aria-label="Email Address"
                 aria-describedby="basic-addon1">
        </div>
        <div class="input-group mb-lg-4">
          <span class="input-group-text" id="basic-addon1"><i class="bi bi-lock-fill"></i>
</span>
          <input type="password" class="form-control" placeholder="Password" aria-label="Password"
                 aria-describedby="basic-addon1">
        </div>
        <div style="font-size: small">
          Don't have an account ? <a href="/signup">Sign up here</a>
        </div>
        <div style="display: flex; justify-content: center; margin-top: 2rem">
                 <button class="button" style="display: flex; justify-content: center; width: 100%">Login</button>
        </div>
      </form>
    </div>
  </body>
</template>

<style scoped>
.backgroundQuebec {
  background-image: url("@/assets/quebec-map.png");
  height: 88vh;
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