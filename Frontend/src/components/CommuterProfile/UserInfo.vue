<script>
import Avatar from 'vue-avatar'

export default {
  name: "UserInfo",
  components: {
    Avatar
  }
}
</script>

<template>
  <div class="profile-container">
    <div class="user-information-header" style="display: flex; flex-direction: row;">
      <div style="display: flex; justify-content: center; align-items: center; flex-direction: column">
      <img src="../../assets/stm_logo.png" width="100px" style="border-radius: 1rem; object-fit: contain" alt="The One True Samy"/>
    <div style="font-weight: bold; flex: 1">Samy K.</div>
        <a href="#">Edit</a>
          </div>
    <div id="section-1" style="margin-left: 1rem; flex: 2; display: flex; justify-content: center; align-items: flex-start; flex-direction: column">
      <div style="display:flex; flex-direction: column;">
        <div style="font-weight: bold">Email Address:</div>
        <div>samy_khalfallah@nyss-support.ca</div>
      </div>
      <div style="display:flex; flex-direction: column;">
        <div style="font-weight: bold">Phone Number:</div>
        <div>(418) 555-SAMY</div>
      </div>
    </div>
    <div id="section-2" style="margin-left: 1rem; flex: 2; display: flex; justify-content: center; align-items: flex-start; flex-direction: column">
      <div style="display:flex; flex-direction: column;">
        <div style="font-weight: bold">Home Address:</div>
        <div>The One True Samy Island, Quebec</div>
      </div>
      <div style="display:flex; flex-direction: column;">
        <div style="font-weight: bold">Birth Date:</div>
        <div>2000-01-01</div>
      </div>
    </div>
    </div>

  </div>
</template>

<style scoped>
.profile-container {
  margin: 0.5rem;
}
.user-information-header {
  background-color: #f1f1f1;
  padding: 10px;
  border-radius: 20px;
}
</style>