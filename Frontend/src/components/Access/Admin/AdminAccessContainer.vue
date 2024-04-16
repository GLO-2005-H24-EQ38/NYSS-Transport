<script>
import AdminAccessUnit from '@/components/Access/Admin/AdminAccessUnit.vue'
import { getAdminAccess } from '@/api/access.js'

export default {
  name: 'AdminAccessContainer',
  components: { AdminAccessUnit },
  props: {
    accessCards: {
      type: Array,
      required: true
    }
  },
}
</script>

<template>

    <h3 style="margin:1rem">Active Accesses</h3>
    <div class="access-cards-container ">
      <AdminAccessUnit @deleteAccess="this.$emit('update')" v-for="(access,index) in this.accessCards" :key="index"
                       :access="access" />

  </div>
  <h3 style="margin:1rem">Inactive Accesses</h3>
  <div class="access-cards-container ">
    <AdminAccessUnit v-for="(access,index) in this.accessCards" :key="index" :showOutOfSale="true" :access="access" />
  </div>
</template>

<style scoped>
.access-cards-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin-top: 0.5rem;
  width: auto;

}
</style>