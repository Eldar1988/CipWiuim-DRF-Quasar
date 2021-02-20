<template>
<q-page>
  <cip-bread-cumps current-page-title="Информационный блог" />
  <cip-page-title title="Наш блог" subtitle="Где бы человек не находился, он там и должен улучшить свое благосостояние. Вместе с «CIP WIUIM» вы сможете его улучшить не только для себя, но и для всех жителей Центрально-азиатского региона. Не пропустите последние новости, присоединяйтесь к нашему блогу! " />
<!--  Posts grid   -->
  <section>
    <div class="posts row section">
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
    }
  },
  created() {
    this.$store.dispatch('fetchPosts')
  }
}
</script>

<style lang="sass">

</style>
