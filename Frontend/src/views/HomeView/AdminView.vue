<script>
import UserInfo from "@/components/CommuterProfile/UserInfo.vue";
import AccessManager from "@/components/Access/Admin/AccessManager.vue";
import AdminAccessContainer from "@/components/Access/Admin/AdminAccessContainer.vue";
import AdminAccessUnit from "@/components/Access/Admin/AdminAccessUnit.vue";
import Cookies from "js-cookie";

export default {
  name: "AdminView",
  components: {AdminAccessUnit, AdminAccessContainer, AccessManager, UserInfo},
  data() {
    return {
    }
  },
  mounted() {
    if (!Cookies.get('adminToken')) {
      this.$router.push('/login');
    }
  },
}
</script>

<template>
  <h2 style="margin:1rem">Profile</h2>
  <UserInfo />
<!--  <div style="display:flex; flex-direction: row">-->
<!--    <h2 style="margin:1rem">Manage Access</h2>-->
<!--    <h2 class="bi bi-gear-wide-connected" style="display: flex; align-items: center"></h2>-->
<!--  </div>-->
<!--  <AccessManager />-->
  <h2 style="margin:1rem">List of Active Access</h2>
  <div class="add-access">+ Add Access</div>
  <AdminAccessContainer />
</template>

<style scoped>
.add-access {
  background-color: #01356a;
  margin-left: 1rem;
  margin-right: 1rem;
  margin-bottom: 0.25rem;
  border-radius: 1rem;
  padding: 1rem;
  color: white;
  transition: ease-in-out 0.25s;

}
.add-access:hover {
  cursor: pointer;
  background-color: #0368cc;
  transition: ease-in-out 0.25s;
}
</style>