<template>
  <q-page>
    <cip-bread-cumps :current-page-title="post.title" :pages="[{title: 'Блог', slug: '/blog'}]"/>
    <!--    Post   -->
    <article>
      <section class="q-mt-md">
        <cip-post-image :post="post"/>
        <div class="post-meta q-mt-sm">
          <span><q-icon name="event" class="q-mr-sm"/>{{ post.pub_date.split('-')[0] }}</span>
          <span class="q-ml-md"><q-icon name="visibility" class="q-mr-sm"/>{{ post.views }}</span>
          <span class="q-ml-md"><q-icon name="chat_bubble_outline" class="q-mr-sm"/>{{ post.comments.length }}</span>
        </div>
      </section>
      <section>
        <p class="text-bold q-mt-lg">{{ post.description }}</p>
        <div class="bg-white q-mt-lg q-pa-md rounded-borders">
          <div v-html="post.body"></div>
        </div>
      </section>
    </article>
    <!--    /// Post   -->
<!--    Future posts   -->
    <section class="section">
      <h2 class="section-title">Читайте также</h2>
      <cip-blog-posts-scroll-x :postID="post.id" />
    </section>
<!--    /// Future posts   -->
    <!--    Comments   -->
    <section class="section">
      <h2 class="section-title">Комментарии <q-btn flat> <q-badge>{{ post.comments.length }}</q-badge></q-btn></h2>
      <cip-post-commets :comments="post.comments" :postId="post.id"/>
    </section>
    <!--    /// Comments   -->
  </q-page>
</template>

<script>
import CipBreadCumps from "components/service/cipBreadCumps";
import CipPostImage from "components/blog/post/cipPostImage";
import CipBlogPostsScrollX from "components/blog/cipBlogPostsScrollX";
import CipPostCommets from "components/blog/post/cipPostCommets";

export default {
  name: "PostDetail",
  components: {
    CipPostCommets,
    CipBlogPostsScrollX,
    CipPostImage,
    CipBreadCumps,
  },
  computed: {
    post() {
      return this.$store.getters.getPost;
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch("fetchPost", currentRoute.params.slug);
  }
};
</script>

<style lang="sass">
.post-image
  height: 600px

.post-image-meta
  position: absolute
  bottom: 0
  left: 0
  right: 0
  top: 0
  background: linear-gradient(180deg, rgba(0, 0, 0, 0) 30%, #000000 100%) !important
  z-index: 200

@media screen and (max-width: 1440px)
  .post-image
    height: 500px

@media screen and (max-width: 1100px)
  .post-image
    height: 400px

@media screen and (max-width: 650px)
  .post-image
    height: 250px

</style>
