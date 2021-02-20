<template>
  <div>
    <div class="benefits-grid q-mt-lg">
      <splide :options="options" :slides="benefits">
        <splide-slide
          v-for="benefit in benefits"
          :key="benefit.id"
        >
          <q-card
            class="benefit-card shadow-0 q-py-lg"
          >
            <q-card-section>
              <q-btn
                :icon="benefit.icon"
                size="lg"
                class="bg-gradient-1 my-shadow"
                text-color="white"
                round unelevated
              />
              <p class="text-bold q-py-md">{{ benefit.title }}</p>
              <q-scroll-area
                :thumb-style="thumbStyle"
                style="height: 150px;"
              >
              <p>{{ benefit.text }}</p>
              </q-scroll-area>
            </q-card-section>
          </q-card>
        </splide-slide>
      </splide>
    </div>
  </div>
</template>

<script>
import {Splide, SplideSlide} from '../../../node_modules/@splidejs/vue-splide'
import '../../../node_modules/@splidejs/splide/dist/css/themes/splide-sea-green.min.css'

export default {
  name: "cipProjectBenefits",
  components: {
    Splide,
    SplideSlide,
  },
  props: {
    benefits: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      thumbStyle: {
        right: '2px',
        borderRadius: '5px',
        backgroundColor: '#027be3',
        width: '0',
        opacity: 0.75
      },
      options: {
        type: 'loop',
        autoplay: true,
        interval: 3000,
        perPage: 4.5,
        arrows: false,
        pagination: false,
        perMove: 1,
        gap: 20,
        lazyLoad: false,
        breakpoints: {
          1440: {
            perPage: 3.5,
          },
          1100: {
            type: 'loop',
            perPage: 2.5,
            autoplay: false
          },
          650: {
            type: 'loop',
            perPage: 1.3,
            perMove: 1,
            arrows: false,
            autoplay: false
          }
        }
      }
    }
  },
}
</script>

<style lang="sass">
.benefit-card
  display: grid
  width: 100%
  align-items: center
  min-height: 100%
</style>
