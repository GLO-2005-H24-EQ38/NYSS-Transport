<script>
import PaymentMethodForm from "@/components/CommuterProfile/PaymentMethodForm.vue";

export default {
  name: "paymentMethod",
  components: {PaymentMethodForm},
  data() {
    return {
      showForm: false,
    }
  },
  methods: {
    showPaymentMethodForm() {
      this.showForm = !this.showForm;
    },
  }
}
</script>

<template>
  <div>
    <div class="PaymentMethod">
      <PaymentMethodForm/>
    </div>
<!--    <div class="PaymentMethod"-->
<!--         style="display: flex; justify-content: flex-start; align-items: start; flex-direction: column">-->
<!--      <div style="display:flex; justify-content:center; align-items: center; font-weight: bold"><i class="fa fa-cc-visa"-->
<!--                                                                                                   style="margin-right:0.5rem; font-size:24px; color:#01356a"></i>Credit-->
<!--        Card ending in ···· 4559-->
<!--      </div>-->
<!--      <div style="display:flex; justify-content:center; align-items: center; font-weight: bold">Exp. Date: 12/24</div>-->
<!--      <div style="width: 100%;display: flex; justify-content: flex-end;">-->
<!--        <button class="btn btn-danger">Remove Card</button>-->
<!--      </div>-->
<!--    </div>-->
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