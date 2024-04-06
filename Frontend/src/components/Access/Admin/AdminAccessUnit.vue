<script>
import QrcodeVue from "qrcode.vue";

export default {
  name: "AdminAccessUnit",
  components: {QrcodeVue},
  data() {
    return {
      inputEnabled: false
    }
  },
  methods: {
    modifyAccess() {
      this.inputEnabled = true;
    }
  }
}
</script>

<template>
 <div id="transaction" style="display: flex; flex-direction: row">
    <div style="display: flex; flex-direction: column; flex: 5">
      <div style="display: flex; flex-direction: row">
        <div style="flex:1; display: flex; justify-content: flex-start">Access Name</div>
        <div style="flex:2;">
          <input disabled value="2 Passages" />
        </div>
      </div>
      <div style="display: flex; flex-direction: row">
        <div style="flex:1; display: flex; justify-content: flex-start">Access Price</div>
        <div style="flex:2;">
          <input disabled value="$ 3.79" />
        </div>
      </div>
    </div>
    <div style="display: flex; flex-direction: column; flex: 5">
      <div style="display: flex; flex-direction: row">
        <div style="flex:1; display: flex; justify-content: flex-start">Access Type</div>
        <div style="flex:2;">
          <input disabled value="Ticket" />
        </div>
      </div>
      <div style="display: flex; flex-direction: row">
        <div style="flex:1; display: flex; justify-content: flex-start">Access Exp. Date</div>
        <div style="flex:2;">
          <input disabled value="01/01/2025" />
        </div>
      </div>
    </div>
   <div style="display: flex; flex-direction: column; flex: 1; justify-content: center; align-items: center">
      <div style="display: flex; flex-direction: row; ">
        <i id="modify" class="bi bi-gear-fill" @click="modifyAccess" style="margin: 0.5rem;"></i>
        <i id="delete" class="bi bi-trash3-fill" style="margin: 0.5rem;"></i>
      </div>
    </div>
<!--    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center">-->
<!--      <a href="#">Show QR Code</a>-->
<!--    </div>-->

  </div>
</template>

<style scoped>
#transaction {
  background-color: #f1f1f1;
  margin-left: 1rem;
  margin-right: 1rem;
  margin-bottom: 0.25rem;
  border-radius: 1rem;
  padding: 1rem;
}

#modify {
  cursor: pointer;
}
#delete {
  cursor: pointer;
}
</style>