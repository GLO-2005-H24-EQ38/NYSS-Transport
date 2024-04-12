<script>
import AccessContainer from "@/components/Access/Communter/AccessContainer.vue";
import {tokensList} from "@/api/login.js";

export default {
  name: "HomeView",
  components: {AccessContainer},
  data() {
    return {
          // TODO A revoir avec userCookie
      tokens: tokensList
    }
  },
  // TODO A revoir avec userCookie
  mounted() {
    if (this.tokens.length === 0) {
      this.$router.push('/login');
    }
  },
  unmounted() {
    this.tokens = [];
  }
}
</script>

<template>
  <AccessContainer />
</template>
