<template>
  <section class="section">
    <div class="projects-wrapper">
      <div class="heading text-center">
        <h3 class="section-title">
          {{ title }}
        </h3>
      </div>
      <cip-testimonials-cards :testimonials="testimonials" />
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
    },
    testimonials: {
      type: Array,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
