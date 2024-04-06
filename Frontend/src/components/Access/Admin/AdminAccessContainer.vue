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
    <AdminAccessUnit v-for="index in 8" :key="index" />
  </div>
</template>

<style scoped>

</style>