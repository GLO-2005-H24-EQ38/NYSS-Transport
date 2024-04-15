<script>
import AccessCard from '@/components/Access/Communter/AccessCard.vue'
import Transaction from '@/components/CommuterProfile/TransactionCard.vue'
import { getTransactions } from '@/api/transactions.js'

export default {
  name: 'TransactionContainer',
  components: { Transaction },
  data() {
    return {
      transactions: []
    }
  },
  methods: {
    async fetchTransactions() {
      this.transactions = await getTransactions()
    }
  },
  mounted() {
    this.fetchTransactions()
  }
}
</script>

<template>
  <div class="transaction-container">
    <Transaction v-for="transaction in this.transactions " :key="transaction.accessNumber"  :transaction="transaction"/>
  </div>

</template>

<style scoped>
.transaction-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin-top: 40px;
}
</style>