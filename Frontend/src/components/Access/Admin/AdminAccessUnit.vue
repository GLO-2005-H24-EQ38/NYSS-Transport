<script>

import QRCodeTicket from '@/components/CommuterProfile/QRCodeTicket.vue'
import { deleteAccess } from '@/api/access.js'

export default {
  name: 'AdminAccessUnit',
  components: { QRCodeTicket },
  props: {
    access: {
      type: Object,
      required: true
    },
    showOutOfSale: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    async deleteAccess() {
      const res = await deleteAccess(this.access.accessId)
      this.$emit("deleteAccess")
      console.log(res.status)
    }
  },
  data() {
    return {}
  }
}
</script>

<template>

  <div class="access-card" v-if="access.outOfSale === showOutOfSale"  style="position: relative">
    <div class="expirationDate" style="display: flex; justify-content: center; align-items: end; flex-direction: column">
      <div >
        {{ this.access.accessType }}

      </div>
      <div v-if="showOutOfSale">
        Deletion Date: {{ this.access.deletionDate }}
      </div>
    </div>
    <div class="card-body">
      <div class="card-title" style="display: flex; flex-direction: column">
        <div style="width: 50%">
          Access Name
        </div>
        <div style="flex: 1; font-size: 1.70rem; color: black">
          {{ this.access.accessName }}
        </div>
      </div>
      <div style="display: flex; flex-direction: row">
        <div class="card-text" style="justify-content: flex-start; display: flex; font-size: 1.5rem; color: darkgray">
          {{ this.access.duration }} {{ 'days' }}
        </div>
      </div>
      <hr>
      <div class="card-text"
           style="justify-content: flex-end; display: flex; font-size: 1.5rem; font-weight: bold; color: black; margin-bottom: 1rem">
        Price: {{ this.access.price }}$
      </div>
    </div>
    <div style="width: 100%; display: flex;">
      <button class="btn btn-danger" v-if="this.access.outOfSale === false" style="width: 100%; height: 3rem"
              @click="deleteAccess">Delete Access
      </button>
    </div>

  </div>
</template>

<style scoped>
.access-card {
  transition: ease-in-out 0.25s;
  position: relative;
  width: 23rem;
  height: 100%;
  margin: 20px;
  border-radius: 5px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.access-card img {
  transition: ease-in-out 0.25s;
  width: 20%;
  object-fit: contain;
}

.card-body {
  position: relative;
  padding-top: 20px;
  padding-left: 10px;
  padding-right: 10px;
  margin: 0;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;

}

.expirationDate {
  padding: 1px;
  border: none;
  position: absolute;
  top: 3%;
  border-top-right-radius: 0.5rem;
  right: 5%;
  font-size: small;
  color: darkgray;
  font-weight: bold;
}

.expirationDate2 {
  padding: 1px;
  border: none;
  position: absolute;
  top: 3%;
  border-top-right-radius: 0.5rem;
  right: 3%;
  color: forestgreen;
  font-size: small;
  font-weight: bold;
}

.invalid {
  border: none;
  position: absolute;
  top: 60%;
  background-color: darkred;
  padding: 0.5rem 1rem;
  right: 5%;
  color: white;
  font-size: small;
  font-weight: bold;
}

.logoPosition {
  padding: 1px;
  border: none;
  position: absolute;
  top: 60%;
  border-top-right-radius: 0.5rem;
  left: 5%;
}

.card-title {
  font-size: 1rem;
  color: darkgray;
}

.card-text {
  font-size: 1rem;
  color: darkgray;
}

.access-card:hover {
  transition: ease-in-out 0.25s;
  cursor: pointer;
  box-shadow: 0 0 6px rgb(104, 104, 104);
}
</style>