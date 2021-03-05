<template>
  <div class="head">
    <p>
      <span>Free Go</span>
      <button v-show="isUserConnected">Notifications</button>
    </p>
  </div>
</template>

<script>
export default {
  name: 'Head',
  props: {
    isUserConnected: {
      type: Boolean,
      required: true,
    }
  },
}
</script>

<style scoped>
  a {
    color: #000;
  }
</style>
