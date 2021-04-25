<template>
  <q-page>
    <cip-bread-cumps current-page-title="Виды деятельности"/>
    <cip-page-title title="Выберите регион"/>
    <div class="regions-grid">

      <q-card
        v-for="region in regions"
        :key="region.id"
        class="shadow-lt bg-gradient-1 text-center"
        dark
      >
        <router-link :to="`/activities/${region.slug}`">
          <q-card-section>
            <h2 class="text-subtitle2 text-white">{{ region.title }}</h2>
            <p class="absolute-top-right q-pr-sm q-pt-xs text-white">{{ region.points.length }}</p>
          </q-card-section>
        </router-link>

      </q-card>
    </div>
  </q-page>
</template>

<script>
import CipPageTitle from "components/cipPageTitle";
import CipBreadCumps from "components/service/cipBreadCumps";

export default {
  name: "Activities",
  components: {CipBreadCumps, CipPageTitle},
  data() {
    return {
      regions: []
    }
  },
  created() {
    this.loadRegions()
  },
  methods: {
    async loadRegions() {
      this.regions = await this.$axios.get(`${this.$store.getters.getServerURL}/map/regions/`)
        .then(({data}) => data)
    }
  }
}
</script>

<style lang="sass">
.regions-grid
  display: grid
  grid-template-columns: repeat(3, 1fr)
  grid-gap: 15px
  margin-top: 50px

@media screen and (max-width: 800px)
  .regions-grid
    grid-template-columns: repeat(2, 1fr)

@media screen and (max-width: 800px)
  .regions-grid
    grid-template-columns: repeat(1, 1fr)
</style>
