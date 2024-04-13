<script>
import AccessCard from "@/components/Access/Communter/AccessCard.vue";
import Transaction from "@/components/CommuterProfile/Transaction.vue";

export default {
  name: "TransactionContainer",
  components: {Transaction}
}
</script>

<template>
    <div class="transaction-container">
    <Transaction v-for="index in 8" :key="index" />
  </div>

</template>

<style scoped>
.transaction-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin-top: 40px;
}
</style>