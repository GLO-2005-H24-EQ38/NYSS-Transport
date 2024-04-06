<script>
import AccessCard from "@/components/Access/Communter/AccessCard.vue";

export default {
  name: "Access-Container",
  components: {AccessCard}
}
</script>

<template>
  <div class="access-cards-container">
    <AccessCard v-for="index in 9" :key="index" />
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