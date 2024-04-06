<script>
export default {
  name: "AccessManager"
}
</script>

<template>
  <div id="add-modify-delete-access" style="display: flex; justify-content: center; flex-direction: row">
    <div id="add-access" style="flex: 1; margin: 0.5rem;">
      <button style="width: 100%; height: 20vh; font-size: 1.5rem" class="button add"> <i class="bi bi-plus-lg"></i>
Add Access</button>
    </div>
    <div id="modify-access" style="flex: 1; margin: 0.5rem">
      <button style="width: 100%; height: 20vh; font-size: 1.5rem" class="button modify"><i class="bi bi-gear-fill"></i>
Modify Access</button>
    </div>
    <div id="delete-access" style="flex: 1; margin: 0.5rem">
      <button style="width: 100%; height: 20vh; font-size: 1.5rem" class="button delete"><i class="bi bi-trash3-fill"></i>
Delete Access</button>
    </div>
  </div>
</template>

<style scoped>

button:hover {
  transition: ease-in-out 0.25s;
  background-color: #0368cc;
  color: white;
}

button {
  transition: ease-in-out 0.25s;
  border: none;
  outline: none;
  border-radius: 2rem;
}

.add {
  background-color: #01356a;
  color: white;
}

.modify {
  background-color: #01356a;
  color: white;
  border: none;
  outline: none;
  border-radius: 2rem;
}

.delete {
  background-color: #01356a;
  color: white;
  border: none;
  outline: none;
  border-radius: 2rem;
}
</style>