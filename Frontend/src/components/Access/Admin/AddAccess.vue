<script>
import {addAccess} from "@/api/access.js";

export default {
  name: "AddAccess",
  props: {
    adminCompany: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      accessName: '',
      price: null,
      accessType: '',
      duration: null,
      numberOfPassage: null,
    }
  },
  methods: {
    async addAccess() {
      console.log('Add Access', this.adminCompany);
      const access = {
        accessName: this.accessName,
        price: parseInt(this.price),
        accessType: this.accessType,
        duration: parseInt(this.duration),
        company: this.adminCompany
      }
      if (this.accessType === 'ticket') {
        access.numberOfPassage = parseInt(this.numberOfPassage);
      }
      console.log('Access Object' , access);
      const res = await addAccess(access);
      console.log(res);
    }
  }
}
</script>

<template>
  <div class="modal fade" id="paymentMethodModal" aria-hidden="true" aria-labelledby="paymentMethodModalLabel" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-body" style="display: flex; justify-content: space-between">
        <h1 class="modal-title fs-5" id="paymentMethodModalLabel">Add Access</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div style="margin-left: 0.25rem">
          <div id="AccessName">
            <label for="AccessName">Access Name</label>
            <input type="text" class="form-control" placeholder="" aria-label="AccessName"
                   v-model="accessName" aria-describedby="basic-addon1">
          </div>
            <div id="Price" style="flex: 1;">
              <label for="Price">Access Price:</label>
              <input type="number" class="form-control" placeholder="" aria-label="Username"
                     v-model="price" aria-describedby="basic-addon1">
            </div>
          <div id="Duration" style="flex: 1;">
              <label for="Duration">Duration (days) :</label>
              <input type="number" class="form-control" placeholder="" aria-label="Username"
                  v-model="duration"   aria-describedby="basic-addon1">
            </div>
            <div id="AccessType" style="flex:1;">
              <label for="ExpirationDate">Access Type</label>
              <select  class="form-control" v-model="accessType">
                <option value="ticket">Ticket</option>
                <option value="subscription">Subscription</option>
              </select>
            </div>
          <div v-if="accessType === 'ticket'"  id="Passages" style="flex: 1;">
              <label for="Duration">Number Of Trips:</label>
              <input type="number" class="form-control" placeholder="" aria-label="Username"
                  v-model="numberOfPassage" aria-describedby="basic-addon1">
            </div>

          <div style="display: flex; margin-top: 1rem;">
            <button type="button" class="btn btn-primary btn-block" style="width: 100%;" data-bs-dismiss="modal"  @click="addAccess">Add Access</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
  <div data-bs-target="#paymentMethodModal" data-bs-toggle="modal" style="display: flex; width: 100%; flex-direction: column; align-items: center;">
    <div href="#" class="add-access" style="width: 100%" >+ Add Access</div>
</div>

</template>

<style scoped>
.add-access {
  background-color: #01356a;
  margin-left: 2rem;
  margin-right: 2rem;
  margin-bottom: 0.25rem;
  border-radius: 1rem;
  padding: 1rem;
  color: white;
  transition: ease-in-out 0.25s;

}
.add-access:hover {
  cursor: pointer;
  background-color: #0368cc;
  transition: ease-in-out 0.25s;
}
</style>