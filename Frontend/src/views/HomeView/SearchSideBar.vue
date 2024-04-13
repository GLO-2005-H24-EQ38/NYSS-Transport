<script>
export default {
  name: "SearchSideBar"
}
</script>

<template>
    <div class="search-bar" style="display: flex; justify-content: center; align-items: center">
      <div class="search-container">
        <div style="font-size: 1.5rem; margin-bottom: 2rem;"><strong>Looking for a specific access ?</strong></div>
        <div>
          <div style="margin-left: 0.5rem">Search By Company</div>
          <input type="text" placeholder="RTC" class="search-input">
        </div>
        <div>
          <div style="margin-left: 0.5rem">Search By Price</div>
          <input type="number" placeholder="5.00" class="search-input">
        </div>
        <div>
          <div style="margin-left: 0.5rem">Search By Access Name</div>
          <input type="text" placeholder="Access Weekend" class="search-input">
        </div>
        <div>
          <div style="margin-left: 0.5rem">Search By Access Type</div>
          <select>
            <option value="Ticket">Ticket</option>
            <option value="Subscription">Subscription</option>
          </select>
        </div>
        <div style="width: 100%; display: flex; justify-content: center">
          <button class="search-button">Search</button>
        </div>
      </div>
    </div>
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
  color: white;
}

.search-container {
  padding: 1rem;
  border-radius: 0.5rem;
  display: flex;
  justify-content: center;
  flex-direction: column;
  margin: 1rem;
}
</style>