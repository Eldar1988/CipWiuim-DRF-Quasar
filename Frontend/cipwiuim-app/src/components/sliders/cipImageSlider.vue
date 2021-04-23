<template>
<div v-if="images && images.length > 0">
  <h2 class="section-title section text-center">Фотогалерея</h2>
  <q-carousel
    animated
    v-model="slide"
    arrows
    navigation
    infinite
    :autoplay="true"
    class="slider-images rounded-borders q-mt-md"
  >
    <q-carousel-slide
      v-for="(image, index) in images"
      :key="index"
      :name="index"
      :img-src="image.url"
    />
  </q-carousel>
</div>
</template>

<script>
export default {
name: "cipImageSlider",
  props: {
    images: {
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
.slider-images
  height: 650px

@media screen and (max-width: 1390px)
  .slider-images
    height: 450px

@media screen and (max-width: 650px)
  .slider-images
    height: 250px
</style>
