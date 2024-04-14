<script>
import PaymentMethod from "@/components/CommuterProfile/PaymentMethod.vue";

import UserInfo from "@/components/CommuterProfile/UserInfo.vue";
import TransactionContainer from "@/components/CommuterProfile/TransactionContainer.vue";
import Cookies  from "js-cookie";
import {getUser} from "@/api/getuser.js";

export default {
  name: "UserView",
  components: {TransactionContainer, PaymentMethod, UserInfo},
  data() {
    return {
      user: {
        name: '',
        email: '',
        tel: '',
        address: '',
        birthDate: '',
        company: '',
      }
    }
  },
  methods: {
    async getUserInfo() {
      const res = await getUser();
      console.log('=------------------->', res);
      this.user.name = res.name;
      this.user.address = res.address;
      this.user.email = res.email;
      this.user.tel = res.tel;
      this.user.birthDate = res.dateOfBirth;
      this.user.company = res.company;
      return res
    }
  },
  mounted() {
    console.log(Cookies.get('commuterToken'));
    if (!Cookies.get('commuterToken')){
      this.$router.push('/login');
    }
    this.getUserInfo();
  }
}
</script>

<template>
  <div class="userView">
    <div style="flex: 4"><h2 style="margin:1rem">Profile</h2>
      <UserInfo :user="this.user"/>
    </div>
    <div>
      <h2 style="margin:1rem; flex: 1">Payment Method</h2>
      <div>
        <PaymentMethod/>

      </div>
    </div>
  </div>

  <h2 style="margin:1rem">Wallet</h2>
  <TransactionContainer/>
</template>

<style scoped>
.userView {
  display: flex;
  flex-direction: row
}

@media only screen and (max-width: 900px) {
  .userView {
    display: flex;
    flex-direction: column
  }

}
</style>