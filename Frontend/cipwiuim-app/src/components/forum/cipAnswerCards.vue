<template>
  <div>
    <q-card
      v-for="answer in answers"
      :key="answer.id"
      class="shadow-0 bg-grey-2"
    >
      <article>
        <div class="answer-grid q-pa-md bg-white q-mt-md rounded-borders">
          <div class="answer-author text-center">
            <p class="text-bold">{{ answer.name }}</p>
          </div>
          <div class="answer">
            <p class="answer-text rounded-borders q-pa-md">{{ answer.text }}</p>

            <!--            Answer for ...   -->
            <div v-if="answer.answer_for" class="q-mt-sm">
              <small class="text-bold">Ответ на {{ messageTitle }}:</small>
              <div class="answer-for q-ml-sm q-pa-sm rounded-borders bg-grey-3">
                <p class="text-bold">
                  <q-icon name="person" class="q-mr-sm"/>
                  {{ answer.answer_for.name }}
                </p>
                <p><i>{{ answer.answer_for.text }}</i></p>
              </div>
            </div>
            <!--            /// Answer for ...   -->

            <div class="answer-meta flex q-mt-sm justify-between" style="align-items: center">
              <div class="flex">
                <p class="text-grey-7">
                  <q-icon name="restore"/>
                  {{ answer.pub_date.split('-')[1] }}
                </p>
                <p class="text-grey-7 q-ml-md">
                  <q-icon name="event"/>
                  {{ answer.pub_date.split('-')[0] }}
                </p>
              </div>
              <q-btn
                label="Ответить"
                color="primary"
                size="sm"
                icon-right="reply"
                unelevated
                @click="$emit('reply', answer)"
              />
            </div>
          </div>
        </div>
      </article>
    </q-card>

  </div>
</template>

<script>
export default {
  name: "cipAnswerCards",
  props: {
    answers: {
      type: Array,
      default: null
    },
    messageTitle: {
      type: String,
      default: 'сообщение'
    }
  }
}
</script>

<style lang="sass">
.answer-grid
  display: grid
  grid-template-columns: 1fr 3fr
  align-items: center
  grid-gap: 15px
  @media (max-width: 650px)
    grid-template-columns: 1fr

.answer-text
  border: 1px solid $grey-5

.answer-for p
  font-size: 12px


</style>
