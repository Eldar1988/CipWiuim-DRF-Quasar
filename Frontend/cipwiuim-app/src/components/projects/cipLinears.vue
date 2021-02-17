<template>
  <div>
    <div class="liners">
      <q-linear-progress
        size="50px"
        :value="progress2"
        color="accent"
        class="q-mt-sm"
      >
        <div class="absolute-full flex flex-center">
          <q-badge color="white" text-color="accent" :label="progressLabel2"/>
        </div>
      </q-linear-progress>
    </div>
  </div>
</template>

<script>
export default {
  name: "cipLinears",
  props: {
    indicators: {
      type: Object,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
