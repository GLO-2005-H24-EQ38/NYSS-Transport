<script>
import AccessContainer from '@/components/Access/Communter/AccessContainer.vue'
import Cookies from 'js-cookie'
import SearchSideBar from '@/views/HomeView/SearchSideBar.vue'
import { SearchAccessQuery } from '@/Objects.js'
import { getAccess, getAllAccess } from '@/api/access.js'

export default {
  name: 'HomeView',
  components: { SearchSideBar, AccessContainer },
  data() {
    return {
      accesslist: []
    }
  }, methods: {
    async getAccessCards(searchQuery) {
      const query = new SearchAccessQuery(searchQuery.name, searchQuery.accessType, searchQuery.company, searchQuery.price)
      console.log(query)
      this.accesslist = await getAccess(query)
      console.log(this.accesslist)

    },
    async getAllAccessCards() {
      this.accesslist = await getAllAccess()
      console.log(this.accesslist)
    }

  },
  mounted() {
    if (!Cookies.get('commuterToken')) {
      this.$router.push('/login')
    }

    this.getAllAccessCards()


  }
}
</script>

<template>
  <div>
    <AccessContainer :accessCards="accesslist" />
    <SearchSideBar @searchQuery="getAccessCards" />
  </div>
</template>

<style scoped>



</style>
