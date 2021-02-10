<template>
  <div>
    <section>
      <div class="projects-grid q-mt-xl">
        <div
          v-for="project in projects"
          :key="project.id"
        >
          <cip-project-card :project="project"/>
        </div>
      </div>
    </section>
    <section class="q-mt-xl">
      <cip-share image="https://images.squarespace-cdn.com/content/v1/54bfc46be4b0a0e8a51ebbf6/1505746609711-0DBAANDYVV8ZYDUJ1ER3/ke17ZwdGBToddI8pDm48kDgjdZ7qynC0R46hPECFVg17gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1UUv-L9P2ABE5MHo3gunxdFmDWKHz2oEDK1ZKAuTbyHHaEcpqqiibjsYZd52d9hiFyA/tourback.jpg?format=2500w"/>
    </section>
  </div>
</template>

<script>
import CipProjectCard from "components/projects/cipProjectCard";
import CipShare from "components/service/cipShare";

export default {
  name: "cipProjectsGrid",
  components: {CipShare, CipProjectCard},
  props: {
    projects: {
      type: Array,
      default: null
    }
  }
}
</script>

<style lang="sass">
.projects-grid
  display: grid
  grid-template-columns: repeat(4, 1fr)
  @media screen and (max-width: 1440px)
    grid-template-columns: repeat(3, 1fr)
  @media screen and (max-width: 1100px)
    grid-template-columns: repeat(2, 1fr)
  @media screen and (max-width: 650px)
    grid-template-columns: repeat(1, 1fr)
  grid-gap: 20px


</style>
