<script>
import PaymentMethod from "@/components/CommuterProfile/PaymentMethod.vue";

import UserInfo from "@/components/CommuterProfile/UserInfo.vue";
import TransactionContainer from "@/components/CommuterProfile/TransactionContainer.vue";
import Cookies  from "js-cookie";

export default {
  name: "UserView",
  components: {TransactionContainer, PaymentMethod, UserInfo},
  mounted() {
    console.log(Cookies.get('commuterToken'));
    if (!Cookies.get('commuterToken')){
      this.$router.push('/login');
    }
  }
}
</script>

<template>
  <div class="userView">
    <div style="flex: 4"><h2 style="margin:1rem">Profile</h2>
      <UserInfo/>
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