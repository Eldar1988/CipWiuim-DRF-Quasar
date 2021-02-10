<template>
<q-page>
  <cip-bread-cumps current-page-title="Проекты" />
  <cip-page-title
    title="Проекты"
    subtitle="Мы открывает новые горизонты для жителей Центрально-азиатского региона. <br>
    Теперь у всех есть возможность стать инвестором в размещаемых проектах."
  />
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
    }
  },
  preFetch({store}) {
    return store.dispatch('fetchProjects')
  }
}
</script>

<style scoped>

</style>
