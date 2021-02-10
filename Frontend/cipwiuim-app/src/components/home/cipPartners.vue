<template>
  <section class="cip-partners section">
    <div class="heading text-center">
      <h3 class="section-title">
        Наши партнеры
      </h3>
    </div>
    <div class="partners-logo-grid q-mt-md">
        <splide :options="options" :slides="partners">
          <splide-slide v-for="partner in partners" :key="partner.id">
            <div class="text-center">
              <img
                :src="partner.logo"
                height="75px"
                style="object-fit: contain"
              />
            </div>
          </splide-slide>
        </splide>
    </div>
  </section>
</template>

<script>
import {Splide, SplideSlide} from '../../../node_modules/@splidejs/vue-splide'
import '../../../node_modules/@splidejs/splide/dist/css/themes/splide-sea-green.min.css'

export default {
  name: "cipPartners",
  components: {
    Splide,
    SplideSlide,
  },
  computed: {
    partners() {
      return this.$store.getters.getMainData.partners
    }
  },
  data() {
    return {
      options: {
        type: 'loop',
        autoplay: true,
        interval: 2000,
        perPage: 5,
        arrows: false,
        pagination: false,
        perMove: 1,
        gap: 10,
        breakpoints: {
          1100: {
            type: 'loop',
            perPage: 3,
            arrows: false,
          },
          650: {
            type: 'loop',
            perPage: 2,
            arrows: false,
            perMove: 1,
          }
        }
      }
    }
  }
}
</script>

<style lang="sass">

</style>
