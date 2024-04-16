<script>
import { rtcLogo, stLevisLogo, stmLogo, rtLongueuilLogo } from '@/assets/logo.js'

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
      } else if (this.access.company === 'STLevis'){
        this.logo = stLevisLogo;
      } else if (this.access.company === 'RTL'){
        this.logo = rtLongueuilLogo;
      } else {
        this.logo = 'No Logo Found'
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
    <div style="padding-left: 0.5rem; padding-right: 0.5rem">
      <div class="card-body">
        <div class="card-title" style="display: flex; flex-direction: row;">
          <div
            style="flex: 3; font-size: 2rem; color: black; display: flex; justify-content: flex-start; align-items: center">
            {{ this.access.accessName }}
          </div>
          <div id="image" style="flex:1">
            <div style="display: flex;flex-direction: column; justify-content: flex-end">
              <div style="display: flex; justify-content: flex-end; margin-bottom: 0.5rem">
                <div class="expirationDate"
                     style="width: max-content; display: flex; justify-content: center; flex-direction: row">
                  {{ this.access.accessType }}
                </div>
              </div>
              <img
                class="logoPosition"
                :src="this.logo"
                alt="stm" />
            </div>
          </div>
        </div>

        <hr>
        <div style="display: flex; flex-direction: row; justify-content: space-between">
          <div style="display: flex; justify-content: flex-start; align-items: center" class="card-title">Price</div>
          <div
            style="display: flex; justify-content: flex-end; flex: 1; font-size: 1.70rem; color: black; font-weight: bold"
            class="card-text">${{ this.access.price.toFixed(2) }}
          </div>
        </div>
      </div>
    </div>

    <div style="margin-top: 0.5rem">
      <div @click="incrementQuantity()" v-if="!quantity" style="width: 100%"
           class="btn btn-primary btn-lg btn-block addButton">
        <i class="bi bi-plus-lg"></i>
        Add
      </div>
      <div v-if="quantity" style="width: 100%; display: flex; flex-direction: row">
        <div style="display: flex; flex-direction: row; flex: 3; justify-content: space-evenly; align-items: center">
          <i class="bi bi-dash-lg btn addButton" @click="decrementQuantity"></i>
          <div style="font-size: large">{{ quantity }}</div>
          <i class="bi bi-plus-lg btn addButton" @click="incrementQuantity"></i>
        </div>
        <buyAccessPrompt v-if="quantity > 0" :accessId="this.access.accessId" :quantity="quantity" />
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

.logoPosition {
  height: 4rem;
  border: none;
  border-top-right-radius: 0.5rem;
}

.card-body {
  position: relative;
  padding-top: 0.5rem;
  margin: 0;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;

}

.card-title {
  font-size: 1.25rem;
  color: darkgray;
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
  border-radius: 1rem;
  background-color: #0368cc;
  border: none;
  color: white;
  font-size: 1rem;
  padding: 0.25rem 0.75rem;
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