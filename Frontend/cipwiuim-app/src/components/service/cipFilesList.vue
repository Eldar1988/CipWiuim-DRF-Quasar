<template>
<div>
  <div class="files-list">
    <div
      v-for="file in files"
      :key="file.id"
      class="file rounded-borders q-pa-sm q-mb-md text-primary bg-white"
      style="align-items: center"
    >
      <p class="text-bold">{{ file.title }}</p>
      <div class="flex justify-end q-mt-sm">
      <q-btn
        label="скачать"
        class="bg-gradient-1"
        icon-right="cloud_download"
        unelevated
        text-color="white"
        type="a"
        :href="file.url"
        size="sm"
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
