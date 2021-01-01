<template>
  <section class="section">
    <div class="projects-wrapper">
      <div class="heading text-center">
        <h3 class="section-title">
          Информационный блог
        </h3>
        <p class="q-mt-md">Не пропустите последние новости, <br>присоединяйтесь к нашему блогу</p>
      </div>
      <cip-blog-posts-scroll-x />
    </div>
  </section>
</template>

<script>
import CipBlogPostsScrollX from "components/blog/cipBlogPostsScrollX";
export default {
name: "cipPosts",
  components: {CipBlogPostsScrollX}
}
</script>

<style scoped>

</style>
