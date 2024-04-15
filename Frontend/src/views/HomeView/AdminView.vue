<script>
import UserInfo from "@/components/CommuterProfile/UserInfo.vue";
import AdminAccessContainer from "@/components/Access/Admin/AdminAccessContainer.vue";
import AddAccess from "@/components/Access/Admin/AddAccess.vue";
import {getUser} from "@/api/getuser.js";
import Cookies from "js-cookie";
import { checkAdminOnline, checkCommuterOnline } from '@/api/login.js'

export default {
  name: "AdminView",
  components: {AddAccess, AdminAccessContainer, UserInfo},
  data() {
    return {
      user: {
        name: '',
        email: '',
        tel: '',
        address: '',
        birthDate: '',
        company: '',
      }
    }
  },
  methods: {
    async getUserInfo() {
      const res = await getUser();
      console.log('=------------------->', res);
      this.user.name = res.name;
      this.user.address = res.address;
      this.user.email = res.email;
      this.user.tel = res.tel;
      this.user.birthDate = res.dateOfBirth;
      this.user.company = res.company;
      return res
    },
    async validateToken() {
      const response = await checkAdminOnline()

      if (response.status !== 200) {
        Cookies.remove('commuterToken')
        this.$router.push('/login')
      }else {
        console.log('Token is valid')
      }
    }
  },
  mounted() {
    this.validateToken()
    console.log('=------------------->', this.getUserInfo());
    this.getUserInfo();
  },
}
</script>

<template>
  <h2 style="margin:1rem">Profile</h2>
  <UserInfo :user="this.user" />
  <AddAccess :admin-company="this.user.company" />
  <h2 style="margin:1rem">List of Active Access</h2>
  <AdminAccessContainer />
</template>

<style scoped>

</style>