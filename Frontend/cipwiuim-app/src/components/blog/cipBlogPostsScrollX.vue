<template>
  <div class="q-mt-lg">
    <splide :options="options" :slides="posts">
      <splide-slide v-for="post in posts" :key="post.id">
        <cip-post-card :post="post" />
      </splide-slide>
    </splide>
  </div>
</template>

<script>
import CipPostCard from "components/blog/cipPostCard"
import {Splide, SplideSlide} from '../../../node_modules/@splidejs/vue-splide'
import '../../../node_modules/@splidejs/splide/dist/css/themes/splide-sea-green.min.css'


export default {
  name: "cipBlogPostsScrollX",
  props: {
    postID: {
      type: Number,
      default: null
    }
  },
  components: {
    CipPostCard,
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
            perPage: 2.2,
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
    posts() {
      return this.$store.getters.getFuturePosts
    }
  },
  created() {
    this.$store.dispatch('fetchFuturePosts')
  }
}
</script>

<style scoped>

</style>
