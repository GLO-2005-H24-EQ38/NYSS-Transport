<script>
import AdminAccessUnit from "@/components/Access/Admin/AdminAccessUnit.vue";
import {getAdminAccess} from "@/api/access.js";

export default {
  name: "AdminAccessContainer",
  components: {AdminAccessUnit},
  data() {
    return {
      list: []
    }
  },
  methods: {
    async getAccessCards() {
      const res = await getAdminAccess();
      this.list = res;
    },
  },
  mounted() {
    this.getAccessCards();
  },
  updated() {
    this.getAccessCards();
  }
}
</script>

<template>
  <div class="access-cards-container">
    <AdminAccessUnit v-for="(access,index) in this.list" :key="index" :access="access"/>
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