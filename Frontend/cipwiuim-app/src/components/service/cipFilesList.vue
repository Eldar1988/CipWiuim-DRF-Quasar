<template>
<div>
  <div class="files-list">
    <div
      v-for="file in files"
      :key="file.id"
      class="file rounded-borders q-pa-sm q-mt-md text-primary flex justify-between bg-white"
      style="align-items: center"
    >
      <p>{{ file.title }}</p>
      <div class="text-right">
      <q-btn
        label="скачать"
        class="bg-gradient-1"
        icon-right="cloud_download"
        unelevated
        text-color="white"
        type="a"
        :href="file.url"
        target="_blank"
      />
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "cipFilesList",
  props: {
    files: {
      type: Array,
      default: null
    }
  }
}
</script>

<style lang="sass">
.file
  border: 1px solid $grey-3
</style>
