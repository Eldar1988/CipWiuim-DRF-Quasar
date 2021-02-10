<template>
  <div class="q-mt-lg">
    <splide :options="options" :slides="projects">
      <splide-slide v-for="project in projects" :key="project.id">
        <cip-project-card :project="project" />
      </splide-slide>
    </splide>


  </div>
</template>

<script>
import {Splide, SplideSlide} from '../../../node_modules/@splidejs/vue-splide'
import '../../../node_modules/@splidejs/splide/dist/css/themes/splide-sea-green.min.css'
import CipProjectCard from "components/projects/cipProjectCard"

export default {
  name: "cipProjectsListScrollX",
  components: {
    CipProjectCard,
    Splide,
    SplideSlide,
  },
  data() {
    return {
      options: {
        type: 'slide',
        autoplay: true,
        interval: 5000,
        perPage: 4,
        arrows: true,
        pagination: true,
        perMove: 1,
        gap: 10,
        lazyLoad: false,
        breakpoints: {
          1440: {
            perPage: 3,
          },
          1100: {
            type: 'loop',
            perPage: 2,
            arrows: false,
            autoplay: false,
          },
          650: {
            type: 'loop',
            perPage: 1.2,
            perMove: 1,
            arrows: false,
            autoplay: false,
          }
        }
      }
    }
  },
  computed: {
    projects() {
      return this.$store.getters.getMainData.projects
    }
  }
}
</script>

<style scoped>

</style>
