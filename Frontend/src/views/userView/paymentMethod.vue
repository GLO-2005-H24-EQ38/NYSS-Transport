<script>
export default {
  name: "paymentMethod"
}
</script>

<template>
  <div id="paymentMethod" class="container-fluid">
    <form>
      <div id="CardNumber">
        <label for="CardNumber">Card Number</label>
         <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <div id="ExpirationDate">
        <label for="ExpirationDate">Expiration Date</label>
       <input type="text" class="form-control" placeholder="CardHolder" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <div id="CardHolder">
        <label for="CardHolder">Card Holder</label>
        <input type="text" class="form-control" placeholder="CardHolder" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <div id="CVV">
        <label for="CVV">CVV</label>
        <input type="text" class="form-control" placeholder="CVV" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <button>Submit</button>
    </form>
  </div>
</template>

<style scoped>

</style>