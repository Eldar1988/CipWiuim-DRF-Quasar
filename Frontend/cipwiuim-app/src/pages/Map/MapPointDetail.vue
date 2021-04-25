<template>
  <q-page>
    <cip-bread-cumps
      :current-page-title="point.title"
      :pages="[{title:'Виды деятельности', slug: '/activities'}, {title: point.region.title, slug: `/activities/${point.region.slug}` }]"
    />
    <cip-page-title :title="point.title"/>
    <div id="map2" class="q-mt-xl rounded-borders overflow-hidden shadow-lt" style="height: 50vh">
    </div>
    <q-img v-if="point.image" :src="point.image" height="60vh" class="rounded-borders shadow-lt q-mt-lg"/>
    <div class="q-mt-lg">
      <div v-html="point.description"></div>
    </div>
    <div class="q-mt-lg">
      <cip-share />
    </div>
  </q-page>
</template>

<script>
import CipBreadCumps from "components/service/cipBreadCumps";
import CipPageTitle from "components/cipPageTitle";
import CipShare from "components/service/cipShare";

export default {
  name: "MapPointDetail",
  components: {CipShare, CipPageTitle, CipBreadCumps},
  computed: {
    point() {
      return this.$store.getters.getPoint
    }
  },
  created() {
    this.map()
  },
  methods: {
    map() {
      ymaps.ready(this.init);
    },
    init() {

      let myMap = new ymaps.Map("map2", {
        center: this.point.coordinates.split(','),
        // center: [51.248854, 71.160291],
        zoom: 8
      });
      let coordinates = []
      this.point.coordinates.split(',').forEach(item => coordinates.push(+item))
      let myPlacemark = new ymaps.Placemark(coordinates, {
        // Чтобы балун и хинт открывались на метке, необходимо задать ей определенные свойства.
        balloonContentHeader: this.point.title,
        hintContent: this.point.title,
      });
      myMap.geoObjects.add(myPlacemark);

    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('loadMapPoint', currentRoute.params.slug)
  }
}
</script>

<style scoped>

</style>
