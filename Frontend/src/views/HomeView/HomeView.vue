<script>
import AccessContainer from "@/components/Access/Communter/AccessContainer.vue";
import Cookies from "js-cookie";
import SearchSideBar from "@/views/HomeView/SearchSideBar.vue";

export default {
  name: "HomeView",
  components: {SearchSideBar, AccessContainer},
  data() {
    return {}
  },
  mounted() {
    if (!Cookies.get('commuterToken')) {
      this.$router.push('/login');
    }
  },
}
</script>

<template>
  <div>
    <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#staticBackdrop"
            aria-controls="staticBackdrop">
      Search Here
    </button>

    <div class="offcanvas offcanvas-start" data-bs-backdrop="static" tabindex="-1" id="staticBackdrop"
         aria-labelledby="staticBackdropLabel">
      <div class="offcanvas-header">
        <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
      </div>
      <div class="offcanvas-body">
        <div>
          <SearchSideBar />
        </div>
      </div>
    </div>
    <AccessContainer/>
  </div>
</template>

<style scoped>

</style>
