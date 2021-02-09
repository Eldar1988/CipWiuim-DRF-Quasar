<template>
  <div class="testimonials">
    <q-carousel
      v-model="slide"
      transition-prev="scale"
      transition-next="scale"
      swipeable
      animated
      navigation-position="top"
      infinite
      control-color="white"
      navigation-icon="radio_button_unchecked"
      navigation
      padding
      height="auto"
      :autoplay="true"
      class="bg-gradient-1 text-white my-shadow rounded "
    >
      <q-carousel-slide
        v-for="(testimonial, index) in testimonials"
        :key="index"
        :name="index"
        class="text-center no-padding"
      >
        <div class="testimonial-text q-py-lg q-px-sm">
          <p class="text-h6 q-pt-xl">{{ testimonial.name }} </p>
          <p class="q-pt-md">{{ testimonial.text }}</p>
          <p class="q-pt-lg text-grey-3 text-bold">{{ testimonial.position }}</p>
        </div>
      </q-carousel-slide>
    </q-carousel>
  </div>
</template>

<script>
export default {
  name: "cipTestimonialsCards",
  props: {
    testimonials: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      slide: 0
    }
  },
}
</script>

<style lang="sass">
.testimonial-text
  width: 1000px
  max-width: 100%
  margin: auto
</style>
