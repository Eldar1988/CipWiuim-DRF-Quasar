<template>
  <article>
    <div class="answer-grid q-pa-md bg-white q-mt-md rounded-borders">
      <div class="answer-author text-center">
        <p class="text-bold">{{ comment.name }}</p>
      </div>
      <div class="answer">
        <p class="answer-text rounded-borders q-pa-md">{{ comment.text }}</p>

        <div class="answer-meta flex q-mt-sm justify-between" style="align-items: center">
          <div class="flex">
            <p class="text-grey-7">
              <q-icon name="restore"/>
              {{ comment.pub_date.split('-')[1] }}
            </p>
            <p class="text-grey-7 q-ml-md">
              <q-icon name="event"/>
              {{ comment.pub_date.split('-')[0] }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </article>
</template>

<script>
export default {
  name: "cipPostCommentCard",
  props: {
    comment: {
      type: Object,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
