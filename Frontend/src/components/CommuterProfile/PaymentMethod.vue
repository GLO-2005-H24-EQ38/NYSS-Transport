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
  <div id="paymentMethod" style="display: flex; justify-content: center; align-items: center; flex-direction: column">
    <div>No Payment Methods Found</div>
    <a href="#" @click="showPaymentMethodForm">Add Here</a>
    <PaymentMethodForm v-if="showForm" />
  </div>
</template>

<style scoped>
#paymentMethod {
  background-color: #f1f1f1;
  padding: 1rem;
  margin: 0.5rem;
  border-radius: 20px;
}
</style>