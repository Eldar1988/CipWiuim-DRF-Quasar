<template>
  <q-card class="my-card">
    <q-img
      :src="post.image"
      height="250px"
    />

    <q-card-section>
      <q-btn
        fab
        color="primary"
        icon="mdi-arrow-right-bold"
        class="absolute bg-gradient-1"
        style="top: 0; right: 12px; transform: translateY(-50%);"
        :to="`/blog/post/${post.slug}`"
      />

      <div class="row no-wrap items-center">
        <div class="col text-h6 ellipsis">
          {{ post.title }}
        </div>
      </div>

      <q-rating v-model="post.rating" :max="10" size="22px" readonly />
    </q-card-section>

    <q-card-section class="q-pt-none">
      <div class="text-grey ellipsis-2-lines">
        {{ post.description }}
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: "cipPostCard",
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
