<script>
import AccessContainer from "@/components/Access/Communter/AccessContainer.vue";
import Cookies from "js-cookie";

export default {
  name: "HomeView",
  components: {AccessContainer},
  data() {
    return {

    }
  },
  mounted() {
    if (!Cookies.get('commuterToken')) {
      this.$router.push('/login');
    }
  },
}
</script>

<template>
  <AccessContainer />
</template>
