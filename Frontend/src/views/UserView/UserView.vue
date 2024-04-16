<script>
import UserInfo from '@/components/CommuterProfile/UserInfo.vue'
import TransactionContainer from '@/components/CommuterProfile/TransactionContainer.vue'
import Cookies from 'js-cookie'
import { getUser } from '@/api/getuser.js'
import { checkCommuterOnline } from '@/api/login.js'

export default {
  name: 'UserView',
  components: { TransactionContainer, UserInfo },
  data() {
    return {
      user: {
        name: '',
        email: '',
        tel: '',
        address: '',
        birthDate: '',
        company: ''
      }
    }
  },
  methods: {
    // fetch user informations
    async getUserInfo() {
      const res = await getUser()
      console.log('=------------------->', res)
      this.user.name = res.name
      this.user.address = res.address
      this.user.email = res.email
      this.user.tel = res.tel
      this.user.birthDate = res.dateOfBirth
      this.user.company = res.company
      return res
    },
    //validate token to check if user is still logged in
    async validateToken() {
      const response = await checkCommuterOnline()
      if (response.status !== 200) {
        Cookies.remove('commuterToken')
        this.$router.push('/login')
      }
    }
  },
  mounted() {

    this.getUserInfo()
  },
  created() {
    this.validateToken()
  }
}
</script>

<template>
  <div class="userView">
    <div style="flex: 4"><h2 style="margin:1rem">Profile</h2>
      <UserInfo :user="this.user" />
    </div>
  </div>
  <h2 style="margin:1rem">Wallet</h2>
  <TransactionContainer />
</template>

<style scoped>
.userView {
  display: flex;
  flex-direction: row
}

@media only screen and (max-width: 900px) {
  .userView {
    display: flex;
    flex-direction: column
  }

}
</style>