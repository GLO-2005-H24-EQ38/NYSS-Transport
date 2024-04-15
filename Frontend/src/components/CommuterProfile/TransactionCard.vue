<script>
import QRCodeTicket from "@/components/CommuterProfile/QRCodeTicket.vue";

export default {
  name: "TransactionCard",
  components: {QRCodeTicket},
  props: {
    transaction: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      accessNumber: "",
      transactionNumber: "",
      expDate: "",
      transactionDate: "",
      QRValue: null,
      showQRCode: false,
    }
  },
  mounted() {
    console.log(this.transaction)
    this.accessNumber = this.transaction.accessNumber
    this.transactionNumber = this.transaction.transactionNumber
    this.expDate = this.transaction.expirationDate
    this.transactionDate = this.transaction.transactionDate
    this.QRValue = [this.accessNumber, this.transactionNumber, this.expDate, this.transactionDate]
  }
}
</script>

<template>
<!--  <div class="access-card" style="position: relative">-->
<!--    <div class="expirationDate" style="display: flex; justify-content: center">-->
<!--         Expires on {{ expDate }}-->
<!--        </div>-->
<!--    <img-->
<!--        style="object-fit: contain"-->
<!--        src="@/assets/stm_logo.png"-->
<!--        alt="stm"/>-->
<!--    <div class="card-body">-->
<!--      <div class="card-title" style="display: flex; flex-direction: row">-->
<!--        <div style="flex: 1">-->
<!--         Access N.# : {{ accessNumber }}-->
<!--        </div>-->
<!--      </div>-->
<!--      <div style="display: flex; flex-direction: row">-->
<!--        <div class="card-text" style="flex:1">Type: Ticket</div>-->
<!--        <div class="card-text" style="flex:1; justify-content: flex-end; display: flex">Purchased : {{ transactionDate }}</div>-->
<!--      </div>-->
<!--      <div class="card-text">Transaction N.#: {{ transactionNumber }}</div>-->
<!--    </div>-->
<!--    <QRCodeTicket />-->
<!--  </div>-->
    <div class="access-card" style="position: relative">
    <div class="expirationDate" style="display: flex; justify-content: center; flex-direction: row">
      {{ 'Ticket' }} {{ "•" }}
        </div>
      <div class="expirationDate2" style="display: flex; justify-content: center; flex-direction: row">
      {{ this.expDate }}
        </div>
<!--    <img-->
<!--        style="object-fit: contain"-->
<!--        src="@/assets/stm_logo.png"-->
<!--        alt="stm"/>-->
    <div class="card-body">
      <div class="card-title" style="display: flex; flex-direction: column">
        <div style="flex: 1">
         Access n.
        </div>
        <div style="flex: 1; font-size: 1.70rem; color: black">
         {{ this.accessNumber }}
        </div>
      </div>
      <div style="display: flex; flex-direction: row">
        <div class="card-text" style="flex:1; justify-content: flex-start; display: flex">Purchased : {{ this.transactionDate }}</div>
      </div>
      <hr>
      <div class="card-text">Transaction #</div>
      <div class="card-text" style="margin-bottom: 1rem">{{ this.transactionNumber }}</div>
    </div>
<!--      <div class="invalid">Invalid</div>-->
    <QRCodeTicket :q-r-value="this.QRValue" />
      <img
          class="logoPosition"
        src="@/assets/rtc_logo.jpg"
        alt="stm"/>
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
  width: 35%;
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

.expirationDate {
  padding: 1px;
  border: none;
  position: absolute;
  top: 5%;
  border-top-right-radius: 0.5rem;
  right: 25%;
  font-size: small;
  color: darkgray;
  font-weight: bold;
}

.expirationDate2 {
  padding: 1px;
  border: none;
  position: absolute;
  top: 5%;
  border-top-right-radius: 0.5rem;
  right: 5%;
  color: forestgreen;
  font-size: small;
  font-weight: bold;
}

.invalid {
  border: none;
  position: absolute;
  top: 60%;
  background-color: darkred;
  padding: 0.5rem 1rem;
  right: 5%;
  color: white;
  font-size: small;
  font-weight: bold;
}

.logoPosition {
  padding: 1px;
  border: none;
  position: absolute;
  top: 20%;

  border-top-right-radius: 0.5rem;
  right: 5%;
}

.card-title {
  font-size: 1rem;
  color: darkgray;
}

.card-text {
  font-size: 1rem;
  color: darkgray;
}

.access-card:hover {
  transition: ease-in-out 0.25s;
  cursor: pointer;
  box-shadow: 0 0 6px rgb(104, 104, 104);
}
</style>