<script>
export default {
  name: "AccessCard",
  data() {
    return {
      added: false,
      quantity: 1
    }
  },
  methods: {
    decrementQuantity() {
      this.quantity = this.quantity - 1;
      if (this.quantity === 0) {
        this.added = false;
        this.quantity = 1;
      }
    },
    incrementQuantity() {
      this.quantity = this.quantity + 1;
    }
  }
}
</script>

<template>
  <div class="restaurant-card">
    <img
        style="object-fit: contain"
        src="@/assets/stm_logo.png"
        alt="stm"/>
    <div class="card-body">
      <div class="single-line card-title">
        2 Passages
      </div>
      <div class="card-text">
            <span
                :style="{
                fontWeight: 'bold',
              }"
            ></span
            >
      </div>
      <div class="card-text">Type: Ticket</div>
    </div>
    <div style="margin: 1rem;">
      <div @click="added = true" v-if="!added" style="width: 100%" class="btn btn-primary btn-lg btn-block">
        <i class="bi bi-plus-lg"></i>
        Add
      </div>
      <div v-if="added" style="width: 100%; display: flex; flex-direction: row">
        <div style="display: flex; flex-direction: row; flex: 3; justify-content: space-evenly; align-items: center">
         <i class="bi bi-dash-lg btn btn-outline-primary" @click="decrementQuantity"></i>
          <div style="font-size: large">{{ quantity }}</div>
          <i class="bi bi-plus-lg btn btn-outline-primary" @click="incrementQuantity"></i>
        </div>
        <div class="btn btn-primary btn-lg btn-block" style="flex: 1">
          Buy
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.restaurant-card {
  transition: ease-in-out 0.25s;
  position: relative;
  width: 23rem;
  height: 100%;
  margin: 20px;
  border-radius: 5px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.restaurant-card img {
  transition: ease-in-out 0.25s;
  width: 100%;
  height: 13rem;
  object-fit: fill;
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

.card-title {
  font-size: 1.25rem;
  font-weight: bold;
  color: #000000;
}

.card-text {
  font-size: 1rem;
  color: #666;
  flex-grow: 1;
}

.addButton {
  cursor: pointer;
  color: dodgerblue;
  display: flex;
  justify-content: center;
  align-items: center;
}

.single-line {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.registerVisitButton {
  transition: ease-in-out 0.25s;
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.2);
  background-color: #ffffff;
  border: none;
  border-radius: 25px;
  padding: 8px;
  position: absolute;
  bottom: 30%;
  left: 50%;
  transform: translate(-50%, 0);
}

.addButton:hover {
  background-color: dodgerblue;
  transition: ease-in-out 0.25s;
  color: white;
  cursor: pointer;
}

.restaurant-card:hover {
  transition: ease-in-out 0.25s;
  cursor: pointer;
  box-shadow: 0 0 6px rgb(0, 82, 158);
}
</style>