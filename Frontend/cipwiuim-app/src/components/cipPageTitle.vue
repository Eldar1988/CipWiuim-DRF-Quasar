<template>
  <div class="page-title-wrapper text-center q-mt-xl">
    <h1 class="page-title">{{ title }}</h1>
    <h2 v-if="subtitle" class="page-subtitle q-mt-md" v-html="subtitle"></h2>
  </div>
</template>

<script>
export default {
  name: "cipPageTitle",
  props: {
    title: {
      type: String,
      default: 'Page Header'
    },
    subtitle: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="sass">
.page-title
  font-size: 40px
  font-weight: 700

.page-subtitle
  font-size: 18px
  font-weight: 400

@media screen and (max-width: 992px)
  .page-title
    font-size: 22px

  .page-subtitle
    font-size: 14px
</style>
