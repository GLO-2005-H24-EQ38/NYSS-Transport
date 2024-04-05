<script>
import AccessCard from "@/views/HomeView/AccessCard.vue";

export default {
  name: "Access-Container",
  components: {AccessCard}
}
</script>

<template>
  <div class="restaurant-cards">
    <AccessCard v-for="index in 8" :key="index" />
  </div>

</template>

<style scoped>
.restaurant-cards {
  display: flex;
  flex-wrap: wrap;
  justify-content: start;
  margin-top: 40px;
}
</style>