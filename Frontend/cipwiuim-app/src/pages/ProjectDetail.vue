<template>
  <q-page>
    <cip-bread-cumps :current-page-title="project.title" :pages="[{title: 'Проекты', slug: '/projects'}]"/>
    <article>
      <cip-page-title :title="project.title"/>
      <!--      First section - Main info   -->
      <section class="main-info">
        <div class="main-info-section-grid q-mt-xl">
          <div>
            <div class="project-description" v-html="project.short_description"></div>
            <cip-files-list v-if="project.files.length > 0" :files="project.files" class="q-mt-xl"/>
          </div>
          <!--          Company card   -->
          <div class="project-company q-mt-lg">
            <cip-company-card :company="project.company"/>
          </div>
          <!--          /// Company card   -->
        </div>
        <div class="bg-white q-pa-md q-mt-xl rounded-borders">
          <div v-html="project.bio"></div>
        </div>
      </section>
    </article>
    <!--      /// First section - Main info   -->

    <!--      Benefits   -->
    <section v-if="project.benefits.length > 0" class="text-center section">
      <h2 class="section-title">Преференции</h2>
      <cip-project-benefits :benefits="project.benefits"/>
    </section>
    <!--      /// Benefits   -->

    <!--      Video slider   -->
    <section v-if="project.videos.length > 0" class="text-center section">
      <h2 class="section-title">Видео</h2>
      <cip-video-slider :videos="project.videos" class="q-mt-md"/>
    </section>
    <!--      /// Video slider   -->

    <!--    Structure   -->
    <section v-if="project.structures.length > 0" class="section">
      <h2 class="section-title text-center">Структура проекта</h2>
      <cip-structure-slider :structure="project.structures" class="q-mt-md"/>
    </section>
    <!--    /// Structure   -->

    <!--    Questions & Forum   -->
    <section v-if="project.questions.length > 0" class="section">
      <div class="question-and-forum-grid">
        <div class="questions">
          <h2 class="section-title">Вопросы и ответы</h2>
          <cip-qustions :questions="project.questions" class="q-mt-md"/>
        </div>
        <div class="go-to-forum q-mt-xl">
          <q-card
            class="go-to-forum-card shadow-0 rounded-borders flex flex-center column q-py-xl q-px-sm text-center"
            style="min-height: 100%"
          >
            <h3 class="text-h6">Вы можете обсудить проект на форуме</h3>
            <q-btn
              v-if="project.forum_themes && project.forum_themes.length > 0"
              label="Перейти к обсуждению"
              color="primary"
              text-color="white"
              icon-right="forward"
              class="q-mt-md bg-gradient-1 my-shadow"
              no-caps unelevated
              :to="`/forum/${project.forum_themes[0].slug}`"
            />
          </q-card>
        </div>
      </div>
    </section>
    <!--    /// Questions & Forum   -->

    <!--    Project testimonials   -->
    <section v-if="project.reviews.length > 0" class="section">
      <h2 class="section-title text-center">Отзывы о проекте</h2>
      <cip-testimonials-cards :testimonials="project.reviews" class="q-mt-md"/>
    </section>
    <!--    /// Project testimonials   -->

  </q-page>
</template>

<script>
import CipPageTitle from "components/cipPageTitle";
import CipBreadCumps from "components/service/cipBreadCumps";
import CipCompanyCard from "components/company/cipCompanyCard";
import CipFilesList from "components/service/cipFilesList";
import CipVideoSlider from "components/service/cipVideoSlider";
import CipProjectBenefits from "components/projects/cipProjectBenefits";
import CipStructureSlider from "components/projects/cipStructureSlider";
import CipQustions from "components/service/cipQustions";
import CipTestimonialsCards from "components/home/cipTestimonialsCards";

export default {
  name: "ProjectDetail",
  components: {
    CipTestimonialsCards,
    CipQustions,
    CipStructureSlider,
    CipProjectBenefits, CipVideoSlider, CipFilesList, CipCompanyCard, CipBreadCumps, CipPageTitle
  },
  computed: {
    project() {
      return this.$store.getters.getProject
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchProjectDetail', currentRoute.params.slug)
  }
}
</script>

<style lang="sass">
.main-info-section-grid
  display: grid
  grid-template-columns: 3fr 1fr
  grid-gap: 30px
  align-items: center

.question-and-forum-grid
  display: grid
  grid-template-columns: 1fr 1fr
  grid-gap: 50px

@media screen and (max-width: 800px)
  .main-info-section-grid
    grid-template-columns: 1fr
    grid-gap: 20px

  .question-and-forum-grid
    grid-template-columns: 1fr
</style>
