<template>
  <div id="map" class="q-mt-xl rounded-borders overflow-hidden shadow-lt">

  </div>
</template>

<script>

import yamaps from "src/utils/yamaps"
export default {
  name: "cipYaMap",
  created() {
    yamaps()
  },
  data() {
    return {

    }
  },
}
</script>

<style lang="sass">
#map
  height: 60vh
  width: 100%
  background: $grey-5
</style>
