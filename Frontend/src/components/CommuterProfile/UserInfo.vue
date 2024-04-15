<script>

import PaymentMethod from "@/components/CommuterProfile/PaymentMethod.vue";

export default {
  name: "UserInfo",
  components: {PaymentMethod},
  props: {
    user: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      userType: ''
    }
  },
  methods: {
    getUserType() {
      if (this.$route.path === '/admin') {
        this.userType = 'Admin';
      } else {
        this.userType = 'Commuter';
      }
    }
  },
  mounted() {
    this.getUserType();
  }
}
</script>

<template>
  <div class="profile-container">
    <div class="name-section">
      <div style="display: flex; justify-content: center; align-items: center; flex-direction: column">
        <img src="../../assets/user.png" width="150rem" style="border-radius: 5rem; object-fit: contain"
             alt="The One True Samy"/>
        <div style="font-weight: bold;">{{ this.user.name }}</div>
        <div>{{ this.userType }}</div>
      </div>

    </div>
    <div class="user-information-header">
      <div id="section-1"
           style="margin-left: 1rem; flex: 2; display: flex; justify-content: center; align-items: flex-start; flex-direction: column">
        <div style="display:flex; flex-direction: column;">
          <div style="font-weight: bold">Email Address:</div>
          <div>{{ this.user.email }}</div>
        </div>
        <div style="display:flex; flex-direction: column;">
          <div style="font-weight: bold">Phone Number:</div>
          <div>{{ this.user.tel }}</div>
        </div>
      </div>
      <div id="section-2"
           style="margin-left: 1rem; flex: 2; display: flex; justify-content: center; align-items: flex-start; flex-direction: column">
        <div style="display:flex; flex-direction: column;">
          <div style="font-weight: bold">Home Address:</div>
          <div>{{ this.user.address }}</div>
        </div>
        <div style="display:flex; flex-direction: column;">
          <div style="font-weight: bold">Birth Date:</div>
          <div>{{ this.user.birthDate }}</div>
        </div>
      </div>
      <div id="section-3"
           style="margin-left: 1rem; flex: 2; display: flex; justify-content: center; align-items: flex-start; flex-direction: column">
        <div style="width: 100%;" v-if="this.$route.path === '/admin'">
          <div style="display:flex; flex-direction: column;">
            <div style="font-weight: bold">Company:</div>
            <div>{{ this.user.company }}</div>
          </div>

        </div>
        <div style="width: 100%;" v-else>
          <div style="width:100%; display:flex; flex-direction: column;">
            <div style="font-weight: bold">Payment Method:</div>
           <PaymentMethod/>
          </div>
        </div>
      </div>

    </div>

  </div>
</template>

<style scoped>
.name-section {
  padding: 2rem;
  margin-right: 2rem;
  border-radius: 1rem;
}

.profile-container {
  margin: 0.5rem;
  display: flex;
  flex-direction: row;
}

.user-information-header {
  width: 100%;
  background-color: #f1f1f1;
  padding: 10px;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  font-size: large;
}

#section-1 {
  display: flex;
  justify-content: space-around;
}

@media only screen and (max-width: 900px) {
  .profile-container {
    flex-direction: column;
  }

  .user-information-header {
    flex-direction: column;
  }
}
</style>