<script>
import Transaction from "@/components/CommuterProfile/Transaction.vue";
import AdminAccessUnit from "@/components/Access/Admin/AdminAccessUnit.vue";

export default {
  name: "AdminAccessContainer",
  components: {AdminAccessUnit, Transaction}
}
</script>

<template>
<div class="access-cards-container">
    <AdminAccessUnit v-for="index in 3" :key="index" />
  </div>
</template>

<style scoped>
.access-cards-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin-top: 40px;
}
</style>