<script>
import { SearchAccessQuery } from '@/Objects.js'

export default {
  name: 'SearchSideBar',
  data() {
    return {
      company: '',
      price: '',
      name: '',
      accessType: ''
    }
  },
  methods: {
    search() {

      const searchQuery = new SearchAccessQuery(this.name, this.accessType, this.company, this.price);

      this.$emit('searchQuery', searchQuery);
    }
  }

}
</script>

<template>
  <nav class="navbar  sticky-bottom " >
    <div class="nav-container container-fluid">

      <div>
        <div style="margin-left: 0.5rem">Search By Company</div>
        <input type="text" placeholder="RTC" class="search-input" v-model="company">
      </div>
      <div>
        <div style="margin-left: 0.5rem">Search By Price</div>
        <input type="number" placeholder="5.00" class="search-input" v-model="price">
      </div>
      <div>
        <div style="margin-left: 0.5rem">Search By Access Name</div>
        <input type="text" placeholder="Access Weekend" class="search-input" v-model="name">
      </div>
      <div>
        <div style="margin-left: 0.5rem">Search By Access Type</div>
        <select v-model="accessType">
          <option value="Ticket">Ticket</option>
          <option value="Subscription">Subscription</option>
        </select>
      </div>
        <button @click="search">Search</button>

    </div>
  </nav>
</template>

<style scoped>
input {
  padding: 0.5rem;
  margin: 0.5rem;
  border-radius: 1rem;
  border: none;
}

select {
  padding: 0.5rem;
  margin: 0.5rem;
  border-radius: 1rem;
  border: none;
}

button {
  width: 100%;
  padding: 0.5rem;
  margin: 0.5rem;
  border-radius: 1rem;
  border: none;
  background-color: #01356a;
  transition: ease-in-out 0.25s;
  color: white;
}

button:hover {
  cursor: pointer;
  background-color: #0368cc;
  transition: ease-in-out 0.25s;
}

.nav-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  background-color: #f1f1f1;
  padding: 1rem;
  border-radius: 20px;
}


</style>