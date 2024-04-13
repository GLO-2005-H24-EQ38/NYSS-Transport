<script>
import {AddPaymentMethod} from "@/Objects.js";
import {addPaymentMethod} from "@/api/payment.js";


export default {
  name: "PaymentMethodForm",
  props: {
  },
  data() {
    return {
      cardNumber: '',
      holder: '',
      expirationDate: '',
    }
  },
  methods: {
   async addCard() {
      const paymentMethod = new AddPaymentMethod(parseInt(this.cardNumber), this.holder, this.expirationDate);
      const res = await addPaymentMethod(paymentMethod)

      if (  "Successfully added payment method" === res.message ) {

        this.$emit('close');
      }

    }
  }
}
</script>
<template>
  <div class="modal fade" id="paymentMethodModal" aria-hidden="true" aria-labelledby="paymentMethodModalLabel" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-body" style="display: flex; justify-content: space-between">
        <h1 class="modal-title fs-5" id="paymentMethodModalLabel">Add Card</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div id="paymentMethod">
        <div  >
          <div id="CardNumber">
            <label for="CardNumber">Card Number</label>
            <input type="number" class="form-control" placeholder="1234 45678 9012 3456" aria-label="Username"
                   v-model="cardNumber" aria-describedby="basic-addon1">
          </div>
          <div style="display: flex; flex-direction: row; margin-top: 1rem" >
            <div id="CardHolder" style="flex: 2; margin-left: 0.25rem">
              <label for="CardHolder">Card Holder Name:</label>
              <input type="text" class="form-control" placeholder="Elon Musk" aria-label="Username"
                     v-model="holder" aria-describedby="basic-addon1">
            </div>
            <div id="ExpirationDate" style="flex:1; margin-left: 0.25rem;">
              <label for="ExpirationDate">Exp. Date</label>
              <input type="text" class="form-control" placeholder="01/23" aria-label="Username"
                  v-model="expirationDate"   aria-describedby="basic-addon1">
            </div>
            <div id="CVC" style="flex: 1; margin-left: 0.25rem;">
              <label for="CVC">CVC</label>
              <input type="password" class="form-control" placeholder="123" aria-label="Username"
                     aria-describedby="basic-addon1">
            </div>
          </div>
          <div style="display: flex; justify-content: flex-end; margin-top: 1rem">
            <button type="button" class="btn btn-primary" data-bs-dismiss="modal"  @click="addCard">Add Card</button>
          </div>
        </div>
      </div>
      </div>
    </div>
  </div>
</div>
  <div data-bs-target="#paymentMethodModal" data-bs-toggle="modal" class="addPayment" style="display: flex; justify-content: center; flex-direction: column; align-items: center;">
    <div style="font-size: 2rem"><i class="bi bi-plus-circle"></i></div>
    <div href="#" >Add Payment Method</div>
</div>


</template>

<style scoped>
.modal-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1050;
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