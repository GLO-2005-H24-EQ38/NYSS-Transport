<script>
import QrcodeVue from "qrcode.vue";

export default {
  name: "QRCodeTicket",
  components: {QrcodeVue},
  data() {
    return {
      QRValue: "40001"
    }
  }
}
</script>

<template>
  <div class="modal fade" id="qrCodeTicket" aria-hidden="true" aria-labelledby="asasa" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered" style="display: flex; justify-content: center; align-items: center">
    <div class="modal-content">
      <div class="modal-body">
        <div style="display: flex; justify-content: center; align-items: center;flex-direction: column; margin-bottom: 20px">
     <img src="@/assets/NYSS-Blue.png" alt="logo" style="width: auto; height: 100px; margin-bottom: 20px">
        <qrcode-vue :value="QRValue" size="250" level="Q"></qrcode-vue>
      <div style="margin-top: 1rem">{{ QRValue }}</div>
<!--          <div style="display: flex; justify-content: center; align-items: center; margin-top: 1rem">-->
<!--            <button class="btn btn-primary btn-block" data-bs-dismiss="modal">Redeem Now</button>-->
<!--          </div>-->
      </div>
      </div>
    </div>
  </div>
</div>
<div class="btn btn-secondary" style="display: flex; justify-content: center; align-items: center" href="#" data-bs-target="#qrCodeTicket" data-bs-toggle="modal">Show QR Code</div>
<!--    <div class="modal-background">-->
<!--    <div class="modal-content">-->
<!--      <div style="display: flex; justify-content: center; align-items: center;flex-direction: column; margin-bottom: 20px">-->
<!--     <img src="@/assets/NYSS-Blue.png" alt="logo" style="auto; height: 100px; margin-bottom: 20px">-->
<!--        <qrcode-vue :value="QRValue" size="250" level="Q"></qrcode-vue>-->
<!--      <div style="margin-top: 1rem">{{ QRValue }}</div>-->
<!--      </div>-->
<!--    </div>-->
<!--    </div>-->
</template>

<style scoped>
.modal-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1050;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  width: 300px;
}
</style>