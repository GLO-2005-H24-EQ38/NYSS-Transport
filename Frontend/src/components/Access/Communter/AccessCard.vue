<script>
import stmLogo from '@/assets/stm_logo.png';
import rtcLogo from '@/assets/rtc_logo.jpg';
import samyLogo from '@/assets/samy.jpeg';
import BuyAccessPrompt from '@/components/Access/Communter/buyAccessPrompt.vue'

export default {
  name: "AccessCard",
  components: { BuyAccessPrompt },
  props: {
    access: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      quantity: 0,
      logo: ''
    }
  },
  methods: {
    decrementQuantity() {
      this.quantity = this.quantity - 1;
      if (this.quantity <= 0) {
        this.quantity = 0;

      }
    },
    incrementQuantity() {
      this.quantity = this.quantity + 1;
      if (this.quantity <= 0) {
        this.quantity = 0;

      }
    },
    getLogo() {
      if (this.access.company === 'STM') {
        this.logo = stmLogo;
      } else if (this.access.company === 'RTC') {
        this.logo = rtcLogo;
      } else {
        this.logo = samyLogo;
      }
    }
  },
  created() {
    if (this.access)
      this.getLogo();
  },
  updated() {
    if (this.access)
      this.getLogo();
  }
}
</script>

<template>
    <div class="access-card" style="position: relative">
    <div class="expirationDate" style="display: flex; justify-content: center; flex-direction: row">
      {{  this.access.accessType }}
        </div>
    <div class="card-body">
      <div class="card-title" style="display: flex; flex-direction: column">
        <div style="flex: 1; padding-top: 2rem; font-size: 1.70rem; color: black">
         {{ this.access.accessName }}
        </div>
      </div>
      <div style="display: flex; flex-direction: row">
        <div class="card-text" style="flex:1; justify-content: flex-end; display: flex; margin-top: 3rem">{{ "$" }}{{ this.access.price.toFixed(2) }}</div>
      </div>
    </div>
      <div style="margin-top: 1.5rem">
      <div @click="incrementQuantity()" v-if="!quantity" style="width: 100%" class="btn btn-primary btn-lg btn-block addButton">
        <i class="bi bi-plus-lg"></i>
        Add
      </div>
      <div v-if="quantity" style="width: 100%; display: flex; flex-direction: row">
        <div style="display: flex; flex-direction: row; flex: 3; justify-content: space-evenly; align-items: center">
         <i class="bi bi-dash-lg btn addButton" @click="decrementQuantity"></i>
          <div style="font-size: large">{{ quantity }}</div>
          <i class="bi bi-plus-lg btn addButton" @click="incrementQuantity"></i>
        </div>
        <buyAccessPrompt v-if="quantity > 0"  :accessId="this.access.accessId" :quantity="quantity" @close="quantity = 0" />
      </div>
    </div>
      <img
          class="logoPosition"
          style="height: 25%; object-fit: contain"
        :src="this.logo"
        alt="stm"/>
  </div>
</template>

<style scoped>
.access-card {
  transition: ease-in-out 0.25s;
  position: relative;
  width: 23rem;
  height: 15rem;
  margin: 20px;
  border-radius: 5px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}


.logoPosition {
  padding: 1px;
  border: none;
  position: absolute;
  top: 25%;
  border-top-right-radius: 0.5rem;
  right: 3%;
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

.card-title {
  font-size: 1.25rem;
  font-weight: bold;
  width: 60%;
  color: #000000;
}

.card-text {
  color: #000000;
  font-weight: bold;
  font-size: 2rem;
  flex-grow: 1;
}

.addButton {
  cursor: pointer;
  background-color: #01356a;
  border-color: transparent;
  display: flex;
  color: white;
  justify-content: center;
  align-items: center;
}

.expirationDate {
  transition: ease-in-out 0.25s;
  background-color: #0368cc;
  border: none;
  width: 100%;
  position: absolute;
  color: white;
  padding: 0.5rem 0.5rem ;
}

.addButton:hover {
  background-color: #0368cc;
  transition: ease-in-out 0.25s;
  color: white;
  cursor: pointer;
}

.access-card:hover {
  transition: ease-in-out 0.25s;
  cursor: pointer;
  box-shadow: 0 0 6px rgb(0, 82, 158);
}
</style>