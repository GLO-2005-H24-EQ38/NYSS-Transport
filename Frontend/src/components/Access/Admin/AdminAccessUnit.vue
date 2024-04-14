<script>

import QRCodeTicket from "@/components/CommuterProfile/QRCodeTicket.vue";

export default {
  name: "AdminAccessUnit",
  components: {QRCodeTicket},
  data() {
    return {
      accessName: "2 passages",
      expDate: "2021-12-31",
      price: 3.75,
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
<!--          {{ accessName }}-->
<!--        </div>-->
<!--      </div>-->
<!--      <div style="display: flex; flex-direction: row">-->
<!--        <div class="card-text" style="flex:1">Type: Ticket</div>-->
<!--        <div class="card-text" style="flex:1; justify-content: flex-end; display: flex">Price : $ {{ price }}</div>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="width: 100%; justify-content: center; display: flex;">-->
<!--          <button class="btn btn-danger btn-block">Delete Access</button>-->
<!--    </div>-->
<!--  </div>-->
    <div class="access-card" style="position: relative">
    <div class="expirationDate" style="display: flex; justify-content: center; flex-direction: row">
      {{ 'Ticket' }} {{ "•" }}
        </div>
      <div class="expirationDate2" style="display: flex; justify-content: center; flex-direction: row">
      {{ expDate }}
        </div>
<!--    <img-->
<!--        style="object-fit: contain"-->
<!--        src="@/assets/stm_logo.png"-->
<!--        alt="stm"/>-->
    <div class="card-body">
      <div class="card-title" style="display: flex; flex-direction: column">
        <div style="width: 50%">
         Access Name
        </div>
        <div style="flex: 1; font-size: 1.70rem; color: black">
         {{ accessNumber }}
        </div>
      </div>
      <div style="display: flex; flex-direction: row">
        <div class="card-text" style="justify-content: flex-start; display: flex; font-size: 1.5rem; font-weight: bold; color: black">{{'2 passages RTC Quebec Pass Montly'
          }}</div>
      </div>
      <hr>
      <div class="card-text" style="justify-content: flex-end; display: flex; font-size: 1.5rem; font-weight: bold; color: black; margin-bottom: 1rem">{{ '$3.75' }}</div>
    </div>
      <div style="width: 100%; display: flex;">
        <button class="btn btn-danger" style="width: 100%; height: 3rem">Delete Access</button>
      </div>
<!--      <div class="invalid">Invalid</div>-->
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
  width: 20%;
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
  top: 3%;
  border-top-right-radius: 0.5rem;
  right: 24%;
  font-size: small;
  color: darkgray;
  font-weight: bold;
}

.expirationDate2 {
  padding: 1px;
  border: none;
  position: absolute;
  top: 3%;
  border-top-right-radius: 0.5rem;
  right: 3%;
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
  top: 60%;
  border-top-right-radius: 0.5rem;
  left: 5%;
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