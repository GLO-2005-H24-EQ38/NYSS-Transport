<script>
import PaymentMethod from '@/components/CommuterProfile/PaymentMethod.vue'
import { Modal } from 'bootstrap'
import { BuyAccessQuery } from '@/Objects.js'
import { buyAccess } from '@/api/access.js'


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
      this.modal_demo.toggle()
      this.$emit('close')
    }
    ,async buyNewAccess() {
      console.log('Buying access')

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
    this.modal_demo = new Modal('#exampleModal', {})
  }
}
</script>

<template>

  <button class="btn btn-primary btn-lg btn-block" @click="openModal" style="flex: 1">
    Buy
  </button>

  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Enter CVC</h1>
          <button type="button" class="btn-close" @click="closeModal"  aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <PaymentMethod :buyingAccess="true" />

          <div id="CVC" style="flex: 1; margin-left: 0.25rem;">
            <label for="CVC">CVC</label>
            <input type="password" class="form-control" placeholder="example: 123" aria-label="Username"
                   aria-describedby="basic-addon1" v-model="cvc">
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

</style>