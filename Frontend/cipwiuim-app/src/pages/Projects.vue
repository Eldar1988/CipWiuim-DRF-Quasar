<template>
<q-page>
  <cip-bread-cumps current-page-title="Проекты" />
  <cip-page-title title="Проекты"/>
  <div class="q-mt-md">
    <div v-html="homeData.projects_description"></div>
  </div>
  <cip-projects-grid :projects="projects" />
</q-page>
</template>

<script>
import CipPageTitle from "components/cipPageTitle";
import CipBreadCumps from "components/service/cipBreadCumps";
import CipProjectsGrid from "components/projects/cipProjectsGrid";
export default {
name: "Projects",
  components: {CipProjectsGrid, CipBreadCumps, CipPageTitle},
  computed: {
    projects() {
      return this.$store.getters.getProjects
    },
    homeData () {
      return this.$store.getters.getMainData.homeMeta
    }
  },
  preFetch({store}) {
    return store.dispatch('fetchProjects')
  }
}
</script>

<style scoped>

</style>
