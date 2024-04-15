<script>
import AccessCard from "@/components/Access/Communter/AccessCard.vue";

export default {
  name: "Access-Container",
  components: {AccessCard},
  props: {
    accessCards: {
      type: Array,
      required: true
    }
  },

}
</script>

<template>
  <div class="access-cards-container">
    <AccessCard v-for="(access, index) in this.accessCards" :key="index" :access="access"/>
  </div>

</template>

<style scoped>
.access-cards-container {
  display: flex;
  flex-wrap: wrap;
  min-height: 75vh;
  justify-content: center;
  margin-top: 40px;
}
</style>