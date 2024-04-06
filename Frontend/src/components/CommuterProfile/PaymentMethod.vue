<script>
export default {
  name: "paymentMethod"
}
</script>

<template>
  <div id="paymentMethod" class="container-fluid" style="width: 50%">
    <form>
      <div id="CardNumber" style="margin: 0.5rem">
        <label for="CardNumber">Card Number</label>
         <input type="text" class="form-control" placeholder="1234 45678 9012 3456" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <div style="display: flex; flex-direction: row">
        <div id="CardHolder" style="flex: 3; margin: 0.5rem">
        <label for="CardHolder">Card Holder Name:</label>
        <input type="text" class="form-control" placeholder="Elon Musk" aria-label="Username" aria-describedby="basic-addon1">
      </div>
        <div id="ExpirationDate" style="flex:1;  margin: 0.5rem">
        <label for="ExpirationDate">Exp. Date</label>
       <input type="text" class="form-control" placeholder="01/23" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <div id="CVV" style="flex: 1; margin: 0.5rem">
        <label for="CVV">CVV</label>
        <input type="password" class="form-control" placeholder="123" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      </div>
      <div style="display: flex; justify-content: flex-end; margin: 0.5rem">
              <button class="btn btn-primary">Add Card</button>

      </div>
    </form>
  </div>
</template>

<style scoped>
#paymentMethod {
  background-color: #f1f1f1;
  padding: 10px;
  border-radius: 20px;
}
</style>