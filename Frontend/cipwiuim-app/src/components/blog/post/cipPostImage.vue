<template>
  <q-img
    :src="post.image"
    class="post-image rounded-borders shadow-5 img-overlay"
  >
    <template v-slot:loading>
      <q-skeleton class="post-image full-width" />
    </template>
    <q-rating v-model="post.rating" max="10" color="yellow" />

    <div class="img-text">
      <cip-page-title :title="post.title"/>
    </div>
  </q-img>
</template>

<script>
import cipPageTitle from "components/cipPageTitle";
export default {
  name: "cipPostImage",
  components: {cipPageTitle},
  props: {
    post: {
      type: Object,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
