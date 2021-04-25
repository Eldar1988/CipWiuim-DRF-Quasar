<template>
  <q-page>
    <cip-bread-cumps :current-page-title="theme.title" :pages="[{title: 'Форум', slug: '/forum'}]"/>
    <cip-page-title :title="theme.title"/>
    <section>
      <div class="theme-detail-grid">
        <!--      Theme author   -->
        <div class="forum-theme-author">
          <cip-profile-card cardTitle="Автор темы" :profile="theme.author" />
          <cip-share class="q-mt-md"/>
        </div>
        <!--      /// Theme author   -->

        <div>
          <div class="theme-detail bg-white q-px-md q-pt-xl q-pb-md rounded-borders">

            <!--      Theme detail   -->
            <article>
              <div v-html="theme.body"></div>
              <q-btn
                v-if="theme.project"
                label="Перейти к проекту"
                class="bg-gradient-1 q-mt-md my-shadow"
                text-color="white"
                icon-right="forward"
                unelevated
                :to="`/projects/${theme.project.slug}`"
              />
              <q-separator class="q-mt-xl"/>
              <div class="theme-detail-meta q-mt-md flex ">
                <p class="text-grey-7">
                  <q-icon name="restore"/>
                  {{ theme.pub_date.split('-')[0] }}
                </p>
                <p class="text-grey-7 q-ml-md">
                  <q-icon name="chat"/>
                  {{ theme.answers.length }}
                </p>
              </div>
            </article>
            <!--      /// Theme detail   -->

          </div>
          <div id="answer-form"></div>
          <!--          Answer form   -->
          <cip-answer-form :theme-id="theme.id" :answer-for="answerFor" :theme-slug="theme.slug"/>
          <!--          /// Answer form   -->

          <!--          Answer cards   -->
          <div class="answers-title q-mt-xl flex justify-between">
            <h2 class="section-title">Ответы</h2>
            <q-btn
              label="Обновить ленту"
              icon-right="autorenew"
              color="primary"
              outline
              size="sm"
              :loading="reloadThemeLoading"
              @click="reloadAnswers"
            />
          </div>
          <cip-answer-cards :answers="theme.answers" @reply="reply"/>
          <!--          /// Answer cards   -->
        </div>
      </div>
    </section>
  </q-page>
</template>

<script>
import CipPageTitle from "components/cipPageTitle";
import CipBreadCumps from "components/service/cipBreadCumps";
import CipShare from "components/service/cipShare";
import CipAnswerCards from "components/forum/cipAnswerCards";
import CipAnswerForm from "components/forum/cipAnswerForm";
import CipProfileCard from "components/profile/cipProfileCard";

export default {
  name: "ForumThemeDetail",
  components: {CipProfileCard, CipAnswerForm, CipAnswerCards, CipShare, CipBreadCumps, CipPageTitle},
  computed: {
    theme() {
      return this.$store.getters.getForumTheme
    }
  },
  data() {
    return {
      reloadThemeLoading: false,
      answerFor: null,
    }
  },
  methods: {
    reply(answer) {
      this.answerFor = answer
      document.querySelector('#answer-form').scrollIntoView({
        behavior: 'smooth'
      })
    },
    async reloadAnswers() {
      this.reloadThemeLoading = true
      setTimeout(() => {
        this.$q.notify('Лента сообщений обновлена')
        this.reloadThemeLoading = false
        this.$store.dispatch('fetchForumThemeData', this.theme.slug)
      }, 1000)
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchForumThemeData', currentRoute.params.slug)
  }
}
</script>

<style lang="sass">
.theme-detail-grid
  margin-top: 50px
  display: grid
  grid-template-columns: 1fr 3fr
  grid-gap: 30px

@media screen and (max-width: 650px)
  .theme-detail-grid
    grid-template-columns: 1fr
</style>
