<template>
  <q-breadcrumbs>
    <q-breadcrumbs-el icon="home" to="/" />
    <q-breadcrumbs-el
      v-for="(page, index) in pages"
      :key="index"
      :label="page.title"
      :to="page.slug"
    />
    <q-breadcrumbs-el :label="currentPageTitle" />
  </q-breadcrumbs>
</template>

<script>
export default {
  name: "cipBreadCumps",
  props: {
    currentPageTitle: {
      type: String,
      default: ''
    },
    pages: {
      type: Array,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
