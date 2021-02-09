<template>
  <section class="section">
    <div class="projects-wrapper">
      <div class="heading text-center">
        <h3 class="section-title">
          {{ title }}
        </h3>
      </div>
      <cip-testimonials-cards :testimonials="testimonials" class="q-mt-lg" />
    </div>
  </section>
</template>

<script>
import CipTestimonialsCards from "components/home/cipTestimonialsCards";
export default {
name: "cipTestimonialsBlock",
  components: {CipTestimonialsCards},
  props: {
    title: {
      type: String,
      default: 'Отзывы'
    }
  },
  computed: {
    testimonials() {
      return this.$store.getters.getMainData.testimonials
    }
  }
}
</script>

<style scoped>

</style>
