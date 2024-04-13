<script>
import AccessCard from "@/components/Access/Communter/AccessCard.vue";
import {getAllAccess} from "@/api/access.js";

export default {
  name: "Access-Container",
  components: {AccessCard},
  data() {
    return {
      accessCards: [],
    }
  },
  methods: {
    async getAccessCards() {
      const res = await getAllAccess();
      console.log(res);
      for (let i = 0; i < res.length; i++) {
        this.accessCards.push(res[i]);
      }
      return res;

    }
  },
  created() {
    console.log('=====================================');
    this.getAccessCards();
  }
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
  justify-content: space-around;
  margin-top: 40px;
}
</style>