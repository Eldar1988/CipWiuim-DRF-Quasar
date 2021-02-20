<template>
  <article>
    <q-card class="my-card shadow-0">
      <q-img
        :src="post.image"
        height="250px"
      >
        <q-rating v-model="post.rating" :max="10" size="22px" readonly color="yellow"/>
        <template v-slot:loading>
          <q-skeleton class="full-width" height="250px" square/>
        </template>
      </q-img>

      <q-card-section>
        <q-btn
          fab
          color="primary"
          icon="read_more"
          class="absolute bg-gradient-1 blue-shadow" unelevated
          style="top: 0; right: 12px; transform: translateY(-50%);"
          :to="`/blog/post/${post.slug}`"
          padding="10px"
        >
          <q-tooltip>Читать далее</q-tooltip>
        </q-btn>

        <div class="row no-wrap items-center">
          <div class="col text-h6 ellipsis">
            <router-link :to="`/blog/post/${post.slug}`">
              {{ post.title }}
            </router-link>
            <q-tooltip>{{ post.title }}</q-tooltip>
          </div>
        </div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        <div class="text-grey ellipsis-2-lines">
          <p>
            {{ post.description }}
          </p>
        </div>
      </q-card-section>
    </q-card>
  </article>
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
