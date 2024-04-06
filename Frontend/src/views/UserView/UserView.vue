<script>
import PaymentMethod from "@/components/CommuterProfile/PaymentMethod.vue";

import UserInfo from "@/components/CommuterProfile/UserInfo.vue";
import AccessCard from "@/components/Access/AccessCard.vue";
import TransactionContainer from "@/components/CommuterProfile/TransactionContainer.vue";

export default {
  name: "UserView",
  components: {TransactionContainer, AccessCard, PaymentMethod, UserInfo}
}
</script>

<template>
  <h2 style="margin:1rem">Profile</h2>
  <UserInfo />
  <h2 style="margin:1rem">Payment Method</h2>
  <PaymentMethod />
  <h2 style="margin:1rem">Wallet</h2>
  <TransactionContainer/>
</template>

<style scoped>

</style>