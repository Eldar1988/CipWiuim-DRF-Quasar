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

<style lang="sass">
.page-title
  font-size: 40px
  font-weight: 700

@media screen and (max-width: 992px)
  .page-title
    font-size: 30px
</style>
