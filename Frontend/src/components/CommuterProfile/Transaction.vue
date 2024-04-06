<script>
import QrcodeVue from "qrcode.vue";
import QRCodeTicket from "@/components/CommuterProfile/QRCodeTicket.vue";

export default {
  name: "Transaction",
  components: {QRCodeTicket, QrcodeVue},
  data() {
    return {
      accessNumber: "40001",
      transactionNumber: "40001",
      expDate: "12/24",
      transactionDate: "01/05/2024",
      QRValue: this.accessNumber,
      showQRCode: false,
    }
  }
}
</script>

<template>
  <div id="transaction" style="display: flex; flex-direction: row">
    <div style="display: flex; flex-direction: column; flex: 1">
      <div>
        Access Number : #40001
      </div>
      <div>
        Transaction Number : #40001
      </div>
    </div>
    <div style="display: flex; flex-direction: column; flex: 1">
      <div>
        Exp. Date : 12/24
      </div>
      <div>
        Transaction Date : 01/05/2024
      </div>
    </div>
    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center">
      <a href="#" @click="showQRCode = !showQRCode">Show QR Code</a>
    </div>
    <QRCodeTicket v-if="showQRCode" />
<!--    <div>-->
<!--      <qrcode-vue :value="QRValue" size="50" level="H"></qrcode-vue>-->
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
</style>