<script>
import {AddPaymentMethod} from "@/Objects.js";
import {addPaymentMethod} from "@/api/payment.js";
import {Modal} from "bootstrap";


export default {
  name: "PaymentMethodForm",
  props: {
  },
  data() {
    return {
      cardNumber: '',
      holder: '',
      expirationDate: '',
      modal_demo: null,
      cvc: null,
    }
  },
  methods: {
    openModal() {
      this.modal_demo.show()
    },
    closeModal() {
      this.modal_demo.toggle()
    },
    // add a new card to the payment method while checking the validity of the card
    async addCard() {
      const paymentMethod = new AddPaymentMethod(parseInt(this.cardNumber), this.holder, this.expirationDate);
      const res = await addPaymentMethod(paymentMethod)
      //validate the card
      if (res.status === 201) {
        this.closeModal();
        this.$emit('close')
      }
    }
  },
  beforeUnmount() {
    if (this.modal_demo._isShown) {
      this.closeModal()
    }
  },
  mounted() {
    this.modal_demo = new Modal('#paymentMethodModal', {})
  }
}
</script>
<template>
  <div class="modal fade" id="paymentMethodModal" aria-hidden="true" aria-labelledby="paymentMethodModalLabel"
       tabindex="-1">
    <div class="modal-dialog modal-dialog-centered" style="display: flex; justify-content: center; align-items: center">
      <div class="modal-content">
        <div class="modal-body" style="display: flex; justify-content: space-between">
          <h1 class="modal-title fs-5" id="paymentMethodModalLabel">Add Card</h1>
          <button type="button" class="btn-close" @click="closeModal"></button>
        </div>
        <div class="modal-body">
          <div id="paymentMethod">
            <div>
              <div id="CardNumber">
                <label for="CardNumber">Card Number</label>
                <input type="number" class="form-control" placeholder="1234 5678 9012 3456" aria-label="Username"
                       v-model="cardNumber" aria-describedby="basic-addon1">
              </div>
              <div class="holderExpCVC">
                <div id="CardHolder" style="flex: 2; margin-left: 0.25rem">
                  <label for="CardHolder">Card Holder Name:</label>
                  <input type="text" class="form-control" placeholder="Elon Musk" aria-label="Username"
                         v-model="holder" aria-describedby="basic-addon1">
                </div>
                <div id="ExpirationDate" style="flex:1; margin-left: 0.25rem;">
                  <label for="ExpirationDate">Exp. Date</label>
                  <input type="text" class="form-control" placeholder="01/23" aria-label="Username"
                         v-model="expirationDate" aria-describedby="basic-addon1">
                </div>
                <div id="CVC" style="flex: 1; margin-left: 0.25rem;">
                  <label for="CVC">CVC</label>
                  <input id="cvcAddPayment" type="password"  class="form-control" placeholder="123" aria-label="Username"
                       v-model="cvc"  aria-describedby="basic-addon1">
                </div>
              </div>
              <div id="errorAddPayment" style="color: red; font-size: small"></div>
              <div style="display: flex; justify-content: flex-end; margin-top: 1rem">
                <button type="button" class="btn btn-primary" @click="addCard">Add Card</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="addPayment">
    <a href="#" @click="openModal">Add Payment Method</a>
  </div>


</template>

<style scoped>

.holderExpCVC {
  display: flex; flex-direction: row; margin-top: 1rem
}

@media screen and (max-width: 500px) {
  .holderExpCVC {
    flex-direction: column;
  }
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  width: max-content;
}
.addPayment:hover {
  cursor: pointer;
  text-decoration: underline;
}
</style>