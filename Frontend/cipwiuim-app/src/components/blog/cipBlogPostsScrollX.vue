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
      ref="scrollPosts"
      horizontal
      class="full-width q-mt-md"
      style="height: 450px; width: 100%"
      :thumb-style="{ display: 'none' }"
    >
      <div class="row no-wrap">
        <div
          v-for="post in posts"
          :key="post.id"
          class="product-wrapper"
          style="width: 325px; padding: 0 4px"
        >
          <cip-post-card :post="post" />
        </div>
      </div>
    </q-scroll-area>
    <!--    ============   -->
  </div>
</template>

<script>
import CipPostCard from "components/blog/cipPostCard";
export default {
  name: "cipBlogPostsScrollX",
  components: {CipPostCard},
  data() {
    return {
      position: 0,
      posts: []
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
    },
    // Скролл вправо
    scrollRight() {
      // Проверка: количество карточек * ширину экрана (98% ширина контейнера)
      if(this.position < this.posts.length * 320 - (window.innerWidth * 0.98)) {
        this.position += 325
        this.$refs.scrollPosts.setScrollPosition(this.position, 500)
      }
    },
    // Левый скролл
    scrollLeft() {
      if (this.position !== 0) {
        this.position = this.position - 325
        this.$refs.scrollPosts.setScrollPosition(this.position, 500)
      }
    }
  }
}
</script>

<style scoped>

</style>
