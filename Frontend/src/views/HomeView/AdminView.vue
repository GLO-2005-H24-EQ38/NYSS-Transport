<script>
import UserInfo from '@/components/CommuterProfile/UserInfo.vue'
import AdminAccessContainer from '@/components/Access/Admin/AdminAccessContainer.vue'
import AddAccess from '@/components/Access/Admin/AddAccess.vue'
import { getUser } from '@/api/getuser.js'
import Cookies from 'js-cookie'
import { checkAdminOnline } from '@/api/login.js'
import { getAdminAccess } from '@/api/access.js'

export default {
  name: 'AdminView',
  components: { AddAccess, AdminAccessContainer, UserInfo },
  data() {
    return {
      user: {
        name: '',
        email: '',
        tel: '',
        address: '',
        birthDate: '',
        company: ''
      },
      updateAccessContainer: false,
      accessCardsList: []
    }
  },
  methods: {
    // fetch user informations
    async getUserInfo() {
      const res = await getUser()
      this.user.name = res.name
      this.user.address = res.address
      this.user.email = res.email
      this.user.tel = res.tel
      this.user.birthDate = res.dateOfBirth
      this.user.company = res.company
      return res
    },
    async getAccessCards() {
      const res = await getAdminAccess()
      this.accessCardsList = res
    },
    //validate token to check if user is still logged in
    async validateToken() {
      const response = await checkAdminOnline()

      if (response.status !== 200) {
        Cookies.remove('adminToken')
        this.$router.push('/login')
      } else {
        console.log('Token is valid')
      }
    }
  },
  mounted() {
    this.validateToken()
    this.getUserInfo()
    this.getAccessCards()
  }
}
</script>

<template><h2 style="margin:1rem">List of Active Access</h2>
  <h2 style="margin:1rem">Profile</h2>
  <UserInfo :user="this.user" />
  <AddAccess :admin-company="this.user.company" @close="getAccessCards" />
  <h2 style="margin:1rem">Access List</h2>
  <AdminAccessContainer @update="getAccessCards" :accessCards="accessCardsList" />
</template>

<style scoped>

</style>