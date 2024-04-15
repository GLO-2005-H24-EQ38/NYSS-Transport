<script>
import QrcodeVue from 'qrcode.vue'
import { Modal } from 'bootstrap'

export default {
  name: 'QRCodeTicket',
  components: { QrcodeVue },
  props: {
    QRValue: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      qr_modal: null
    }
  },methods: {
    openModal() {
      this.qr_modal.show()
    },
    closeModal() {

      this.qr_modal.toggle()
    }
  },
  mounted() {
    this.qr_modal = new Modal('#qrCodeTicket', {})
  },
  beforeUnmount() {
    console.log(this.qr_modal._isShown)
    if (this.qr_modal._isShown) {
      this.closeModal()
      console.log(this.qr_modal._isShown)
    }
  }

}
</script>

<template>
  <div class="modal fade" id="qrCodeTicket" aria-hidden="true" aria-labelledby="asasa" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered" style="display: flex; justify-content: center; align-items: center">
      <div class="modal-content">
        <div class="modal-body" style="border-style: solid; border-width: thin; border-color: darkgray">
          <div
            style="display: flex; justify-content: center; align-items: center;flex-direction: column;">
            <div style="width: 100%;">
              <div style="display: flex; justify-content: center"><strong style="font-size: 1.5rem">Your Ticket
              </strong></div>

              <hr>

              <div id="details">
                <div class="qrCode" style="position: relative; display: flex; justify-content: center">
                  <qrcode-vue background="#ffffff" :value="QRValue" size="200" level="Q"></qrcode-vue>
                  <img
                    class="qrcode__image"
                    src="@/assets/qrlogo.png"
                    alt="nyss"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="btn btn-secondary" style="display: flex; justify-content: center; align-items: center; height: 3.25rem"
       href="#"
        @click="openModal">Show QR Code
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

.qrCode .qrcode__image {
  border-radius: 5rem;
  border-color: white;
  height: 30%;
  left: 50%;
  overflow: hidden;
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  width: auto;
  border-width: thick;
  border-style: solid;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  width: auto;
}

.modal-body {
  border-color: black;
  bor: medium;
}

#details {
  border-radius: 0.5rem;
  border-color: darkgray;
}

.btn-secondary {
  background-color: #01356a;
  color: white;
}

.btn-secondary:hover {
  background-color: #0368cc;
  color: white;
}
</style>