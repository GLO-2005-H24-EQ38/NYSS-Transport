<script>
import QrcodeVue from "qrcode.vue";
import QRCodeTicket from "@/components/CommuterProfile/QRCodeTicket.vue";

export default {
  name: "Transaction",
  components: {QRCodeTicket, QrcodeVue},
  data() {
    return {
      accessNumber: "40001",
      transactionNumber: "217000548",
      expDate: "01/07/24",
      transactionDate: "01/05/2024",
      QRValue: this.accessNumber,
      showQRCode: false,
    }
  }
}
</script>

<template>
  <div class="access-card" style="position: relative">
    <img
        style="object-fit: contain"
        src="@/assets/stm_logo.png"
        alt="stm"/>
    <div class="card-body">
      <div class="card-title" style="display: flex; flex-direction: row">
        <div style="flex: 1">
         Access N.# : {{ accessNumber }}
        </div>
      </div>
      <div class="registerVisitButton">
         Expires on {{ expDate }}
        </div>
      <div style="display: flex; flex-direction: row">
        <div class="card-text" style="flex:1">Type: Ticket</div>
        <div class="card-text" style="flex:1; justify-content: flex-end; display: flex">Purchased : {{ transactionDate }}</div>
      </div>
      <div class="card-text">Transaction N.#: {{ transactionNumber }}</div>
    </div>
    <QRCodeTicket />
  </div>
</template>

<style scoped>
.access-card {
  transition: ease-in-out 0.25s;
  position: relative;
  width: 23rem;
  height: 100%;
  margin: 20px;
  border-radius: 5px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.access-card img {
  transition: ease-in-out 0.25s;
  width: 60%;
  height: 7rem;
  object-fit: contain;
}

.card-body {
  position: relative;
  padding-top: 20px;
  padding-left: 10px;
  padding-right: 10px;
  margin: 0;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;

}

.registerVisitButton {
  background-color: #01356a;
  padding: 1px;
  border: none;
  position: absolute;
  top: -115%;
  border-top-right-radius: 0.5rem;
  left: 67%;
  color: white;
}

.card-title {
  font-size: 1.25rem;
  font-weight: bold;
  color: #000000;
}

.card-text {
  font-size: 1rem;
  color: #666;
  flex-grow: 1;
}

.access-card:hover {
  transition: ease-in-out 0.25s;
  cursor: pointer;
  box-shadow: 0 0 6px rgb(104, 104, 104);
}
</style>