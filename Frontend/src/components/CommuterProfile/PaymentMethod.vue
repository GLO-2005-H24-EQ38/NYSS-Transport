<script>
import PaymentMethodForm from "@/components/CommuterProfile/PaymentMethodForm.vue";
import {deletePaymentMethod, getPaymentMethod} from "@/api/payment.js";

export default {
  name: "paymentMethod",
  components: {PaymentMethodForm},
  data() {
    return {
      paymentExists: false,
      cardNumber: '',
      expDate: '',
      holder: '',
      icon: 'fa fa-credit-card',
    }
  },
  methods: {
    async getCard() {
      const res = await getPaymentMethod();
      if (res !== 0) {
        this.paymentExists = true;
        this.setupCard(res);
      } else {
        this.paymentExists = false;
      }
    },
    setupCard(res) {
      this.cardNumber = res.cardNumber;
      this.expDate = res.expirationDate;
      this.holder = res.holder;
      if (this.cardNumber.startsWith('3')) {
        this.icon = 'fa fa-cc-amex';
      }
      else if (this.cardNumber.startsWith('4')) {
        this.icon = 'fa fa-cc-visa';
      } else if (this.cardNumber.startsWith('5')) {
        this.icon = 'fa fa-cc-mastercard';
      } else if (this.cardNumber.startsWith('6')) {
        this.icon = 'fa fa-cc-discover';
      }
    },
    async removeCard() {
      const res = await deletePaymentMethod();
      console.log(res);
      await this.getCard()
    }
  },
  created() {
    this.getCard();
  },
  updated() {
    this.getCard();
  }
}
</script>

<template>
  <div>
    <div v-if="paymentExists" class="PaymentMethod"
         style="display: flex; justify-content: flex-start; align-items: start; flex-direction: column">
      <div style="display: flex; align-items: start; flex-direction: column">
        <div style="display:flex; justify-content:center; align-items: center; font-weight: bold"><i
            :class="icon"
            style="margin-right:0.5rem; font-size:24px; color: #01356a"></i>Credit
          Card ending in ···· {{ cardNumber.substring(1) }}
        </div>
        <div style="display:flex; justify-content:flex-start; align-items: center; font-weight: bold">Exp. Date: {{ expDate }}
        </div>
      </div>
      <div style="width: 100%;display: flex; justify-content: flex-end;">
        <button class="btn btn-danger" @click="removeCard">Remove Card</button>
      </div>
    </div>
    <div v-else class="PaymentMethod">
      <PaymentMethodForm v-if="paymentExists === false" @close="getCard" :paymentcallback="getCard"/>
    </div>
  </div>


</template>

<style scoped>
.PaymentMethod {
  background-color: #f1f1f1;
  padding: 1rem;
  margin: 0.5rem;
  border-radius: 20px;
}
</style>