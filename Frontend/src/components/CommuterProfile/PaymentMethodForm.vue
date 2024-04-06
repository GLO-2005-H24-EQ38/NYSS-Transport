<script>
export default {
  name: "PaymentMethodForm",
}
</script>

<template>
  <div class="modal-background">
    <div class="modal-content">
      <div id="paymentMethod" class="container-fluid">
        <form>
          <div id="CardNumber" style="margin: 0.5rem">
            <label for="CardNumber">Card Number</label>
            <input type="text" class="form-control" placeholder="1234 45678 9012 3456" aria-label="Username"
                   aria-describedby="basic-addon1">
          </div>
          <div style="display: flex; flex-direction: row">
            <div id="CardHolder" style="flex: 2; margin: 0.5rem">
              <label for="CardHolder">Card Holder Name:</label>
              <input type="text" class="form-control" placeholder="Elon Musk" aria-label="Username"
                     aria-describedby="basic-addon1">
            </div>
            <div id="ExpirationDate" style="flex:1;  margin: 0.5rem">
              <label for="ExpirationDate">Exp. Date</label>
              <input type="text" class="form-control" placeholder="01/23" aria-label="Username"
                     aria-describedby="basic-addon1">
            </div>
            <div id="CVV" style="flex: 1; margin: 0.5rem">
              <label for="CVV">CVV</label>
              <input type="password" class="form-control" placeholder="123" aria-label="Username"
                     aria-describedby="basic-addon1">
            </div>
          </div>
          <div style="display: flex; justify-content: flex-end; margin: 0.5rem">
            <button class="btn btn-primary">Add Card</button>

          </div>
        </form>
      </div>
    </div>
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
  width: auto;
}
</style>