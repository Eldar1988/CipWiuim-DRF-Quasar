<template>
  <div>
    <div class="forum-themes-grid q-mt-lg">
      <q-card
        v-for="theme in themes"
        :key="theme"
        class="forum-theme-card shadow-0 q-pa-md"
      >
        <!--        Theme meta   -->
        <div class="q-pa-sm text-left">
          <small class="answers-count q-my-sm text-right text-grey-7 block">
            <q-icon name="chat_bubble_outline"/> {{ theme.answers.length }}
            <q-icon name="restore" class="q-ml-md"/> {{ theme.pub_date.split('-')[0] }}
          </small>
          <router-link :to="`/forum/${theme.slug}`">
            <h3 class="forum-theme-card-title text-bold ">{{ theme.title }}</h3>
          </router-link>
          <p class="q-mt-sm">{{ theme.description }}</p>

          <!--          Actions   -->
          <q-btn
            label="Перейти к обсуждению"
            no-caps
            class="q-mt-md bg-gradient-1 my-shadow"
            text-color="white"
            unelevated
            :to="`/forum/${theme.slug}`"
          />
          <q-btn
            label="О проекте"
            no-caps
            class="q-mt-md q-ml-md"
            color="primary"
            outline
            unelevated
            :to="`/projects/${theme.project.slug}`"
          />

          <!--          /// Actions   -->
          <q-separator class="q-mt-md"/>
          <!--        Author   -->
          <router-link :to="`/profile/${theme.author.id}`">
            <div class="theme-card-author q-mt-sm flex" style="align-items: center">

              <q-avatar size="30px">
                <q-img
                  :src="theme.author.avatar"
                />
              </q-avatar>
              <p class="q-ml-sm">{{ theme.author.name }}</p>
            </div>
          </router-link>

          <!--        /// Author   -->
        </div>
        <!--        /// Theme meta   -->


      </q-card>
    </div>
  </div>
</template>

<script>
export default {
  name: "cipForumThemesGrid",
  props: {
    themes: {
      type: Array,
      default: null
    }
  }
}
</script>

<style lang="sass">
.forum-themes-grid
  display: grid
  grid-template-columns: 1fr 1fr
  grid-gap: 30px

.forum-theme-card-author
  padding: 10px
  border-right: 1px solid $grey-3 !important

.forum-theme-card-title
  font-size: 22px


@media screen and (max-width: 650px)
  .forum-themes-grid
    grid-template-columns: 1fr
    grid-gap: 20px

  .forum-theme-card-title
    font-size: 16px

</style>
