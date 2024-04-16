<script>
import { rtcLogo, stLevisLogo, stmLogo, rtLongueuilLogo } from '@/assets/logo.js'
import QRCodeTicket from '@/components/CommuterProfile/QRCodeTicket.vue'

export default {
  name: 'TransactionCard',
  components: { QRCodeTicket },
  props: {
    transaction: {
      type: Object,
      required: true
    },
    qrCodeValue: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      accessName: '',
      accessNumber: '',
      accessType: '',
      transactionNumber: '',
      accessCompany: '',
      expDate: '',
      numberOfPassage: '',
      transactionDate: '',
      type: '',
      showQRCode: false,
      expired: null,
      logo: null
    }
  }, mounted() {
    this.accessName = this.transaction.accessName
    this.accessType = this.transaction.accessType
    this.accessNumber = this.transaction.accessNumber
    this.transactionNumber = this.transaction.transactionNumber
    this.expDate = this.transaction.expirationDate
    this.accessCompany = this.transaction.company
    this.numberOfPassage = this.transaction.numberOfPassage
    this.transactionDate = this.transaction.transactionDate
    this.type = this.transaction.accessType
    // check if the access is expired to be used in text color style
    this.expired = new Date().getDate() > new Date(this.expDate).getDate()
    this.getLogo();
  },
  methods: {
    // get the logo of the company
    getLogo() {
      if (this.accessCompany === 'STM') {
        this.logo = stmLogo;
      } else if (this.accessCompany === 'RTC') {
        this.logo = rtcLogo;
      } else if (this.accessCompany === 'STLevis') {
        this.logo = stLevisLogo;
      } else if (this.accessCompany === 'RTL') {
        this.logo = rtLongueuilLogo;
      } else {
        this.logo = 'No Logo Found'
      }
    }
  }
}
</script>

<template>
  <div class="access-card" style="position: relative">
    <div class="expirationDate" style="display: flex; justify-content: center; flex-direction: row">
      {{ this.accessType }} {{ '•' }}
    </div>
    <div class="expirationDate2" style="display: flex; justify-content: center; flex-direction: row"
         :style="{color: expired ? 'red': 'green'}">
      {{ expDate }}
    </div>
    <div v-if="numberOfPassage" class="expirationDate3" style="display: flex; justify-content: center; flex-direction: row">
    {{'Number Of Passages : '}}  {{ numberOfPassage }}
    </div>
    <div class="card-body">
      <div class="card-title" style="display: flex; flex-direction: row; margin-top: 1rem">
        <div
          style="flex: 3; font-size: 2rem; color: black; display: flex; justify-content: flex-start; align-items: center">
          {{ this.accessName }}
        </div>
        <div id="image" style="flex:1">
          <div style="display: flex;flex-direction: column; justify-content: flex-end">
            <img
              class="logoPosition"
              :src="this.logo"
              :alt="this.accessCompany"  />
          </div>
        </div>
      </div>
      <div style="display: flex; flex-direction: row">
        <div class="card-text" style="flex:1; justify-content: flex-start; display: flex">Purchased : {{ transactionDate
          }}
        </div>
      </div>
      <hr>
      <div class="card-text">Transaction #</div>
      <div class="card-text" style="margin-bottom: 1rem">{{ this.transactionNumber }}</div>
    </div>
    <QRCodeTicket :number="accessNumber" />
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

.expirationDate3 {
  border: none;
  position: absolute;
  top: 5%;
  color: darkgray;
  left: 3%;
  font-size: small;
  font-weight: bold;
}

.logoPosition {
  padding: 1px;
  border: none;
  position: absolute;
  top: 25%;

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