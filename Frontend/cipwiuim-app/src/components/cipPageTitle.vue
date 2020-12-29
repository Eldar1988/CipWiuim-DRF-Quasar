<template>
<div class="page-title-wrapper">
  <h1 class="page-title">{{ title }}</h1>
</div>
</template>

<script>
export default {
name: "cipPageTitle",
  props: {
  title: {
    type: String,
    default: 'Page Header'
  }
  }
}
</script>

<style scoped>

</style>
