<template>
  <section class="section">
    <div class="projects-wrapper">
      <div class="heading text-center">
        <h3 class="section-title">
          Проекты
        </h3>
        <div class="q-mt-md">
          <div v-html="homeData.projects_description"></div>
        </div>
      </div>
      <cip-projects-list-scroll-x />
    </div>
  </section>
</template>

<script>
import CipProjectsListScrollX from "components/projects/cipProjectsListScrollX";
export default {
name: "cipProjects",
  components: {CipProjectsListScrollX},
  computed: {
    homeData () {
      return this.$store.getters.getMainData.homeMeta
    }
  }
}
</script>

<style scoped>

</style>
