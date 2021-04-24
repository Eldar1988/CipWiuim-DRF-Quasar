<template>
<q-page>
  <cip-bread-cumps current-page-title="Виды деятельности"/>
  <cip-page-title title="Выберите регион" />
  <div class="regions-grid">
    <q-card>

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

  },
  methods: {
    async loadRegions() {
      this.regions = await this.$axios.get()
    }
  }
}
</script>

<style scoped>

</style>
