<template>
  <div>
    <q-carousel
      swipeable
      animated
      v-model="slide"
      navigation
      navigation-position="top"
      infinite
      autoplay
      class="home-slider rounded-borders shadow-5"
    >
        <q-carousel-slide
          v-for="(slide, index) in slides"
          :key="slide.id"
          :name="slide.id"
          :img-src="slide.image"
          class="img-overlay"
        >
          <div class="slider-text">
            <h1
              v-if="index === 0"
              class="slide-title"
            >
              {{ slide.title }}
            </h1>
            <h2
              v-else
              class="slide-title"
            >
              {{ slide.title }}
            </h2>
            <p>{{ slide.text }}</p>
            <q-btn
              :label="slide.button_text"
              color="secondary"
              :to="slide.button_url"
              class="q-px-sm my-shadow bg-gradient-1"
            />
          </div>
        </q-carousel-slide>
    </q-carousel>
  </div>
</template>

<script>
export default {
  name: "cipHomeSlider",
  data() {
    return {
      slide: this.$store.getters.getMainData.slides[0].id
    }
  },
  computed: {
    slides() {
      return this.$store.getters.getMainData.slides
    }
  }
}
</script>

<style lang="sass">
.home-slider
  height: 500px

.slider-text
  position: absolute
  bottom: 20px
  left: 0
  right: 0
  width: 100%
  text-align: center
  z-index: 10
  color: #fff

.slide-title
  font-size: 40px
  font-weight: 700

@media screen and (max-width: 650px)
  .home-slider
    height: 300px

  .slide-title
    font-size: 24px
    font-weight: 700
</style>
