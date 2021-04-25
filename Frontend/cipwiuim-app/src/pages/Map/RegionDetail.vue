<template>
  <q-page>
    <cip-bread-cumps :current-page-title="region.title" :pages="[{title: 'Виды деятельности', slug: '/activities'}]"/>
    <cip-page-title :title="region.title"/>
    <cip-ya-map :region="region" :points="points"/>

    <div class="point-titles-grid">
      <div v-for="point in points" :key="point.id" class="q-px-md">
        <router-link :to="`/activities/${region.slug}/${point.slug}`">
          <h2 class="text-subtitle1">{{ point.title }}</h2>
          <small class="text-grey-7">{{ point.type.join(' ') }}</small>
        </router-link>
      </div>
    </div>
  </q-page>
</template>

<script>
import CipBreadCumps from "components/service/cipBreadCumps";
import CipYaMap from "components/maps/cipYaMap";
import CipPageTitle from "components/cipPageTitle";

export default {
  name: "RegionDetail",
  components: {CipPageTitle, CipYaMap, CipBreadCumps},
  methods: {

  },
  computed: {
    region() {
      return this.$store.getters.getRegion
    },
    points() {
      return this.$store.getters.getPoints
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('loadMapPoints', currentRoute.params.slug)
  }
}
</script>

<style lang="sass">
.point-titles-grid
  display: grid
  grid-template-columns: 1fr 1fr
  margin-top: 50px
  grid-gap: 20px

@media screen and (max-width: 800px)
  .point-titles-grid
    grid-template-columns: 1fr
</style>
