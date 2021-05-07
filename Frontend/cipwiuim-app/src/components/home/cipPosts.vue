<template>
  <section class="section">
    <div class="projects-wrapper">
      <div class="heading text-center">
        <h3 class="section-title">
          Информационный блог
        </h3>
        <div class="q-mt-md">
          <div v-html="homeData.blog_description"></div>
        </div>
      </div>
      <cip-blog-posts-scroll-x />
    </div>
  </section>
</template>

<script>
import CipBlogPostsScrollX from "components/blog/cipBlogPostsScrollX";
export default {
name: "cipPosts",
  components: {CipBlogPostsScrollX},
  computed: {
    homeData () {
      return this.$store.getters.getMainData.homeMeta
    }
  }
}
</script>

<style scoped>

</style>
