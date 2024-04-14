<script>
import PaymentMethodForm from "@/components/CommuterProfile/PaymentMethodForm.vue";
import {deletePaymentMethod, getPaymentMethod} from "@/api/payment.js";

export default {
  name: "paymentMethod",
  components: {PaymentMethodForm},
  props:{
     buyingAccess:{
       type: Boolean,
       default: false
     }

  },

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
    <div v-if="paymentExists" class="PaymentMethod">
      <div class="paymentContainer" style="display: flex; align-items: start; flex-direction: row">
        <div class="info" style="flex:3; display:flex;font-weight: bold; flex-direction: row"><i
            :class="icon"
            style="margin-right:0.5rem; font-size:24px; color: #01356a"></i>
          ···· {{ cardNumber.substring(1)}} {{ ','  }}
          <div style="display:flex; font-weight: bold">Exp. Date: {{ expDate }}
        </div>
        </div>
        <div class="removeBtn" style="flex:1 ; width: 100%;display: flex; justify-content: flex-end;">
        <button :hidden="buyingAccess" class="btn btn-danger" @click="removeCard">Remove Card</button>
      </div>
      </div>
    </div>
    <div v-else class="PaymentMethod">
      <PaymentMethodForm v-if="paymentExists === false && buyingAccess === false" @close="getCard" :paymentcallback="getCard"/>
      <div v-if="buyingAccess" style="display: flex; justify-content: center">
        <button class="btn btn-primary" @click="this.$router.push('/user'); " style="background: #01356a">Go add Card</button>
      </div>
    </div>


</template>

<style scoped>

</style>