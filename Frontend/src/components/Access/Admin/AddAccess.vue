<script>
import { addAccess } from '@/api/access.js'
import { Modal } from 'bootstrap'

export default {
  name: 'AddAccess',
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
      modal_demo: null
    }
  },
  methods: {
    // Open the modal
    openModal() {
      this.modal_demo.show()
    },
    // Close the modal
    closeModal() {
      this.modal_demo.toggle()
      this.$emit('close')
    },
    async addAccess() {
      const access = {
        accessName: this.accessName,
        price: parseInt(this.price),
        accessType: this.accessType,
        duration: parseInt(this.duration),
        company: this.adminCompany
      }
      // If the access type is a ticket, add the number of passages
      if (this.accessType === 'ticket') {
        access.numberOfPassage = parseInt(this.numberOfPassage)
      }
     // Add the access and if successful, clear the form and close the modal
      const res = await addAccess(access)
      if (res.status === 201) {
          this.accessName = '',
          this.price = null,
          this.accessType = '',
          this.duration = null,
          this.numberOfPassage = null,
          this.closeModal()
      } else {
        console.error('Error Adding Access')
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
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-body" style="display: flex; justify-content: space-between">
          <h1 class="modal-title fs-5" id="paymentMethodModalLabel">Add Access</h1>
          <button type="button" class="btn-close" @click="closeModal"></button>
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
                     v-model="duration" aria-describedby="basic-addon1">
            </div>
            <div id="AccessType" style="flex:1;">
              <label for="ExpirationDate">Access Type</label>
              <select class="form-control" v-model="accessType">
                <option value="ticket">Ticket</option>
                <option value="subscription">Subscription</option>
              </select>
            </div>
            <div v-if="accessType === 'ticket'" id="Passages" style="flex: 1;">
              <label for="Duration">Number Of Trips:</label>
              <input type="number" class="form-control" placeholder="" aria-label="Username"
                     v-model="numberOfPassage" aria-describedby="basic-addon1">
            </div>
            <div id="errorAddAccess" style="font-size: small; color: red"></div>
            <div style="display: flex; margin-top: 1rem;">
              <button type="button" class="btn btn-primary btn-block" style="width: 100%;"
                      @click="addAccess">Add Access
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    style="display: flex; width: 100%; flex-direction: column; align-items: center;">
    <div href="#" class="add-access" style="width: 100%" @click="openModal">+ Add Access</div>
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