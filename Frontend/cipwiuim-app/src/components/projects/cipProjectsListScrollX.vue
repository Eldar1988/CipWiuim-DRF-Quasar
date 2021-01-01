<template>
  <div class="q-mt-lg">
    <!--    Scroll controls   -->
    <div class="scroll-controls text-center">
      <q-btn
        @click="scrollLeft"
        icon="navigate_before"
        round
        color="primary"
      />
      <q-btn
        @click="scrollRight"
        icon="navigate_next"
        round
        color="primary"
        class="q-ml-sm"
      />
    </div>
    <!--    ==============   -->
    <!--    Scroll Area   -->
    <q-scroll-area
      ref="scrollFutureProducts"
      horizontal
      class="full-width q-mt-md"
      style="height: 450px; width: 100%"
      :thumb-style="{ display: 'none' }"
    >
      <div class="row no-wrap">
        <div
          v-for="project in projects"
          :key="project.id"
          class="product-wrapper"
          style="width: 325px; padding: 0 4px"
        >
          <cip-project-card :project="project" />
        </div>
      </div>
    </q-scroll-area>
    <!--    ============   -->
  </div>
</template>

<script>
import CipProjectCard from "components/projects/cipProjectCard";
export default {
  name: "cipProjectsListScrollX",
  components: {CipProjectCard},
  data() {
    return {
      position: 0,
    }
  },
  computed: {
    projects() {
      return this.$store.getters.getMainData.projects
    }
  },
  methods: {
    // Скролл вправо
    scrollRight() {
      // Проверка: количество карточек * ширину экрана (98% ширина контейнера)
      if(this.position < this.projects.length * 320 - (window.innerWidth * 0.98)) {
        this.position += 325
        this.$refs.scrollFutureProducts.setScrollPosition(this.position, 500)
      }
    },
    // Левый скролл
    scrollLeft() {
      if (this.position !== 0) {
        this.position = this.position - 325
        this.$refs.scrollFutureProducts.setScrollPosition(this.position, 500)
      }
    }
  }
}
</script>

<style scoped>

</style>
