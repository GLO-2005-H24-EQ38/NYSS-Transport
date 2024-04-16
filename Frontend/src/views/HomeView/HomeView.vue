<script>
import AccessContainer from '@/components/Access/Communter/AccessContainer.vue'
import Cookies from 'js-cookie'
import SearchSideBar from '@/views/HomeView/SearchSideBar.vue'
import { SearchAccessQuery } from '@/Objects.js'
import { getAccess, getAllAccess } from '@/api/access.js'
import { checkCommuterOnline } from '@/api/login.js'

export default {
  name: 'HomeView',
  components: { SearchSideBar, AccessContainer },
  data() {
    return {
      accessList: []
    }
  }, methods: {
    // fetch acccess cards based on user search query
    async getAccessCards(searchQuery) {
      const query = new SearchAccessQuery(searchQuery.name, searchQuery.accessType, searchQuery.company, searchQuery.price)
      this.accessList = await getAccess(query)
    },
    // fetch all valid access from database
    async getAllAccessCards() {
      this.accessList = await getAllAccess()
    }, async validateToken() {
      const response = await checkCommuterOnline()

      if (response.status !== 200) {
        Cookies.remove('commuterToken')
        this.$router.push('/login')
      }
    }
  },
  mounted() {
    this.validateToken();
    this.getAllAccessCards()
  }
}
</script>

<template>
  <div>
    <AccessContainer :accessCards="accessList" />
    <SearchSideBar @searchQuery="getAccessCards" />
  </div>
</template>

<style scoped>



</style>
