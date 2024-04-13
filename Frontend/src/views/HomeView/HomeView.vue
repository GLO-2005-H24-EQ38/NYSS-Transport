<script>
import AccessContainer from "@/components/Access/Communter/AccessContainer.vue";
import Cookies from "js-cookie";
import SearchSideBar from "@/views/HomeView/SearchSideBar.vue";

export default {
  name: "HomeView",
  components: {SearchSideBar, AccessContainer},
  data() {
    return {

    }
  },
  mounted() {
    if (!Cookies.get('commuterToken')) {
      this.$router.push('/login');
    }
    document.querySelector('.access-container').style.overflow = 'auto';
    document.body.style.overflow = 'hidden';
  },
}
</script>

<template>
  <div style="display: flex; flex-direction: row">
    <div id="justBeforeBar" style="flex:1; display: flex; justify-content: center;   background-color: #f3f3f3;">
            <SearchSideBar />
    </div>
    <div class="access-container" style="flex:5; overflow: auto;">
          <AccessContainer/>
    </div>
  </div>
</template>

<style scoped>
.access-container {
  height: 100vh;
  overflow-y: auto;
}

</style>
