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
  <div class="access-card">
    <img
        style="object-fit: contain"
        :src="this.logo"
        alt="stm"/>
    <div class="card-body">
      <div class="card-title" style="display: flex; flex-direction: row">
        <div style="flex: 1">
          {{ this.access.accessName }}
        </div>
        <div style="flex: 1; display: flex; justify-content: end; align-items: end">
          $ {{ this.access.price }}
        </div>
      </div>
      <div class="card-text">Type: {{ this.access.accessType }}</div>
    </div>
    <div style="margin: 1rem;">
      <div @click="incrementQuantity()" v-if="!quantity" style="width: 100%" class="btn btn-primary btn-lg btn-block">
        <i class="bi bi-plus-lg"></i>
        Add
      </div>
      <div v-if="quantity" style="width: 100%; display: flex; flex-direction: row">
        <div style="display: flex; flex-direction: row; flex: 3; justify-content: space-evenly; align-items: center">
         <i class="bi bi-dash-lg btn btn-outline-primary" @click="decrementQuantity"></i>
          <div style="font-size: large">{{ quantity }}</div>
          <i class="bi bi-plus-lg btn btn-outline-primary" @click="incrementQuantity"></i>
        </div>
        <buyAccessPrompt v-if="quantity > 0"  :accessId="this.access.accessId" :quantity="quantity" @close="quantity = 0" />
      </div>
    </div>
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
  width: 100%;
  height: 13rem;
  object-fit: fill;
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
  color: #000000;
}

.card-text {
  font-size: 1rem;
  color: #666;
  flex-grow: 1;
}

.addButton {
  cursor: pointer;
  color: dodgerblue;
  display: flex;
  justify-content: center;
  align-items: center;
}

.expirationDate {
  transition: ease-in-out 0.25s;
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.2);
  background-color: #ffffff;
  border: none;
  border-radius: 25px;
  padding: 8px;
  position: absolute;
  bottom: 30%;
  left: 50%;
  transform: translate(-50%, 0);
}

.addButton:hover {
  background-color: dodgerblue;
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