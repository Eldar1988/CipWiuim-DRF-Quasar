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
  components: {
    CipPostCard,
    Splide,
    SplideSlide,
  },
  data() {
    return {
      position: 0,
      posts: [],
      options: {
        type: 'slide',
        autoplay: false,
        interval: 2000,
        perPage: 3,
        arrows: true,
        pagination: true,
        perMove: 1,
        gap: 10,
        lazyLoad: false,
        breakpoints: {
          1100: {
            type: 'loop',
            perPage: 2.7,
            arrows: false,
          },
          650: {
            type: 'loop',
            perPage: 1.5,
            arrows: false,
            perMove: 1,
          }
        }
      }
    }
  },
  mounted() {
    this.loadPosts()
  },
  methods: {
    async loadPosts() {
      this.posts = await this.$axios.get(`${this.$store.getters.getServerURL}/blog/get_future_posts`)
      .then(({ data }) => {
        return data
      })
    }
  }
}
</script>

<style scoped>

</style>
