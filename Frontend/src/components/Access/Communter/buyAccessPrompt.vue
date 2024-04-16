<script>
import PaymentMethod from '@/components/CommuterProfile/PaymentMethod.vue'
import { Modal } from 'bootstrap'
import { BuyAccessQuery } from '@/Objects.js'
import { buyAccess } from '@/api/transactions.js'


export default {
  name: 'buyAccessPrompt',
  components: { PaymentMethod },
  props: {
    accessId: {
      required: true
    },
    quantity: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      modal_demo: null,
      cvc: '',
      err: false
    }
  },
  methods: {
    openModal() {
      this.modal_demo.show()
    },
    closeModal() {
      this.cvc =""
      this.modal_demo.toggle()
    },
    // Buy the access and close the modal if successful
    async buyNewAccess() {
      const query = new BuyAccessQuery(this.accessId, this.quantity)
      const result = await buyAccess(this.cvc, query)
      if (result.status === 200 ) {
        this.closeModal()
      } else {
        this.err = true
      }
    }

  },
  beforeUnmount() {

    if (this.modal_demo._isShown){
      this.closeModal()
    }


  },
  mounted() {
      // initialize the modal
      this.modal_demo = new Modal(`#${this.accessId}`, {})
  },
}
</script>

<template>

  <button class="btn addButton btn-block" @click="openModal" style="flex: 1">
    Buy
  </button>

  <div class="modal fade" :id="this.accessId" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Enter CVC</h1>
          <button type="button" class="btn-close" @click="closeModal"  aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div style="display: flex; flex-direction: row">
            <PaymentMethod :buyingAccess="true" />
          <div style="display: flex; justify-content: flex-end; flex:1">
            <div id="CVC" style="width: 50%; display: flex; flex-direction: row; justify-content: flex-end; align-items: center">
            <label for="CVC" style="margin-right: 1rem">CVC</label>
            <input type="password" class="form-control" aria-label="Username"
                   aria-describedby="basic-addon1" v-model="cvc">
          </div>
          </div>
          </div>

          <div v-if="err" class="alert alert-danger" role="alert">
            Invalid CVC
            </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" @click="buyNewAccess">Confirm Purchase</button>
        </div>
      </div>
    </div>
  </div>

</template>

<style scoped>
.addButton {
  cursor: pointer;
  background-color: #01356a;
  border-color: transparent;
  display: flex;
  color: white;
  justify-content: center;
  align-items: center;
  margin: 0.5rem;
}

.addButton:hover {
  background-color: #0368cc;
  transition: ease-in-out 0.25s;
  color: white;
  cursor: pointer;
}
</style>