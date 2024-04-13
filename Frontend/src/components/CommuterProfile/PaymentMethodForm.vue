<script>
export default {
  name: "PaymentMethodForm",
}
</script>
<template>
  <div class="modal fade" id="exampleModalToggle" aria-hidden="true" aria-labelledby="exampleModalToggleLabel" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-body" style="display: flex; justify-content: space-between">
        <h1 class="modal-title fs-5" id="exampleModalToggleLabel">Add Card</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div id="paymentMethod">
        <form>
          <div id="CardNumber">
            <label for="CardNumber">Card Number</label>
            <input type="text" class="form-control" placeholder="1234 45678 9012 3456" aria-label="Username"
                   aria-describedby="basic-addon1">
          </div>
          <div style="display: flex; flex-direction: row; margin-top: 1rem" >
            <div id="CardHolder" style="flex: 2; margin-left: 0.25rem">
              <label for="CardHolder">Card Holder Name:</label>
              <input type="text" class="form-control" placeholder="Elon Musk" aria-label="Username"
                     aria-describedby="basic-addon1">
            </div>
            <div id="ExpirationDate" style="flex:1; margin-left: 0.25rem;">
              <label for="ExpirationDate">Exp. Date</label>
              <input type="text" class="form-control" placeholder="01/23" aria-label="Username"
                     aria-describedby="basic-addon1">
            </div>
            <div id="CVV" style="flex: 1; margin-left: 0.25rem;">
              <label for="CVV">CVV</label>
              <input type="password" class="form-control" placeholder="123" aria-label="Username"
                     aria-describedby="basic-addon1">
            </div>
          </div>
          <div style="display: flex; justify-content: flex-end; margin-top: 1rem">
            <button class="btn btn-primary">Add Card</button>
          </div>
        </form>
      </div>
      </div>
    </div>
  </div>
</div>
  <div data-bs-target="#exampleModalToggle" data-bs-toggle="modal" class="addPayment" style="display: flex; justify-content: center; flex-direction: column; align-items: center;">
    <div style="font-size: 2rem"><i class="bi bi-plus-circle"></i></div>
    <div href="#" >Add Payment Method</div>
</div>

<!--  <div class="modal-background">-->
<!--    <div class="modal-content">-->
<!--      <button class="close-btn">×</button>-->

<!--      <div id="paymentMethod" class="container-fluid">-->
<!--        <form>-->
<!--          <div id="CardNumber" style="margin: 0.5rem">-->
<!--            <label for="CardNumber">Card Number</label>-->
<!--            <input type="text" class="form-control" placeholder="1234 45678 9012 3456" aria-label="Username"-->
<!--                   aria-describedby="basic-addon1">-->
<!--          </div>-->
<!--          <div style="display: flex; flex-direction: row">-->
<!--            <div id="CardHolder" style="flex: 2; margin: 0.5rem">-->
<!--              <label for="CardHolder">Card Holder Name:</label>-->
<!--              <input type="text" class="form-control" placeholder="Elon Musk" aria-label="Username"-->
<!--                     aria-describedby="basic-addon1">-->
<!--            </div>-->
<!--            <div id="ExpirationDate" style="flex:1;  margin: 0.5rem">-->
<!--              <label for="ExpirationDate">Exp. Date</label>-->
<!--              <input type="text" class="form-control" placeholder="01/23" aria-label="Username"-->
<!--                     aria-describedby="basic-addon1">-->
<!--            </div>-->
<!--            <div id="CVV" style="flex: 1; margin: 0.5rem">-->
<!--              <label for="CVV">CVV</label>-->
<!--              <input type="password" class="form-control" placeholder="123" aria-label="Username"-->
<!--                     aria-describedby="basic-addon1">-->
<!--            </div>-->
<!--          </div>-->
<!--          <div style="display: flex; justify-content: flex-end; margin: 0.5rem">-->
<!--            <button class="btn btn-primary">Add Card</button>-->

<!--          </div>-->
<!--        </form>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
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