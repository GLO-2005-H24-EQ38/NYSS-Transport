<script>
import {SearchAccessQuery} from '@/Objects.js'

export default {
  name: 'SearchSideBar',
  data() {
    return {
      company: '',
      price: '',
      name: '',
      accessType: '',
      mobileMode: false,
    }
  },
  methods: {
    search() {

      const searchQuery = new SearchAccessQuery(this.name, this.accessType, this.company, this.price);

      this.$emit('searchQuery', searchQuery);
    },
    isMobile() {
      if (window.innerWidth <= 900) {
        this.mobileMode = true;
      } else {
        this.mobileMode = false;
      }
    },
  },
  mounted() {
    this.isMobile();
    window.addEventListener('resize', this.isMobile);
  },
}
</script>

<template>
  <nav class="navbar  sticky-bottom ">
    <div class="nav-container container-fluid">
      <div v-if="mobileMode" class="btn " type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample"
             style="width: 100%;" :aria-expanded="!mobileMode" aria-controls="collapseExample">
        Swipe Up to Search<i class="bi bi-arrow-up"></i>
      </div>
      <div v-if="mobileMode" class="collapse" id="collapseExample" style="width: 100%">
        <div class="collapse-container container-fluid">
          <div>
            <div style="margin-left: 0.5rem">Search By Company</div>
            <input style="width: 100%" type="text" placeholder="RTC" class="search-input" v-model="company">
          </div>
          <div>
            <div style="margin-left: 0.5rem">Search By Price</div>
            <input style="width: 100%" type="number" placeholder="5.00" class="search-input" v-model="price">
          </div>
          <div>
            <div style="margin-left: 0.5rem">Search By Access Name</div>
            <input style="width: 100%" type="text" placeholder="Access Weekend" class="search-input" v-model="name">
          </div>
          <div>
            <div style="margin-left: 0.5rem">Search By Access Type</div>
            <select style="width: 100%" v-model="accessType">
              <option value="Ticket">Ticket</option>
              <option value="Subscription">Subscription</option>
              <option value="">None</option>
            </select>
          </div>
          <button @click="search">Search</button>
        </div>
      </div>
      <div v-else>
        <div class="d-flex flex-row">
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
              <option value="">None</option>
            </select>
          </div>
        </div>

        <button @click="search">Search</button>
      </div>
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

.sticky-bottom {
  padding-bottom: 0;
}


</style>