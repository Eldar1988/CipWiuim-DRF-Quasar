<template>
  <div id="map" class="q-mt-xl rounded-borders overflow-hidden shadow-lt">
  </div>
</template>

<script>

import yamaps from "src/utils/yamaps"
export default {
  name: "cipYaMap",
  props: {
    region: {
      type: Object,
      default: null
    },
    points: {
      type: Array,
      default: null
    },
    zoom: {
      type: Number,
      default: 7
    }
  },
  mounted() {
    yamaps(this.region, this.points, this.zoom)
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

@media screen and (max-width: 650px)
  #map
    height: 40vh
</style>
