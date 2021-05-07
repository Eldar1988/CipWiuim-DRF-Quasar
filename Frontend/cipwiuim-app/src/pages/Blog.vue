<template>
<q-page>
  <cip-bread-cumps current-page-title="Информационный блог" />
  <cip-page-title title="Наш блог" />
  <div class="q-mt-md">
    <div v-html="homeData.blog_description"></div>
  </div>
<!--  Posts grid   -->
  <section>
    <div class="posts row q-mt-xl">
      <div
        v-for="post in posts"
        :key="post.id"
        class="col-12 col-sm-6 col-md-4 col-lg-3"
        style="padding: 5px"
      >
        <cip-post-card :post="post"/>
      </div>
    </div>
  </section>
<!--  /// Posts grid   -->

</q-page>
</template>

<script>
import CipPageTitle from "components/cipPageTitle";
import CipBreadCumps from "components/service/cipBreadCumps";
import CipPostCard from "components/blog/cipPostCard";
export default {
  name: "Blog",
  components: {CipPostCard, CipBreadCumps, CipPageTitle},
  computed: {
    posts() {
      return this.$store.getters.getPosts
    },
    homeData () {
      return this.$store.getters.getMainData.homeMeta
    }
  },
  created() {
    this.$store.dispatch('fetchPosts')
  }
}
</script>

<style lang="sass">

</style>
